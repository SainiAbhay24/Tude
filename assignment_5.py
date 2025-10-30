'''
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student's name is not found, display an appropriate message.

'''
student = {
    "Aarav": 85,
    "Alia": 92,
    "Charlie": 78,
    "David": 90
}

name = input("Enter the Student name: ")
if name in student:
    print(f"{name} marks are: {student[name]}")
else :
    print("Student not found.")

'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

number = [1,2,3,4,5,6,7,8,9,10]
Extracts = number[:5]
Reversed = Extracts[::-1]
print(f"Original List: {number}")
print(f"Extracted List: {Extracts}")
print(f"Reversed List: {Reversed}")