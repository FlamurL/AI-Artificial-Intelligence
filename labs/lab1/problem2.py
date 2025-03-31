from searching_framework import * 

def get_adjacent_cells(block):
    surrounding_cells = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            surrounding_cells.add((block[0] + dx, block[1] + dy))
    return surrounding_cells

def is_within_bounds(coord):
    return 0 <= coord[0] < 8 and 0 <= coord[1] < 6

def check_state(state, obstacles): 
    player = state[0]
    ball = state[1]
    if player in obstacles or ball in obstacles:
        return False
    for obstacle in obstacles:
        if ball in get_adjacent_cells(obstacle):
            return False
    return is_within_bounds(player) and is_within_bounds(ball)


class Football(Problem):
    def __init__(self, initial, obstacles_coord, goal_coord):
        super().__init__(initial, goal=None)  
        self.obstacles_coord = obstacles_coord
        self.goal_coord = goal_coord

    def successor(self, state):
        ways_to_go = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        actions_on_ways_if_no_ball = [
            "Move man up", "Move man up-right", "Move man right",
            "Move man down-right", "Move man down"
        ]
        actions_on_ways_if_ball = [
            "Push ball up", "Push ball up-right", "Push ball right",
            "Push ball down-right", "Push ball down"
        ]

        successors = {}
        player, ball = state  

        for i in range(len(ways_to_go)):  
            way = ways_to_go[i]
            actionBall = actions_on_ways_if_ball[i]
            actionNoBall = actions_on_ways_if_no_ball[i]

            new_coord = (player[0] + way[0], player[1] + way[1])

            if new_coord == ball:  
                new_ball = (new_coord[0] + way[0], new_coord[1] + way[1])
                new_state = (new_coord, new_ball)
                if check_state(new_state, self.obstacles_coord):
                    successors[actionBall] = new_state
            else:  
                new_state = (new_coord, ball)
                if check_state(new_state, self.obstacles_coord):
                    successors[actionNoBall] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal_coord


if __name__ == '__main__':
    playerCoordinates = tuple(map(int, input().split(",")))
    ballCoordinates = tuple(map(int, input().split(",")))

    obstacles = ((3, 3), (5, 4))
    goal = ((7, 2), (7, 3))  

    initial_state = (playerCoordinates, ballCoordinates)

    football = Football(initial_state, obstacles, goal)

    result = breadth_first_graph_search(football)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")
