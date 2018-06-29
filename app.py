student_list = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        marks = self.marks
        if marks:
            return sum(marks) / len(marks)
        return 0


def create_student():
    name = input("Enter student name:  ")
    student_info = Student(name)
    return student_info


def add_mark(student, mark):
    student.marks.append(mark)


def print_student_details(student):
    print(
        "{name}\nGrade Average:  {avg}\nMarks:  {marks}\n".format(
            name=student.name,
            avg=student.average_mark(),
            marks=student.marks,
        )
    )


def get_menu_input():
    choice = input("PASQ Student Database:"
                      "\nP - print student list"
                      "\nA - Add a mark to a student"
                      "\nS - Add a new student"
                      "\nQ - Quit program"
                      "\n\nWhat would you like to do?  ")
    return choice


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {id}".format(id=i))
        print_student_details(student)


def menu():
    selection = get_menu_input()
    while selection.lower() != 'q':
        print("--------------------")
        if selection.lower() == 'p':
            print_student_list(student_list)
        elif selection.lower() == "a":
            student_id = int(input("Enter student ID:  "))
            student = student_list[student_id]
            new_mark = int(input("Enter new mark:  "))
            add_mark(student, new_mark)
        elif selection.lower() == "s":
            student_list.append(create_student())
        else:
            print("I didn't understand that command.")
        print("--------------------")
        selection = get_menu_input()
    print("Goodbye!")


menu()

