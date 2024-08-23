# from distutils.command.install import value

student = {
    "name": "Rahul",
    "age": 25,
    "courses": ["Math", "Computer Science"],
    "graduated": True
}

print(f"student = {student}")

# Print the different parts of the dictionaries
print(f"student = {student['name']}")
print(f"age of student = {student['age']}")
print(f"what courses do student have = {student['courses']}")
print(f" did student graduate = {student['graduated']}")

# Add GPA
student['gpa'] = 9.1
print(f"student = {student}")

# Looping over dictionaries : Method 1
print("Method 1")
for key in student:
    print(f"key = {key}, value = {student[key]}")


print("_"*100)
# Looping over dictionaries : Method 2
print("Method 2")
for key in student.keys():
    print(f"{key} = {key}, value = {student[key]}")

print("_"*100)
# Looping over dictionaries : Method 3
print("Method 3")
for key, value in student.items():
    print(f"key = {key}, value = {value}")

# Nested dictionaries
# dictionaries can contain other dictionaries, allowing for complex data structures.
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Atheendra", "age": 24, "GPA": 9},
}


print("Student 1 Details:")
print(f"name = {students_dictionary['student1']['name']}")
print(f"age = {students_dictionary['student1']['age']}")
print(f"gpa = {students_dictionary['student1']['GPA']}")


print("Student 2 Details:")
print(f"name = {students_dictionary['student2']['name']}")
print(f"age = {students_dictionary['student2']['age']}")
print(f"gpa = {students_dictionary['student2']['GPA']}")

print("_"*100)
print("Method 2")
for student in students_dictionary:
    print(f"name = {students_dictionary[student]['name']}")
    print(f"age = {students_dictionary[student]['age']}")
    print(f"gpa = {students_dictionary[student]['GPA']}")


# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]
print("_"*100)
print("Method 1")
print("_"*100)
for student in students_list:
    print(f"name = {student['name']}")
    print(f"age = {student['age']}")
    print(f"gpa = {student['GPA']}")


print("_"*100)
print("Method 2")
print("_"*100)
for i in range(len(students_list)):
    print(f"name = {students_list[i]['name']}")
    print(f"age = {students_list[i]['age']}")
    print(f"gpa = {students_list[i]['GPA']}")

print("_"*100)
print("Method 3")
print("_"*100)
for index, student in enumerate(students_list):
    print(f"name of student number {index + 1}= {students_list[index]['name']}. Also equal to {student['name']}")
    print(f"age of the student number {index + 1} = {students_list[index]['age']}. Also equal to {student['GPA']}")
    print(f"gpa of the student number {index + 1} = {students_list[index]['GPA']}. Also equal to {student['GPA']}")