# File: Project3.py
# The following file is resposnible for error checking file input, 
# read contents of the file, use built in split function to eliminate
# white spaces within the text file, and use length function to get 
# the total number of words within the text file given.

print("Welcome to the find and replace Phyton program!")

file_name = input("Enter a file name that you would like to scan: ")

with open(file_name) as f:
		r = f.read()
		total_words = r.split()
		total_word_count = len(total_words)

print("Total number of words within the text file provided: ", total_word_count)

input = input("Would you like to search for a specific word within this file? Enter 1 for YES and 2 for NO: ")




