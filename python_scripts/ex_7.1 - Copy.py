student_grades = [['John', '9', '10', '7', '6'], ['Mary', '9', '8', '8'], ['Smith', '8', '4'], ['Adam', '6', '4', '7', '5', '10']]

total = 0
cnt = 0

for student in student_grades:

    per_student_total = 0

    for grade in student[1:]:
        per_student_total = per_student_total + int(grade)
        total = total + int(grade)
        cnt = cnt + 1

    print(student[0] + "'s average is", per_student_total/len(student[1:]))
print("The class average is", total/cnt)