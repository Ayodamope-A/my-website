
name = input("Enter your name: ")
sentinel = -100
highest_grade = "Empty"
lowest_grade = "Empty"
total_grade = 0
total_num_of_grades = 0
i = 0
while new_grade := int(input("Enter your grade(or -100 to end): ")):
    if new_grade == sentinel:
        break
    total_grade = total_grade + new_grade
    total_num_of_grades += 1
    if highest_grade == "Empty" or new_grade > highest_grade:
        highest_grade = new_grade
    if lowest_grade == "Empty" or new_grade < lowest_grade:
        lowest_grade = new_grade
        continue
    
average_grade = total_grade / total_num_of_grades

print("Student Name: ", name)
print("Highest Grade: ", highest_grade)
print("Average Grade: ", average_grade)
print("Lowest Grade: ", lowest_grade)
