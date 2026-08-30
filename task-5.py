N = int(input("Enter number of students: "))
students = []
for _ in range(N):
    name, marks = input("Enter the student name and marks").split()
    students.append((name, int(marks)))
K = int(input("Enter the k value "))
students = sorted(students, key=lambda x: (-x[1], x[0]))
for student in students[:K]:
    print(student[0] , end="")