"""
Define a class for an Agent that stores its position (coordinates x and y) in some space.

Define a method that represents the movement of the agent in space. Then, define agents that implement specific movements (left, right, up, down).

Perform 5 movements for each of the agents and print the agent's position at each step.
"""

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Position: {self.x}, {self.y}'

    def move(self):
        pass

class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x,y)

    def move(self):
        self.x-=1

class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x+=1

class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y+=1;


class DownAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def move(self):
        self.y-=1


if __name__ =='__main__':
    agentL =LeftAgent(0,0)
    for i in range(5):
        agentL.move()
        print(agentL)

    print()
    agentR =RightAgent(0,0)
    for i in range(5):
        agentR.move()
        print(agentR)
    print()
    agentU =UpAgent(0,0)
    for i in range(5):
        agentU.move()
        print(agentU)
    print()
    agentD = DownAgent(0, 0)
    for i in range(5):
            agentD.move()
            print(agentD)