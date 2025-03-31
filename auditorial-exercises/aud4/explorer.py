from searching_framework import *

def get_new_pos_of_obstacle(pos):
    if (pos[1] == 0 and pos[2] == -1) or (pos[1] == 4 and pos[2] == 1):
        pos = (pos[0], pos[1] + pos[2], -pos[2])
    else:
        pos = (pos[0], pos[1] + pos[2], pos[2])
    return pos

def move_right(x, y, obstacles):
    obs1, obs2 = obstacles
    return (x + 1, y, obs1[0], obs1[1], obs1[2], obs2[0], obs2[1], obs2[2])

def move_left(x, y, obstacles):
    obs1, obs2 = obstacles
    return (x - 1, y, obs1[0], obs1[1], obs1[2], obs2[0], obs2[1], obs2[2])

def move_up(x, y, obstacles):
    obs1, obs2 = obstacles
    return (x, y + 1, obs1[0], obs1[1], obs1[2], obs2[0], obs2[1], obs2[2])

def move_down(x, y, obstacles):
    obs1, obs2 = obstacles
    return (x, y - 1, obs1[0], obs1[1], obs1[2], obs2[0], obs2[1], obs2[2])

def is_valid(state):
    x, y = state[0], state[1]
    obstacle_1 = (state[2], state[3])
    obstacle_2 = (state[5], state[6])

    if 0 <= x <= 7 and 0 <= y <= 4:
        if (x, y) != obstacle_1 and (x, y) != obstacle_2:
            return True
    return False

class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        x, y = state[0], state[1]
        obstacle_1 = (state[2], state[3], state[4])
        obstacle_2 = (state[5], state[6], state[7])

        obstacle_1_new = get_new_pos_of_obstacle(obstacle_1)
        obstacle_2_new = get_new_pos_of_obstacle(obstacle_2)
        obstacles = (obstacle_1_new, obstacle_2_new)

        state1 = move_right(x, y, obstacles)
        state2 = move_left(x, y, obstacles)
        state3 = move_up(x, y, obstacles)
        state4 = move_down(x, y, obstacles)

        if is_valid(state1):
            successors["Right"] = state1
        if is_valid(state2):
            successors["Left"] = state2
        if is_valid(state3):
            successors["Up"] = state3
        if is_valid(state4):
            successors["Down"] = state4

        return successors

    def h(self, node):
        x, y = node.state[0], node.state[1]
        x1, y1 = self.goal[0], self.goal[1]
        return abs(x - x1) + abs(y - y1)

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

if __name__ == '__main__':
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house = [house_x, house_y]

    initial_state = (man_x, man_y, 2, 4, -1, 5, 0, 1)
    explorer = Explorer(initial_state, house)

    answer = astar_search(explorer)
    if answer:
        print(answer.solution())
    else:
        print("No path found!")