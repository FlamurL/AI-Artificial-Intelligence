from searching_framework import *


def move_up(param):
    return (param[0], param[1] + 1)


def move_down(param):
    return (param[0], param[1] - 1)


def move_left(param):
    return (param[0] - 1, param[1])





def move_right_two(param):
    return (param[0] + 2, param[1])


def move_right_three(param):
    return (param[0] + 3, param[1])


def check_validity(state, n, obstacles):
    x, y = state
    if not (0 <= x < n and 0 <= y < n):
        return False
    if state in obstacles:
        return False
    return True


def check_validity_two(state, n, obstacles):
    x, y = state
    if not (0 <= x < n and 0 <= y < n):
        return False
    if (x, y) in obstacles or (x - 1, y) in obstacles:
        return False
    return True


def check_validity_three(state, n, obstacles):
    x, y = state
    if not (0 <= x < n and 0 <= y < n):
        return False
    if (x, y) in obstacles or (x - 1, y) in obstacles or (x - 2, y) in obstacles:
        return False
    return True


class Labyrinth(Problem):
    def __init__(self, initial, obstacles, n, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles
        self.n = n

    def successor(self, state):
        successors = {}
        pos, goal = state

        state1 = move_up(pos)
        state2 = move_down(pos)
        state3 = move_left(pos)

        state5 = move_right_two(pos)
        state6 = move_right_three(pos)

        if check_validity(state1, self.n, self.obstacles):
            successors["Up"] = (state1, goal)
        if check_validity(state2, self.n, self.obstacles):
            successors["Down"] = (state2, goal)
        if check_validity(state3, self.n, self.obstacles):
            successors["Left"] = (state3, goal)

        if check_validity_three(state6, self.n, self.obstacles):
            successors["Right 3"] = (state6, goal)

        if check_validity_two(state5, self.n, self.obstacles):
            successors["Right 2"] = (state5, goal)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        person = node.state[0]
        p_x, p_y = person
        h_x, h_y = node.state[1]
        dx = abs(h_x - p_x)
        dy = abs(h_y - p_y)

        if dx % 3 == 0:
            horizontal_moves = dx // 3
        else:
            horizontal_moves = dx // 3 + 1

        return dy + horizontal_moves


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    obstacles = []
    for _ in range(m):
        wall = tuple(map(int, input().split(",")))
        obstacles.append(wall)

    man_cord = tuple(map(int, input().split(",")))
    house_cord = tuple(map(int, input().split(",")))
    obstacles = tuple(obstacles)
    initial_state = (man_cord, house_cord)

    labyrinth = Labyrinth(initial_state, obstacles, n)
    answer = astar_search(labyrinth)

    print(answer.solution() if answer else [])