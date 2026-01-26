"""Module to manage student records including marks and contact information."""

from os import path
from pickle import load, dump


# //// EXCEPTIONS ////

class StudentNotFoundError(Exception):
    """Used when a student is not found in the dictionary."""

    pass


class InvalidMarkError(Exception):
    """Used when mark is not between 0 and 10."""

    pass


class DuplicateStudentError(Exception):
    """Used when student id already registered."""

    pass


# //// VALIDATION ////

def check_mark(mark):
    """Validate if a grade is within the allowed range.

    input:
        mark (float): The numeric grade to validate.
    """
    if mark < 0 or mark > 10:
        raise InvalidMarkError(f"The mark provided {mark} is out of range.")


def duplicated_student(student, list_dict):
    """Check if a student already exists in the records to avoid overwritting.

    input:
        student (str): The name of the student.
        list_dict (list): The list of dictionaries containing all students.
    """
    for students in list_dict:
        if student.lower() == students["name"].lower():
            raise DuplicateStudentError(
                f"The student {student} already exists."
                )


# //// CONFIGURATION ////

def open_lib():
    """Know whether the file and the content are created or not.

    We have to use the format "file = <filename>".
    If the name don't exist we use the default one (bin_file) to avoid errors.

    output (str): The name of the file where student data is stored.
    """
    main_file = "students.cfg"
    bin_file = "students.dat"
    text_to_read = ""

    if not path.exists(main_file):
        with open(main_file, "w") as settings:
            settings.write(f"file={bin_file}")
        return bin_file

    with open(main_file, "r") as settings:
        text_to_read = settings.read().strip()

        if not text_to_read or "file=" not in text_to_read:
            return bin_file

        # We need to separate the name and "file=", so we split in the "=".
        divide = text_to_read.split("=", 1)

        if len(divide) < 2:
            return bin_file

        part_we_need = divide[1].strip()
        if not part_we_need:
            return bin_file

        # To avoid getting useless text, we split and get just the name.
        filename = part_we_need.split()[0]
        return filename


def load_binary(filename):
    """Read student data from a binary file using the pickle module.

    input:
        filename (str): The name of the binary file to load.

    output (list): A list of dictionaries containing student data.
    """
    try:
        with open(filename, "rb") as file:
            return load(file)
    except EOFError:
        print(" Something went wrong with the file.")
        print("Starting with an empty list.")
        return []
    except FileNotFoundError:
        return []


def save_binary(filename, list_dict):
    """Save the student dictionary into a binary file.

    input:
        filename (str): The name of the file where data will be stored.
        list_dict (list): A list containing student information to save.
    """
    try:
        with open(filename, "wb") as file:
            dump(list_dict, file)
    except Exception as error:
        print(f"An unexpected error occurred while saving {error}")


# //// DATA PROCESSING ////

# //// -m ////

def sort_dict(list_dict):
    """Sort the dictionaries by the mark.

    input:
        list_dict (list): A list of dictionaries containing student data.

    output (list): A list containing all the ordered dictionaries.
    """
    ordered_list = sorted(
        list_dict, key=lambda student: student["mark"], reverse=True
        )
    return ordered_list


# //// -a ////

def calculate_average(list_dict):
    """Calculate the average of all the students marks.

    input:
        list_dict (list): A list of dictionaries containing student data.

    output (float): The average mark of all the students.
    """
    marks = []
    for student in list_dict:
        marks.append(student["mark"])

    try:
        average = sum(marks) / len(marks)

    except ZeroDivisionError:
        average = 0
        print("Not enough marks provided to do the average")
    return average


# //// -p ////

def calculate_students_above_threshold(list_dict, threshold_grade):
    """Return students with a mark higher or equal to the number provided.

    input:
        list_dict (list): A list of dictionaries containing student data.

    output (list): A list of dictionaries containing the information.
    """
    higher = []
    for students in list_dict:
        if students["mark"] >= threshold_grade:
            higher.append(students)
    return higher


# //// -s ////

def find_student(pattern, list_dict):
    """Find whether the student is or not in the dictionary.

    input:
        pattern (str): The name or pattern of the student to search for.
        list_dict (list): A list of dictionaries containing student data.

    output (list): The data associated with the student.
    """
    name_list = []
    if len(pattern) < 3:
        raise ValueError(
            "You must provide at least 3 characters to find a student."
            )

    for students in list_dict:
        if pattern.lower() in students["name"].lower():
            name_list.append(students)

    if not name_list:
        raise StudentNotFoundError(
            f" A student with {pattern} was not found."
            )
    return name_list


# //// -o ////

def student_above_average(list_dict):
    """Show the students and their information if they are above the average.

    input:
        list_dict (list): A list of dictionaries containing student data.

    output (list): A list containing all the students above the average mark.
    """
    average = calculate_average(list_dict)
    students_above = []
    for student in sort_dict(list_dict):
        if student["mark"] >= average:
            students_above.append(student)

    return students_above


# //// -d ////

def delete_student(list_dict, pattern):
    """Delete an existing student by searching with a given pattern.

    input:
        list_dict (list): A list of dictionaries containing student data.
        pattern (str): The pattern (or full name) to match.

    output (list): The new list without the deleted students.
    """
    new_list = []
    beginning_length = len(list_dict)

    if len(pattern) < 3:
        raise ValueError(
            "You must provide at least 3 characters to delete a student."
            )

    for student in list_dict:
        if pattern.lower() not in student["name"].lower():
            new_list.append(student)

    if beginning_length == len(new_list):
        raise StudentNotFoundError(
            f"No student matches {pattern}, please provide a valid student. "
            )

    students_deleted = beginning_length - len(new_list)
    print(f"The number of students deleted is: {students_deleted}.")

    return new_list


# //// -r ////

def import_students(filename, list_dict):
    """Read student records from a file and stores them.

    input:
        filename (str): The name or path of the file to read.
        list_dict (list): A list of dictionaries where students will be stored.
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                delete_space = line.strip()
                if not delete_space:
                    continue

                lists = delete_space.split(",")

                if len(lists) < 4:
                    print(f"The student {lists[0]} needs more parameters...")
                    continue

                student_name = lists[0].strip()
                email = lists[2].strip().lower()
                phone = lists[3].strip()

                try:
                    mark = float(lists[1].strip())
                    check_mark(mark)

                    found = False

                    for student_in_list in list_dict:
                        if (student_in_list["name"].lower()
                                == student_name.lower()):

                            if (student_in_list["email"] == email and
                                    student_in_list["phone"] == phone):
                                found = True
                                raise DuplicateStudentError(
                                    "Student exists with same data"
                                    )

                            elif (student_in_list["email"] == email
                                  or student_in_list["phone"] == phone):
                                found = True
                                student_in_list["mark"] = mark
                                student_in_list["email"] = email
                                student_in_list["phone"] = phone
                                student_in_list["extra"] = lists[4:]
                                break

                    if not found:
                        student = {
                            "name": student_name,
                            "mark": mark,
                            "email": email,
                            "phone": phone,
                            "extra": lists[4:],
                        }
                        list_dict.append(student)

                except (ValueError, InvalidMarkError):
                    print(
                        f"The second parameter after {student_name}\
                              is not a valid number"
                        )
                except DuplicateStudentError:
                    print(
                        f"The student {student_name}\
                              already exist and the data is the same"
                        )
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
