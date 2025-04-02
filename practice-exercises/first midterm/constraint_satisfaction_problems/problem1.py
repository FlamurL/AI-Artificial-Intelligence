from constraint import *


def sum_constraint(S,E,N,D,M,O,R,Y):

    x = D + 10 * N + 100 * E + 1000 * S
    y = E + 10 * R + 100 * O + 1000 * M  # MORE
    res = Y + 10 * E + 100 * N + 1000 * O + 10000 * M  # MONEY
    return x + y == res


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    problem.addConstraint(AllDifferentConstraint(),variables)
    problem.addConstraint(sum_constraint, variables)



    # Get and print the solution
    print(problem.getSolution())