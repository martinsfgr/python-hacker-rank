from collections import namedtuple

students = []
number_of_students = int(input())
columns = input().split()

Student = namedtuple("student", columns)

for _ in range(number_of_students):
    row = input().split()
    student = Student(*row)
    students.append(student)

sum_marks = 0

for student in students:
    sum_marks += int(student.MARKS)

average = sum_marks/number_of_students
#average = (sum(map(int, (student.MARKS for student in students))))/number_of_students
print(average)
