from searching_framework import *


def isSnakeValid(s, redApples):
    if len(s) != len(set(s)):  
        return False
    for coordinates in s:
        if coordinates in redApples:
            return False
    if 0 <= s[-1][0] < 10 and 0 <= s[-1][1] < 10: 
        return True
    return False

def moveForward(state):
    snake = state[0]
    snakeDirection = state[1]
    greenApples = state[2]
    possibleMoves = {'l': (-1, 0), 'r': (+1, 0), 'd': (0, -1), 'u': (0, +1)}

    newSnakeHead = (snake[-1][0] + possibleMoves[snakeDirection][0], snake[-1][1] + possibleMoves[snakeDirection][1])

    if newSnakeHead in greenApples:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos = tuple(newSnakePos)
        newGreenApples = [apple for apple in greenApples if apple != newSnakeHead]
        newGreenApples = tuple(newGreenApples)
        new_state = (newSnakePos, snakeDirection, newGreenApples)
        return new_state
    else:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos.pop(0)
        newSnakePos = tuple(newSnakePos)
        new_state = (newSnakePos, snakeDirection, greenApples)
        return new_state

def moveLeft(state):
    snake = state[0]
    snakeDirection = state[1]
    greenApples = state[2]
    possibleMoves = {'l': (0, -1), 'r': (0, +1), 'd': (+1, 0), 'u': (-1, 0)}
    newHeadPositions = {'l': 'd', 'r': 'u', 'd': 'r', 'u': 'l'}
    newHeadDirection = newHeadPositions[snakeDirection]
    newSnakeHead = (snake[-1][0] + possibleMoves[snakeDirection][0], snake[-1][1] + possibleMoves[snakeDirection][1])

    if newSnakeHead in greenApples:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos = tuple(newSnakePos)
        newGreenApples = [apple for apple in greenApples if apple != newSnakeHead]
        newGreenApples = tuple(newGreenApples)
        new_state = (newSnakePos, newHeadDirection, newGreenApples)
        return new_state
    else:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos.pop(0)
        newSnakePos = tuple(newSnakePos)
        new_state = (newSnakePos, newHeadDirection, greenApples)
        return new_state

def moveRight(state):
    snake = state[0]
    snakeDirection = state[1]
    greenApples = state[2]
    possibleMoves = {'l': (0, +1), 'r': (0, -1), 'd': (-1, 0), 'u': (+1, 0)}
    newHeadPositions = {'l': 'u', 'r': 'd', 'd': 'l', 'u': 'r'}
    newHeadDirection = newHeadPositions[snakeDirection]
    newSnakeHead = (snake[-1][0] + possibleMoves[snakeDirection][0], snake[-1][1] + possibleMoves[snakeDirection][1])

    if newSnakeHead in greenApples:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos = tuple(newSnakePos)
        newGreenApples = [apple for apple in greenApples if apple != newSnakeHead]
        newGreenApples = tuple(newGreenApples)
        new_state = (newSnakePos, newHeadDirection, newGreenApples)
        return new_state
    else:
        newSnakePos = list(snake)
        newSnakePos.append(newSnakeHead)
        newSnakePos.pop(0)
        newSnakePos = tuple(newSnakePos)
        new_state = (newSnakePos, newHeadDirection, greenApples)
        return new_state

class Snake(Problem):
    def __init__(self, initial,redApples):
        super().__init__(initial, goal=None)
        self.redApples=redApples
        

    def successor(self, state):
        successors = {}
        state1 = moveForward(state)
        state2 = moveRight(state)
        state3 = moveLeft(state)
        if isSnakeValid(state1[0], redApples):
            successors["ContinueStraight"] = state1
        if isSnakeValid(state2[0], redApples):
            successors["TurnRight"] = state2
        if isSnakeValid(state3[0], redApples):
            successors["TurnLeft"] = state3
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[-1] == ()

if __name__ == '__main__':
    n = int(input())
    redApples = []
    greenApples = []
    
    
    
    for i in range(n):
        inputLine=input().split(",")
        coordinates=[]
        for j in inputLine:
            
            coordinates.append(int(j))
        greenApples.append(tuple(coordinates))
        
    
    
    m = int(input())
 
    for i in range(m):
        inputLine=input().split(",")
        coordinates=[]
        for j in inputLine:
            
            coordinates.append(int(j))
        redApples.append(tuple(coordinates))

  
    initial_state = (((0, 9), (0, 8), (0, 7)), 'd', tuple(greenApples))
    game = Snake(initial_state, redApples)


    answer = breadth_first_graph_search(game)

    if answer is not None:
        print(answer.solution())
    else:
        print([])
