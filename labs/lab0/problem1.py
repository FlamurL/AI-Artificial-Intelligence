import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

class Student:
    def __init__(self, name, surname, student_id):
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.courses = {}

    def add_course(self, course, theory, practical, labs):
        total_points = int(theory) + int(practical) + int(labs)
        if 0 <= total_points <= 50:
            grade = 5
        elif 50 < total_points <= 60:
            grade = 6
        elif 60 < total_points <= 70:
            grade = 7
        elif 70 < total_points <= 80:
            grade = 8
        elif 80 < total_points <= 90:
            grade = 9
        elif 90 < total_points <= 100:
            grade = 10
  
        self.courses[course] = grade

    def __repr__(self):
        result = f"Student: {self.name} {self.surname}\n"
        for course, grade in self.courses.items():
            result += f"----{course}: {grade}\n"
        return result

if __name__ == "__main__":
    students = {}
    
    while True:
        line = input().strip()
        if line.lower() == "end":
            break
        
        parts = line.split(",")
    
        
        student_id = parts[2]
        if student_id not in students:
            students[student_id] = Student(parts[0], parts[1], student_id)
        
        students[student_id].add_course(parts[3], parts[4], parts[5], parts[6])

    for student in students.values():
        print(student)
        
