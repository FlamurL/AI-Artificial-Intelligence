from constraint import Problem, BacktrackingSolver, InSetConstraint

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    simona_free = {13, 14, 16, 19}
    marija_free = {14, 15, 18}
    petar_free = {12, 13, 16, 17, 18, 19}

    possible_times = [12, 13, 14, 15, 16, 17, 18, 19]

    problem.addVariable("meeting_time", possible_times)
    problem.addVariable("Marija_present", [0, 1])
    problem.addVariable("Petar_present", [0, 1])

    def meeting_valid(meeting_time, Marija_present, Petar_present):
        if Marija_present == 0 and Petar_present == 0:
            return False
        if meeting_time not in simona_free:
            return False
        if Marija_present == 1 and meeting_time not in marija_free:
            return False
        if Petar_present == 1 and meeting_time not in petar_free:
            return False
        return True

    problem.addConstraint(meeting_valid, ["meeting_time", "Marija_present", "Petar_present"])

    for solution in problem.getSolutions():
        solution["Simona_present"] = 1
        ordered_solution = {"Simona_present": solution["Simona_present"],
                            "Marija_present": solution["Marija_present"],
                            "Petar_present": solution["Petar_present"],
                            "meeting_time": solution["meeting_time"]}
        print(ordered_solution)
