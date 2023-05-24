from collections import namedtuple


def col_tuple():
    Score = namedtuple('Score', ['marks'])

    # Get number of students from input
    number_of_students = int(input("Enter number of students:"))

    # Get the index of the marks field
    fields = input("Enter  field:").split()
    mark_index = fields.index('marks')

    # Iterate over the student records and compute the average
    total_marks = sum(int(input("Enter marks:").split()[mark_index]) for i in range(number_of_students))
    average=total_marks / number_of_students
    print(average)
    return average
