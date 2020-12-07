# ECE 2524 Project 3
# The following script file is responsible for reading a given text file. Then, the given file is rewritten without any punctuations. 
# With the updated input file, a total word count of the words within the file are outputted. Next, the user is asked if they want to
# search the updated input file for a specific word. If the user enters 1, they are asked to enter the specific word and all of its occurrences
# along with the line number are generated. Then the user is asked if they want to replace every instance of the word they chose.
# If the user enters 1, the user has the ability to change the word into a new word. This change is saved into an output file within their current
# working directory called output.txt


# Used to replace any punctuations from input file with blank spaces

import string

print("Welcome to the find and replace Phyton program!")

file_name = input("Enter a file name that you would like to scan: ")

# Responsible for reading the file provided

with open(file_name) as f:
	r = f.read()

# Responsible for updating the input file with ni punctuations

with open(file_name, 'w') as f:
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
# is done to ensure that the user provides a word that is within the text. 

while (0 == 0):
	
	search_question = input("Would you like to search for a specific word within this file? Enter 1 for YES! and 2 for NO!: ")
	search_answer = int(search_question)	
	l_count = 1

	if search_answer == 1:
		file_word = input("Enter the word you want to search within this file: ")
		if file_word in total_words:	 
			with open(file_name) as f1:
				for lines in f1.readlines():
					if file_word in lines.split():	
						print("The word", file_word, "was found on Line Number", l_count, "(", lines, ")")
					l_count += 1

		else:
			print("Check input. The word", file_word, "does not exist in the file.")								
	
	elif search_answer == 2:
		print("Thank you for using the program. Goodbye!")
		break

	else:
		print("Input Error. Please check if an 1 or 2 were typed")
		


	





