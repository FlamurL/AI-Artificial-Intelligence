from searching_framework import *


def move_right(man, boxes, n,newbox):
    new_man = (man[0] + 1, man[1])

    return (new_man, boxes, n,newbox)  # Convert new_box to tuple


def move_up(man, boxes, n,newbox):
    new_man = (man[0], man[1] + 1)

    return (new_man, boxes, n, newbox)  # Convert new_box to tuple


def is_valid(state):
    man, box, n,newbox = state
    if man[0] >= n or man[1] >= n:
        return False
    if man in box:
        return False
    return True


def checkCnt(state):
    new_man, box, n,newbox = state
    new_box=[]

    for b in newbox:
        if b != (new_man[0], new_man[1] + 1) and b != (new_man[0] + 1, new_man[1]) and b != (new_man[0] - 1, new_man[1]) and b != (new_man[0], new_man[1] - 1) and b != (new_man[0] + 1, new_man[1] + 1) and b != (new_man[0] - 1, new_man[1] - 1) and b != (new_man[0] + 1, new_man[1] - 1) and b != (new_man[0] - 1, new_man[1] + 1):
            new_box.append(b)

    new_box=tuple(new_box)
    return (new_man,box,n,new_box)


class Boxes(Problem):
    def __init__(self, initial, n, goal=None):
        super().__init__(initial, goal)
        self.n = n

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        man, boxes, n,newbox = state  # Unpack state properly
        return newbox == ()  # Check if boxes are empty

    def successor(self, state):
        successors = {}
        man_coordinate, boxes_coordinates, n, newbox = state

        state1 = move_right(man_coordinate, boxes_coordinates, n, newbox)
        state2 = move_up(man_coordinate, boxes_coordinates, n,newbox)
        if is_valid(state2):
            state2 = checkCnt(state2)
            successors["Up"] = state2
        if is_valid(state1):
            state1 = checkCnt(state1)
            successors["Right"] = state1

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)
    num_boxes = int(input())
    boxes = []
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    boxes = tuple(boxes)  # Make initial boxes a tuple too
    new_box=boxes
    initial_state = (man_pos, boxes, n,new_box)
    problem = Boxes(initial_state, num_boxes)  # Pass n, not num_boxes

    answer = breadth_first_graph_search(problem)
    if answer is not None:
        print(answer.solution())
    else:
        print('No Solution!')