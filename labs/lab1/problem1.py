from searching_framework import *
import sys
import io



if __name__ == '__main__':
    n = int(input())
    red_apples = []
    green_apples = []
    
    for i in range(n):
        input_array = [int(num) for num in input().split(",")]
        green_apples.append(tuple(input_array))

    m = int(input())
    for i in range(m):
        input_array = [int(num) for num in input().split(",")]
        red_apples.append(tuple(input_array))

    initial_state = (((0, 9), (0, 8), (0, 7)), 'd', tuple(green_apples))
    game = Snake(initial_state, red_apples)

    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    solution = breadth_first_tree_search(game)

    sys.stdout = old_stdout

    if solution is not None:
        print(solution.solution())
    else:
        print([])
