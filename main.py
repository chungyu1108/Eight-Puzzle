from board import Board
from agent import a_star_search, MT
import time

def main():
    board_10 = []
    board_20 = []
    board_30 = []
    board_40 = []
    board_50 = []
    for m in [10, 20, 30, 40, 50]:
        for seed in range(0, 10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)
            
            start =  time.process_time()
            '''
            ***********************************************
            Solve the Board state here with A*
            ***********************************************
            '''
            solution = a_star_search(board, MT)
            end =  time.process_time()
            solution_cpu_time = end - start
            #print(f"Board: {m}-{seed} solved in {solution_cpu_time:.6f} seconds.")
            #print(f"{solution_cpu_time:.6f},")
            if m == 10:
                board_10.append(len(solution))
            if m == 20:
                board_20.append(len(solution))
            if m == 30:
                board_30.append(len(solution))
            if m == 40:
                board_40.append(len(solution))
            if m == 50:
                board_50.append(len(solution))


    print(f"10,{sum(board_10) / len(board_10)}")
    print(f"20,{sum(board_20) / len(board_20)}")
    print(f"30,{sum(board_30) / len(board_30)}")
    print(f"40,{sum(board_40) / len(board_40)}")
    print(f"50,{sum(board_50) / len(board_50)}")

if __name__ == "__main__":
    main()