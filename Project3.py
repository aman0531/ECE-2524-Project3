# ECE 2524 Project 3
# The following script file is responsible for reading a given "scan" text file (file_name). Then, the given file is rewritten without any punctuations
# into a file (input_file_name) whose name is chosen by the user. This file is responsible for doing the inner workings of the program as seen 
# within the code. Using this information, a total word count of the words within the scan file are outputted. Next, the user is asked if they want to
# search the file (input_file_name) for a specific word. If the user enters 1, they are asked to enter the specific word (file_word) and all of its 
# occurrences along with the line number are generated. Then the user is asked if they want to replace every instance of a new word (new_word) of choice.
# If the user enters 1, the user has the ability to file_word into new_word. This change is saved into an output file within the current
# working directory. The output file has a name choosen by the user and it shows the list of all of the words, words that were replaced, and
# the punctuation changes unlike the file stored in input_file_name which only shows the punctuation changes. Note that 
# the user can only change 1 word at a time becuase the changes are saved to an alternate output file. This is intential becuase the programmer 
# wants the user to be careful with the changes they make. So in order to change another word, the user needs to start the program again and use the specfic
# output file name provided in the previous run as the file for "scanning" if they want to continue making changes to the same file. If the user is satisfied
# with the changes the user can rerun the program and chose another file to scan.


# Used to replace any punctuations from input file with blank spaces

import string

print("Welcome to the find and replace Python program!")

file_name = input("Enter a non-empty file name that you would like to scan: ")

# Responsible for reading the scan file provided

with open(file_name) as f:
	r = f.read()

# Responsible for creating the file without punctuations

input_file_name = input("What would you like to call the file used within the program? ")

with open(input_file_name, 'w') as f:
	for punctuation in r: 
        	if punctuation in string.punctuation:
            		r = r.replace(punctuation, "")
	f.write(r)

# Resonsible for creating a list called total_words which contains all of the words within the text file, 
# generating a numeric value for the total words and outputting the result 

total_words = r.split()
total_word_count = len(total_words)
print("There are", total_word_count, "words in the file", file_name)

# Main code of the program. 

# This loop will always be true. so break statements used to end loop. 
# The loop is responsible for asking the user to search a specfic word. The variable l_count is resposible for counting the number of lines within the 
# updated input file. If the user responds with a 1 when asked to search a specfic word, then the user is tasked with inputting a word that is within the 
# updated input file. Once the user provides a word, the updated input files is opened. Next, a for loop is used to read all of the lines within the input 
# file. With this information, the specfic word provided is checked within the lines list (lines_split()). If the word is found, an output containing the 
# word and line number for each occurenece of the word are generated. The line counter is incremented by 1 each iteration. In addition, error checking 
# is done to ensure that the user provides a word that is within the text. The user is then asked if they want to replace the word they chose (file_word)
# to a different word. If the user enters 1 then file_word is replaced by new_word (using replace()) which is the user-inputted word used to change
# file_word. This change is saved in a txt file with the name set by the user. Note only one word can be changed at a for every program ran. Additional, error checking done to ensure
# that the user properly inputs either 1 or 2.

while (0 == 0):
	print("Would you like to search for a specific word within", file_name) 
	search_question = input("Enter 1 for YES! and 2 for NO!: ")
	search_answer = int(search_question)	
	l_count = 1

	if search_answer == 1:
		file_word = input("Enter the word you want to search within this file: ")
		if file_word in total_words:	 
			with open(input_file_name) as f1:
				for lines in f1.readlines():
					if file_word in lines.split():	
						print("The word", file_word, "was found on Line Number", l_count, "(", lines, ")")
					l_count += 1
		
			print("Would you like to replace the word", file_word, "with another word?")
			replace_question = input("Enter 1 for YES! and 2 for NO!: ")
			replace_answer = int(replace_question)

			if replace_answer == 1:			
				new_word = input("Enter the new word: ")
				output_file_name = input("What would you like to call the output file? ")
				with open(output_file_name, 'w') as f2:
					replace = r.replace(file_word, new_word)
					f2.write(replace)
					print("Thank you for using the program")
					print("To replace another word within the same file. Rerun the program with the scan file as", output_file_name)
					print("To scan another file, simply rerun the program")
					break

			elif replace_answer == 2:
				print("Thank you for using the program. Goodbye!")
				break

			else:
				print("Input Error. Please check if an 1 or 2 were typed")

		else:
			print("Check input. The word", file_word, "does not exist in the file.")								
	
	elif search_answer == 2:
		print("Thank you for using the program. Goodbye!")
		break

	else:
		print("Input Error. Please check if an 1 or 2 were typed")