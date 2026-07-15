# Start

num_stud = int(input("What is number of students? "))

i = 0
min_grade = 100

while i < num_stud and min_grade > 0:
    i += 1
    grade = int(input("Enter your grade: "))
    if grade < 0 or grade > 100:
        print(f"{grade} It's illegal grade :(")
    elif grade < min_grade:
        min_grade = grade

print(f"The min grade in the class is: {min_grade}!")

# Stop