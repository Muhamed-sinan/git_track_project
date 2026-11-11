student_name = "Moosaa"

mark1 = 85
mark2 = 50
mark3 = 50

total = mark1 + mark2 + mark3

average = total / 3

if average >= 90:
    grade = "A"

elif average >= 75:
    grade = "B"

elif average >= 50:
    grade = "C"

else:
    grade = "Fail"

print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)



