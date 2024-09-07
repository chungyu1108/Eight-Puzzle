from __future__ import annotations
from board import Board
from collections.abc import Callable
from queue import PriorityQueue
import numpy as np
import heapq

def MT(board: Board) -> int:
    '''
    Missed Tiles
    '''
    h = 0
    for i in range(3):
        for j in range(3):
            if board.state[i][j] != 0 and board.state[i][j] != board.solution[i][j]:
                h += 1
    return h


def CB(board: Board) -> int:
    '''
    Counts the number of cons in the board's rs and columns
    '''
    num_cons = 0
    n = board.state.shape[0]
    
    for i in range(n):
        c = board.state[:, i]
        r = board.state[i]
        
        # column conflicts
        c_cons = 0
        for j in range(n):
            if c[j] != 0:
                for k in range(j + 1, n):
                    if c[k] != 0 and c[j] > c[k]:
                        c_cons += 1

        # row conflicts
        r_cons = 0
        for j in range(n):
            if r[j] != 0:
                for k in range(j + 1, n):
                    if r[k] != 0 and r[j] > r[k]:
                        r_cons += 1
        

        
        num_cons += r_cons + c_cons
    
    return num_cons



def NA(board: Board) -> int:
    '''
    Counts the number of conflicts in the board's rows and columns
    '''
    num_cons = 0
    n = board.state.shape[0]
    
    for i in range(n):
        c = board.state[:, i]
        r = board.state[i]
        
        # num r cons
        r_cons = 0
        for j in range(n):
            if r[j] != 0:
                for k in range(j + 1, n):
                    if r[k] != 0 and r[j] > r[k]:
                        r_cons += 1
        
        num_cons += r_cons
    
    return num_cons



'''
A* Search 
'''


def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    frontier = []
    heapq.heappush(frontier, (heuristic(board), board))
    visited = set()

    while frontier:
        _, current_state = heapq.heappop(frontier)

        visited.add(tuple(map(tuple, current_state.state)))

        next_states = current_state.next_action_states()

        for next_state, action in next_states:

            if tuple(map(tuple, current_state.state)) == tuple(map(tuple, current_state.solution)):
                return current_state.total_action

            if tuple(map(tuple, next_state.state)) not in visited:
                cost = current_state.g + heuristic(next_state)

                heapq.heappush(frontier, (cost, next_state))

                next_state.g = current_state.g + 1

                next_state.total_action.append(action)

    return None