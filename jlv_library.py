from os import path

# //// EXCEPTIONS ////

class StudentNotFoundError(Exception):
    """ Used when a student is not found in the dictionary """
    pass

class InvalidMarkError(Exception):
    """ Used when mark is not between 0 and 10 """
    pass

class DuplicateStudentError(Exception):
    """ Used when student id already registered """
    pass

# //// VALIDATION ////

def find_student(student,student_dic):
    """ It finds out whether the student is or not in the dictionary.
    If the student is not found it raises an error, otherwise it will
    give us the information about that student.
    
    input: 
        student (str): The full name of the student to search for.
        student_dic (dict): The dictionary containing all students.

    output: The data associated with the student
    """

    if student not in student_dic:
        raise StudentNotFoundError(f"The student {student} is not found.")
    return student_dic[student]

def check_mark(mark):
    """ Validates if a grade is within the allowed range (0 - 10).
    
    input: 
        mark (float): The numeric grade to validate.
    """

    if mark < 0 or mark > 10 :
        raise InvalidMarkError(f"The mark provided {mark} is out of range.")
    
def duplicated_student(student,student_dic):
    """ Checks if a student already exists in the records to avoid overwritting.
    
    input: 
        student (str): The name of the student.
        student_dic (dict): The dictionary containing all students.
    """

    if student in student_dic:
        raise DuplicateStudentError(f"The student {student} already exists.")
    
# //// CONFIGURATION ////

def open_lib():
    """ This is used to know whether the file and the content are created or not.
    We have to use the format "file = <filename>".
    Always that the name dont exist we use the default one (bin_file) to avoid errors.

    output (str): The name of the file where student data is stored.
    """

    main_file ="students.cfg"
    bin_file ="students.dat"
    text_to_read = ""

    if not path.exists(main_file):
        with open(main_file,"w") as settings:
            settings.write(f"file={bin_file}")
        return bin_file
    
    with open(main_file,"r") as settings:
        text_to_read = settings.read().strip()
        if text_to_read == "" or "file=" not in text_to_read:
            return bin_file
        
        divide = text_to_read.split("=") # We need to separate the name and "file=", so we split in the "=".
        if  not divide[1].strip(): #!!!!!!!!!!!!!!!!!!!! REVISAR ESO PORQUE SI NO ES ESPACIO EN BLANCO Y ES ALGO RARO QUE !!!!!!!!!!!!!!!!!!!
            return bin_file
        
        part_we_need = divide[1].strip()
        filename = part_we_need.split()[0] # To avoid getting useless text, we split and get just the name.
        return filename

def import_students(filename,dictionary):
    """ Reads student records from a file and stores them in a dictionary.
    Each line in the file is expected to be semicolon-separated. The function
    converts the mark to a float and validates it using check_mark() before 
    adding the student to the dictionary.

    input:
        filename (str): The name or path of the file to read.
        dictionary (dict): The dictionary where students will be stored.
    """

    with open(filename,"r") as file:
        for line in file:
            delete_space = line.strip()
            lists = delete_space.split(";")
            #Store them in variables because its crucial to clean their format.
            student_name = lists[0].strip()
            mark = lists[1].strip() 

            try:
                validated_mark = float(mark)
                if check_mark(validated_mark): # Validate whether the mark is in range(0-10) or not.
                    dictionary[student_name] = [validated_mark] + lists[2:] #!!!!!!!!!!!!!!!!!!!!!!!!!!PODEMOS LIMPIAR LOS ESPACIOS SI LOS HUBIERA!!!!!!!!!!!!!!!!!!!!!
            except ValueError:
                print(f"The second parameter after the name {student_name} is not a valid number, please check it")
