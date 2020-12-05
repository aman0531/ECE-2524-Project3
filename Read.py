# File: Read.py
# The following file is resposnible for checking if reading a file works.

file_name = input("Enter a file name: ")
with open(file_name) as f:
	r = f.read()

print(r)

