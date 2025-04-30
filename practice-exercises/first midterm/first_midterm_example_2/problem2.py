from constraint import *


def column_constraint(*tent_variables):
    counts = [0 for _ in range(GRID_SIZE)]
    for tent in tent_variables:
        column = tent[0]
        counts[column] = counts[column] + 1

    for col in range(GRID_SIZE):
        if counts[col] != column_count[col]:
            return False

    return True

def not_a_tree(*tent_variables):
    for tent in tent_variables:
        if tent in trees:
            return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    GRID_SIZE = 6
    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot

    num_trees = int(input())
    trees = []
    for _ in range(num_trees):
        tree_x, tree_y = tuple(int(n) for n in input().split(" "))
        trees.append((tree_x, tree_y))

    column_count = [int(n) for n in input().split()]

    # -----------------------------------------------------
    # ---Izberete promenlivi i domeni so koi bi sakale da rabotite-----

    variables = []
    for index, tree in enumerate(trees):
        tent_domain = []
        for i in [-1, 1]:
            new_x = tree[0] + i
            new_y = tree[1] + i
            if 0 <= new_x < GRID_SIZE:
                tent_domain.append((new_x, tree[1]))
            if 0 <= new_y < GRID_SIZE:
                tent_domain.append((tree[0], new_y))
        variable = f"tree{index}"
        variables.append(variable)
        problem.addVariable(variable, tent_domain)

    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------
    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(not_a_tree, variables)
    problem.addConstraint(column_constraint, variables)

    # -----------------------------------------------------
    # ---Potoa pobarajte reshenie--------------------------

    solution = problem.getSolution()

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----

    for i in range(num_trees):
        x, y = solution[f"tree{i}"]
        print(f"{x} {y}")