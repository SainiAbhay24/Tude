'''
Task 1: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''

file = open("sample.txt", "r")
try :
    for line in file:
        print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
finally:
    file.close()

'''
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''

user = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user + "\n")
additional_data = input("Enter some additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")
with open("output.txt", "r") as file:
    content = file.read()
    print("Final content of the file:")
    print(content)
