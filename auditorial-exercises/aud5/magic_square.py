from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    var=range(1,17)
    domain=range(1,17)

    problem.addVariables(var,domain)
    problem.addConstraint(AllDifferentConstraint(),var)

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34),[row * 4 + i + 1 for i in range(4)])


    for col in range(4):
        problem.addConstraint(ExactSumConstraint(34), [col + 4 * i+1 for i in range(4)])

    problem.addConstraint(ExactSumConstraint(34), range(1, 17, 5))
    problem.addConstraint(ExactSumConstraint(34), range(4, 14, 3))

    print(problem.getSolution())
