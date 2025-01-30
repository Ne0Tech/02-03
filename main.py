book = {

    "title": "Sample Book Title",

    "author": "Author Name",

    "year": 2020,

    "available": False,

    "genre": "Fiction"

}


def average_numeric_values(input_dict):

    total_sum = 0

    count = 0

    for value in input_dict.values():

        if isinstance(value, (int, float)):

            total_sum += value

            count += 1

    if count > 0:

        return total_sum / count

    else:

        return "No numeric values found"


example_dict = {'a': 1, 'b': 2.5, 'c': 'text', 'd': 4}

average = average_numeric_values(example_dict)

print(average)


students_grades = {}

def add_student(students_grades, student_name, grades):

    if student_name not in students_grades:

        students_grades[student_name] = grades

    else:

        print(f"Student {student_name} already exists.")

add_student(students_grades, "Alice", {"Math": 90, "Science": 85})

add_student(students_grades, "Bob", {"Math": 75, "Science": 80})

print(students_grades)