from __future__ import annotations
from board import Piece, Board, Move

# Encontra o melhor resultado possível para o jogador inicial
def minimax(board: Board, maximizing: bool, original_player: Piece, max_depth: int = 8) -> float:
    # Caso de base - posição final ou profundidade máxima alcançada
    if board.is_win or board.is_draw or max_depth == 0:
        return board.evaluate(original_player)

    # Caso recursivo - maximiza seus ganhos ou minimiza os ganhos do adversário
    if maximizing:
        best_eval: float = float("-inf") # ponto de partida arbitrariamente baixo
        for move in board.legal_moves:
            result: float = minimax(board.move(move), False, original_player, max_depth - 1)
            best_eval = max(result, best_eval)
        return best_eval
    else: # minimizando
        worst_eval: float = float("inf")
        for move in board.legal_moves:
            result = minimax(board.move(move), True, original_player, max_depth - 1)
            worst_eval = min(result, worst_eval)
        return worst_eval

# Encontra o melhor movimento possível na posição atual
# Observando max_depth
def find_best_move(board: Board, max_depth: int = 8) -> Move:
    best_eval: float = float("-inf")
    best_move: Move = Move(-1)
    for move in board.legal_moves:
        result: float = minimax(board.move(move), False, board.turn, max_depth)
        if result > best_eval:
            best_eval = result
            best_move = move
    return best_move
