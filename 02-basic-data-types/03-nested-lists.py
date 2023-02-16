if __name__ == '__main__':
    students = []
    scores = []

    for i in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        scores.append(score)

    second_lowest = sorted(set(scores))[1]
    students = sorted(students)

    for student in students:
        student_name = student[0]
        student_score = student[1]

        if student_score == second_lowest:
            print(student_name)
