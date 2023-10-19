student_marks = [78,83,90,88,75]
sum = sum(student_marks)
print(f"The sum of the items in the student marks list is  {sum}")


def display_first_and_last_marks(marks):
    if not marks:
        return "The list of marks is empty."

    first_mark = marks[0]
    last_mark = marks[-1]

    return "First Mark: {}, Last Mark: {}".format(first_mark, last_mark)

#  list of student marks
student_marks = [78, 83, 90, 88, 75]

result = display_first_and_last_marks(student_marks)
print(result)


student_marks = [78, 83, 90, 88, 75]
# adding a new mark
student_marks.append(96)

print(student_marks)


#iv
student_marks = [78, 83, 90, 88, 75]

student_marks = [78, 83, 90, 88, 75]

# Update the marks to 78 and 87
student_marks[0] = 78
student_marks[1] = 87

# Print the updated list
print("Updated student marks:", student_marks)