"""Module to process student data via command line arguments."""

import jlv_library as lib
from sys import argv


# //// PROCESSING DATA ////

open_file = lib.open_lib()
students = lib.load_binary(open_file)

if len(argv) == 1:
    print("You must provide some arguments.")
    print("Type -help to see the available commands.")

elif argv[1] == "-help":
    print("-r : You must use it if it's your first time loading students.\
           It import and organise the students. Syntax: <-r> <filename>")
    print("-m : It shows the students sorted by mark. Syntax: <-m>")
    print("-s : It shows the students that contain the pattern provided.\
           Syntax: <-s> <pattern> ")
    print("-d : It deletes the students that contain the pattern provided.\
           Syntax: <-d> <pattern> ")
    print("-o : It shows the students above the average mark. Syntax: <-o>")
    print("-a : It shows the average mark. Syntax: <-a>")
    print("-m : It shows the students above the provided threshold grade.\
           Syntax: <-p> <threshold grade>")

else:
    if argv[1] == "-r":
        print(f"Selecting option: {argv[1]}.")

        if len(argv) < 3:
            print("Please provide a parameter after the command:\
                   < -r >< file >")

        else:
            try:
                filename_to_import = argv[2]
                lib.import_students(filename_to_import, students)
                lib.save_binary(open_file, students)
                print(
                    f"The database has been updated with\
                        data from '{filename_to_import}'."
                    )
            except FileNotFoundError:
                print(f"The file {argv[2]} does not exists.")

    elif argv[1] == "-m":
        print(f"Selecting option: {argv[1]}.")
        sorted_students = lib.sort_dict(students)

        print("These are the students sorted by mark: ")
        for student in sorted_students:
            # We use this loop to share the students in a "prettier" way.
            print(f" {student['name']}: {student['mark']},\
                {student['email']}, {student['phone']}.")

    elif argv[1] == "-s":
        print(f"Selecting option: {argv[1]}.")

        if len(argv) < 3:
            print("You must provide a value after the command:\
                < -s >< pattern/name >")

        else:
            try:
                search_student = lib.find_student(argv[2], students)

                for student in search_student:
                    print(f"Students with {argv[2]}: {student['name']}:\
                           {student['mark']}, {student['email']},\
                                {student['phone']}.")

            except lib.StudentNotFoundError:
                print("A student with the pattern you\
                    have provided has not been found.")
            except ValueError:
                print("Please provide at least 3 characters\
                    to find the student.")

    elif argv[1] == "-d":
        print(f"Selecting option: {argv[1]}.")

        if len(argv) < 3:
            print("You must provide a value after the command:\
                < -d >< pattern/name >")

        else:
            try:
                new_list = lib.delete_student(students, argv[2])
                students = new_list
                lib.save_binary(open_file, new_list)

            except lib.StudentNotFoundError:
                print("A student with the pattern you\
                    have provided has not been found.")
            except ValueError:
                print("Please provide at least 3\
                    characters to find the student.")

    elif argv[1] == "-o":
        print(f"Selecting option: {argv[1]}.")
        students_above = lib.student_above_average(students)

        print("These are the students above the average: ")
        for student in students_above:
            print(f" {student['name']}: {student['mark']},\
                {student['email']}, {student['phone']}. \n")

    elif argv[1] == "-a":
        print(f"Selecting option: {argv[1]}.")
        print(f"This is the average of the students:\
            {lib.calculate_average(students)}")

    elif argv[1] == "-p":
        print(f"Selecting option: {argv[1]}.")

        if len(argv) < 3:
            print("You must provide a value after the command:\
                < -p > < threshold_grade >")

        else:
            try:
                threshold = float(argv[2])
                lib.check_mark(threshold)
                student_above_threshold =\
                    lib.calculate_students_above_threshold(students, threshold)

                for student in student_above_threshold:
                    print(f" {student['name']}: {student['mark']},\
                        {student['email']}, {student['phone']}.")

            except ValueError:
                print("The parameter must be a number.")
            except lib.InvalidMarkError:
                print("The mark must be a nunmber between 1 and 10.")
