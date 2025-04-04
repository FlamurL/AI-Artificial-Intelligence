from constraint import *


def check_tent_spacing(*tents):
    for t1 in tents:
        for t2 in tents:
            if t1 != t2:
                if abs(t1[0] - t2[0]) <= 1 and abs(t1[1] - t2[1]) <= 1:
                    return False
    return True


def valid_tent_position(*tents):
    return all(tent not in trees for tent in tents)


if __name__ == '__main__':
    puzzle = Problem(BacktrackingSolver())
    SIZE = 6

    tree_count = int(input())
    trees = [(int(x), int(y)) for x, y in
             [input().split() for _ in range(tree_count)]]

    tent_vars = []
    for idx, (tx, ty) in enumerate(trees):
        possible_spots = [(tx + dx, ty) for dx in [-1, 1] if 0 <= tx + dx < SIZE] + \
                         [(tx, ty + dy) for dy in [-1, 1] if 0 <= ty + dy < SIZE]
        var_name = f"t{idx}"
        tent_vars.append(var_name)
        puzzle.addVariable(var_name, possible_spots)

    puzzle.addConstraint(AllDifferentConstraint(), tent_vars)
    puzzle.addConstraint(valid_tent_position, tent_vars)
    puzzle.addConstraint(check_tent_spacing, tent_vars)

    result = puzzle.getSolution()

    for i in range(tree_count):
        tent_x, tent_y = result[f"t{i}"]
        print(f"{tent_x} {tent_y}")