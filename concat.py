# Add a word of choice to every word in a text file
# Author: Mavis Coffey

file_to_concat = input("Enter a filename to concatenate. (Make sure you are in the directory of the desired file.) ")
word_to_add = input("Enter a word to concatenate to every word in the list ")
iterations = 0
looking_for = str(file_to_concat)




'''Errors that can be raised'''

class error(Exception):
    pass

# Error for missing '.txt' in string
class missing_string(error):
    pass

# Error for missing '.txt' at the end of string
class enderror(error):
    pass




'''Check for errors'''

# Make sure the input has '.txt'
try:
    
    if looking_for.find(".txt") == -1:
        raise missing_string
    
except missing_string:
    print("\nError: Input files must be text files!")
    exit()


# Make sure the input has '.txt' at the end, ensuring a text file
try:

    if (len(looking_for) - 4) != looking_for.find(".txt"): 
        raise enderror
    
except enderror:
     print("\nError: '.txt' must be at the end")
     exit()


# After all the above is true, read the text file
# Note to self: make more compact and less counter-intuitive
     
file = open(str(file_to_concat), "r")
editor = []
times = 0
buffer = -1
editor = file.readlines()
length = len(editor)
print(length)
edit = []

placeholder = open(str(file_to_concat), 'r').readlines()


    
# Create a new file to store the concatenated word list

new_file = open('python_append.txt', 'x')

# While iterations are less than the amount of lines in the input file, append input word and add to new file

while iterations < length:


    times = times + 1
    buffer = buffer + 1
    edit = placeholder[buffer:times]
    edited = str(edit)[2:len(edit)-5]
    
    
    
    print(times, buffer)
    
    
    
    new = edited + word_to_add + '\n'
    
    
    
    print(edited + word_to_add + "\n")
    
    
    
    new_file.writelines([str(new)])

    

    
    
    iterations = iterations + 1
    print("\niterations", iterations)
    
    

    



