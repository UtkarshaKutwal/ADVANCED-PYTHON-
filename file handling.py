# Program to create and write data into a text file

file = open("sample.txt", "w")

file.write("Hello, World!\n")
file.write("Welcome to Python File Handling.\n")
file.write("This is a sample text file.")

file.close()

print("Data has been written to sample.txt successfully.")
