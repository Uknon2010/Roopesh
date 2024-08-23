from statistics import mean

import pandas as pd

myclass = {
    "Name": ["Rishabh", "Sanjana Nayak", "Shaina Michael", "Monali", "Chaitanya", "Anish",
             "Nandey", "Rishabh", "Adarsh", "Simran", "Anish", "Siddharth", "Atheendra", "Aayushi"],
    "Age": [22, 24, 23, 25, 27, 26, 22, 24, 25, 23, 26, 27, 28, 24],
    "GPA": [3.8, 3.9, 3.7, 3.5, 3.6, 3.8, 3.4, 3.9, 3.2, 3.7, 3.5, 3.6, 3.9, 3.8],
    "Major": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering",
              "Computer Science", "Data Science", "Computer Science", "Data Science",
              "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
              "Mechanical Engineering", "Computer Science", "Data Science"]
}


data_frame = pd.DataFrame(myclass)
print(data_frame)

print("Looping over columns")
for column in data_frame.columns:
    print(f"column = {column}")
    print(f"column values = {data_frame[column]}")

print("_"*100)
print("Looping over rows")
for index, row in data_frame.iterrows():
    print(f"Student Number = {index + 1}")
    print(f"Name = {row['Name']}\n Age = {row['Age']}\n GPA = {row['GPA']}; Major = {row['Major']}")


# Let is get the minimum and maximum and mean and mode and median Age
print("_"*100)
print("Age Variance")
print(f"Minimum Age of Student = {min(data_frame['Age'])}")
print(f"Maximum Age of Student = {max(data_frame['Age'])}")
print(f"Mode of Age of Student = {data_frame['Age'].mode()[0]}")
print(f"Mean of Age of Student = {data_frame['Age'].median()}")
print(f"Median of Age of Student = {data_frame['Age'].mean()}")




#Let is get the minimum and maximum and mean and mode and median gpa

print("_"*100)
print("GPA Variance")
print(f"Minimum GPA of Student = {min(data_frame['GPA'])}")
print(f"Maximum GPA of Student = {max(data_frame['GPA'])}")
print(f"Mode of GPA of Student = {data_frame['GPA'].mode()[0]}")
print(f"Mean of GPA of Student = {data_frame['GPA'].mean()}")
print(f"Median of GPA of Student = {data_frame['GPA'].median()}")
