# Ask for first student name
name = input("Enter student name (or type STOP to quit): ")

# Lists to store names and grades
names = []
grades = []

# Sentinel value
sentinel = "STOP"

# Loop until sentinel is entered
while name.upper() != sentinel:
    # Ask for the grade
    grade = int(input("Enter grade for " + name + ": "))

    # Store them in the lists
    names.append(name)
    grades.append(grade)

    # Ask again for the next name
    name = input("Enter student name (or type STOP to quit): ")

# After loop ends, check if any grades were entered
if len(grades) == 0:
    print("No grades entered.")
else:
    # Calculate results
    total = sum(grades)
    average_grade = total / len(grades)
    highest_grade = max(grades)
    lowest_grade = min(grades)

    # Match names back to grades
    highest_index = grades.index(highest_grade)
    lowest_index = grades.index(lowest_grade)

    # Print results
    print("\nResults:")
    print("Average Grade:", round(average_grade, 2))
    print("Highest Grade:", names[highest_index], "-", highest_grade)
    print("Lowest Grade:", names[lowest_index], "-", lowest_grade)
