from constraint import *


def ml_constraint( *ML_domains):
    times = [(int(i[-2])*10+int(i[-1])) for i in ML_domains]
    return len(times) == len(set(times))


def different_time_constraint(a, b):
    d1, t1 = a.split("_")
    d2, t2 = b.split("_")
    if d1 == d2 and abs(int(t1) - int(t2)) <= 1:
        return False
    return True



if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lectures_AI = input()
    lectures_ML = input()
    lectures_R = input()
    lectures_BI = input()

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_tutorials_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_tutorials_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_tutorials_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------
    ai_variables = []
    for i in range(1,int(lectures_AI)+1):
        ai_variables.append(f"AI_lecture_{i}")


    ml_variables = []
    for i in range(1,int(lectures_ML)+1):
        ml_variables.append(f"ML_lecture_{i}")


    r_variables = []
    for i in range(1,int(lectures_R)+1):
        r_variables.append(f"R_lecture_{i}")


    bi_variables = []
    for i in range(1,int(lectures_BI)+1):
        bi_variables.append(f"BI_lecture_{i}")


    problem.addVariables(ai_variables,AI_lectures_domain)
    problem.addVariable("AI_tutorial",AI_tutorials_domain)

    problem.addVariables(ml_variables,ML_lectures_domain)
    problem.addVariable("ML_tutorial",ML_tutorials_domain)

    problem.addVariables(r_variables,R_lectures_domain)


    problem.addVariables(bi_variables,BI_lectures_domain)
    problem.addVariable("BI_tutorial",BI_tutorials_domain)

    total = ai_variables + ml_variables + r_variables + bi_variables + ["ML_tutorial", "BI_tutorial", "AI_tutorial"]

    for i in total:
        for j in total:
            if i != j:
                problem.addConstraint(different_time_constraint, (i,j))
    problem.addConstraint(ml_constraint, ml_variables + ["ML_tutorial"])


    solution = problem.getSolution()

    print(solution)