# text_storage.py

FILENAME = "students.txt"

def load_students():
    """Load students from the text file."""
    students = []
    try:
        file = open(FILENAME, "r")
        for line in file:
            line = line.strip()
            if line != "":
                ID, name, age, marks = line.split(",")
                student = {"ID": ID, "name": name, "age": age, "marks": marks}
                students.append(student)
        file.close()
    except FileNotFoundError:
        # File doesn't exist yet, return empty list
        return []
    return students


def save_students(students):
    """Save students to the text file."""
    file = open(FILENAME, "w")
    for student in students:
        line = student["ID"] + "," + student["name"] + "," + student["age"] + "," + student["marks"] + "\n"
        file.write(line)
    file.close()

