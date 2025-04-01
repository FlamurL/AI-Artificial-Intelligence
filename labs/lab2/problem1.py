from searching_framework import Problem, astar_search

def move_house(house, directions):
    x, y = house
    if directions[0] == 'r':
        if x == 4:
            x = 3
            directions = "left"
        else:
            x += 1
    elif directions[0] == 'l':
        if x == 0:
            x = 1
            directions = "right"
        else:
            x -= 1
    return ((x, y), directions)

def move_diagonally_left(player, param, allowed,hm):
    x, y = player
    if param == 1:
        new_x, new_y = x - 1, y + 1
    else:
        new_x, new_y = x - 2, y + 2
    if (new_x, new_y) in allowed or (new_x, new_y) == hm:
        return (new_x, new_y)
    return None

def move_diagonally_right(player, param, allowed,hm):
    x, y = player
    if param == 1:
        new_x, new_y = x + 1, y + 1
    else:
        new_x, new_y = x + 2, y + 2
    if (new_x, new_y) in allowed or (new_x, new_y) == hm:
        return (new_x, new_y)
    return None

def move_up(player, param, allowed, hm):
    x, y = player
    if param == 1:
        new_x, new_y = x, y + 1
    else:
        new_x, new_y = x, y + 2
    if (new_x, new_y) in allowed or (new_x, new_y) == hm:
        return (new_x, new_y)
    return None

def check_validity(state):
    player = state[0]
    return 0 <= player[0] <= 4 and 0 <= player[1] <= 8


def check_validity_for_stay(stay_state):
    if stay_state[0] == stay_state[1]:
        return False

    return True


class WallClimber(Problem):
    def __init__(self, initial, allow, goal=None):
        super().__init__(initial, goal)
        self.allow = allow
        self.house_movements = list()


    def successor(self, state):
        successors = {}
        player = state[0]
        house = state[1]
        directions = state[2]

        new_house_cord = move_house(house, directions)
        new_house_pos, new_direction = new_house_cord
        self.house_movements=list(self.house_movements)
        self.house_movements.append(new_house_pos)
        self.house_movements=tuple(self.house_movements)

        state1 = move_diagonally_left(player, 1, self.allow,new_house_pos)
        state2 = move_diagonally_left(player, 2, self.allow,new_house_pos)
        state3 = move_diagonally_right(player, 1, self.allow,new_house_pos)
        state4 = move_diagonally_right(player, 2, self.allow,new_house_pos)
        state5 = move_up(player, 1, self.allow,new_house_pos)
        state6 = move_up(player, 2, self.allow,new_house_pos)

        if state1 and check_validity((state1, new_house_pos, new_direction)):

            successors["Up-left 1"] = (state1, new_house_pos, new_direction)
        if state2 and check_validity((state2, new_house_pos, new_direction)):

            successors["Up-left 2"] = (state2, new_house_pos, new_direction)
        if state3 and check_validity((state3, new_house_pos, new_direction)):

            successors["Up-right 1"] = (state3, new_house_pos, new_direction)
        if state4 and check_validity((state4, new_house_pos, new_direction)):

            successors["Up-right 2"] = (state4, new_house_pos, new_direction)
        if state5 and check_validity((state5, new_house_pos, new_direction)):

            successors["Up 1"] = (state5, new_house_pos, new_direction)
        if state6 and check_validity((state6, new_house_pos, new_direction)):

            successors["Up 2"] = (state6, new_house_pos, new_direction)

        stay_state = (player, new_house_pos, new_direction)
        if check_validity_for_stay(stay_state):
            successors["Stay"] = stay_state


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):

        return state[0] == state[1]

    def h(self, node):
        state = node.state
        y_cord = state[0][1]
        if y_cord == 8:
            return 0
        return (8 - y_cord) / 2

if __name__ == '__main__':
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]
    person_cord = [int(i) for i in input().split(",")]
    house_cord = [int(i) for i in input().split(",")]
    direction = input()

    initial_state = (tuple(person_cord), tuple(house_cord), direction)
    set_up = WallClimber(initial_state, allowed)
    answer = astar_search(set_up)

    if answer is not None:
        print(answer.solution())
    else:
        print([])