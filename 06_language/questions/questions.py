import math
import os
import string
import sys
from collections import Counter

import nltk

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    file_contents = {}
    
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents[file_name] = file.read()
    
    return file_contents


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    tokens = nltk.word_tokenize(document.lower())
    punctuations = set(string.punctuation)
    stopwords = set(nltk.corpus.stopwords.words("english"))

    return list(filter(lambda t: t not in punctuations and t not in stopwords, tokens))


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    num_doc = Counter()
    for words in documents.values():
        num_doc.update(set(words))

    idfs = dict()
    for word, num_doc_has_word in num_doc.items():
        idfs[word] = math.log(len(documents) / num_doc_has_word)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """

    def get_score(file):
        """
        Computes the score of a file by calculating the sum of tf-idf for
        each word in query
        """
        score = 0
        for word in query:
            tf = sum(w == word for w in files[file])
            score += tf * idfs[word]
        return score

    return sorted(files.keys(), key=lambda file: get_score(file), reverse=True)[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """

    def get_score(sentence):
        """
        Computes the score of a sentence by calculating the sum of idfs
        for each word in query and query term density
        """
        document = sentences[sentence]

        idf_sum = sum(idfs[word] for word in set(query) if word in set(document))
        term_density = sum(word in query for word in document) / len(document)

        return idf_sum, term_density

    return sorted(sentences.keys(), key=lambda st: get_score(st), reverse=True)[:n]


if __name__ == "__main__":
    main()
