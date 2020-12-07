# ECE-2524-Project3
The following document provides a description on what the project is, how it should be ran, and the slight changes made from Project 3-1 assignment. Note that the changes made
were due to format issues.

Project 3 create a phyton script file that is responsible for mimicking the following Unix VI Editor commands: ?, /, :s/old_word/new_word/g with minor changes. The 
Project3.py file takes a non-empty text file and scans it. After "scanning" the file, the total amount of words within a given file are outputted to the terminal. 
Next, the user has to abilily to search a specfic word within that which is similar to the commands shown above. After a word (note the word is case sensitive) has been choosen by the user, a custom message is displayed which shows the occurence and line number of the word within the text file. The user then has the ability to change the searched word
into a new word of their choice. This change along with the punctuation changes made to the scan file are save to an output file with the name of their choice. This is the biggest change made form Project 3-1 assignemt becuase the programmmer wanted the user to be careful with the changes they made

How to run the project:
Make sure is in the working directory where the Test Files are saved on the computer. Open the command prompt, and change to the directory using cd and then followed by the filepath. Then run the script file using py Project3.py. Then carefully follow the messages provided within by the script. Note that 
the user can only change 1 word at a time becuase the changes are saved to an alternate output file. This is intential becuase the programmer 
wants the user to be careful with the changes they make. So in order to change another word, the user needs to start the script again and use the specfic
output file name provided in the previous run as the file for "scanning" if they want to continue making changes to the same file. If the user is satisfied
with the changes the user can rerun the script and chose another file to scan. 

This is evident in output1.txt becuase the script file was ran twice to make the changes of "for" to "FOR" and "aman" to "john"

More details are provided within the comments of Project3.py file
