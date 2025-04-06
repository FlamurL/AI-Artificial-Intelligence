from utils import *
from uninformed_search import *
from informed_search import *

def move_left(state):
    man, box, n ,new=state
    new_man=(man[0]-1,man[1])

    return (new_man,box,n,new)


def move_down(state):
    man, box, n, new = state
    new_man = (man[0] , man[1]-1)

    return (new_man, box, n, new)


def is_valid(state):
    man, box, n, new = state
    if man[0]<0 or 0>man[1]:
        return False
    if man in box:
        return False
    return True

def updateBox(state):
    man, box, n, new = state
    newb=[]
    for b in new:
        if b != (man[0]+1,man[1]) and b != (man[0]+1,man[1]-1) and b != (man[0]+1,man[1]+1) and b != (man[0]-1,man[1]) and b != (man[0]-1,man[1]-1) and b != (man[0]-1,man[1]+1) and b != (man[0],man[1]+1) and b != (man[0],man[1]-1):
            newb.append(b)

    newb=tuple(newb)
    return (man,box,n,newb)


class Boxes(Problem):
    def __init__(self, initial,goal=None):
        super().__init__(initial, goal)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[-1] == ()

    def successor(self, state):
        successors = {}
        state1=move_left(state)
        state2=move_down(state)
        if is_valid(state2):
            state2=updateBox(state2)
            successors["Down"]=state2
        if is_valid(state1):
            state1=updateBox(state1)
            successors["Left"]=state1





        return successors



if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, n-1)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))
    boxes = tuple(boxes)
    new_box=boxes
    initial_state=(man_pos,boxes,n,new_box)
    problem= Boxes(initial_state)

    answer=breadth_first_graph_search(problem)

    if answer is not None:
        print(answer.solution())
    else:
        print("No Solution!")