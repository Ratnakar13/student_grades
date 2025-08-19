# Dictionary storing students' names with their marks
students_marks={
    "jenny":92,
    "ratnakar":78,
    "giri":56,
    "avd sai":41,
    "krk":99,
    "karthik":34
}

# Empty dictionary to store students' grades
students_grades={}

# Loop through each student in students_marks
for student in students_marks:
    markes=students_marks[student]

     # Assign grades based on marks
    if markes > 90:
        students_grades[student]="+A"    # Grade for marks > 90
    elif markes > 80:
        students_grades[student]="A"     # Grade for marks > 80
    elif markes > 90:
        students_grades[student]="+B"    # Grade for marks > 70
    elif markes > 60:
        students_grades[student]="B"     # Grade for marks > 60
    elif markes > 50:
        students_grades[student]="C"     # Grade for marks > 50
    elif markes > 40:
        students_grades[student]="D"     # Grade for marks > 40
    else:
        students_grades[student]="F"     # Grade for marks <= 40

print(students_grades)