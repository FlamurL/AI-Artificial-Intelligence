from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3]:
        x1 += 1
    return (x1,y1)


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return (x1,y1)


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return (x1,y1)


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return (x1,y1)


def is_valid(new_state_x,new_state_y, old_x, old_y):
    # Check if position actually changed and is not occupied by obstacles

    if new_state_x == old_x and new_state_y == old_y:
        return False
    return True


class Molecule(Problem):
    def __init__(self,  initial,obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]


        new_pos = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h1_x, h1_y):
            successors["RightH1"] = (new_pos[0], new_pos[1], o_x, o_y, h2_x, h2_y)

        new_pos = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h1_x, h1_y):
            successors["LeftH1"] = (new_pos[0], new_pos[1], o_x, o_y, h2_x, h2_y)

        new_pos = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h1_x, h1_y):
            successors["UpH1"] = (new_pos[0], new_pos[1], o_x, o_y, h2_x, h2_y)

        new_pos = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h1_x, h1_y):
            successors["DownH1"] = (new_pos[0], new_pos[1], o_x, o_y, h2_x, h2_y)


        new_pos = move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h2_x, h2_y):
            successors["RightH2"] = (h1_x, h1_y, o_x, o_y, new_pos[0], new_pos[1])

        new_pos = move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h2_x, h2_y):
            successors["LeftH2"] = (h1_x, h1_y, o_x, o_y, new_pos[0], new_pos[1])

        new_pos = move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h2_x, h2_y):
            successors["UpH2"] = (h1_x, h1_y, o_x, o_y, new_pos[0], new_pos[1])

        new_pos = move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], h2_x, h2_y):
            successors["DownH2"] = (h1_x, h1_y, o_x, o_y, new_pos[0], new_pos[1])


        new_pos = move_right(o_x, o_y, h2_x, h2_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], o_x, o_y):
            successors["RightO"] = (h1_x, h1_y, new_pos[0], new_pos[1], h2_x, h2_y)

        new_pos = move_left(o_x, o_y, h2_x, h2_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], o_x, o_y):
            successors["LeftO"] = (h1_x, h1_y, new_pos[0], new_pos[1], h2_x, h2_y)

        new_pos = move_up(o_x, o_y, h2_x, h2_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], o_x, o_y):
            successors["UpO"] = (h1_x, h1_y, new_pos[0], new_pos[1], h2_x, h2_y)

        new_pos = move_down(o_x, o_y, h2_x, h2_y, h1_x, h1_y, self.obstacles)
        if is_valid(new_pos[0], new_pos[1], o_x, o_y):
            successors["DownO"] = (h1_x, h1_y, new_pos[0], new_pos[1], h2_x, h2_y)

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        # H1 O H2
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule( (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]),obstacles_list)

    result = breadth_first_graph_search(molecule)
    print(result.solution())