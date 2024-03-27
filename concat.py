# Add a word of choice to every word in a text file
# Author: Mavis Coffey

file_to_concat = input("Enter a filename to concatenate. (Make sure you are in the directory of the desired file.) ")
file_input = input("Enter a filename to concatenate to every word in the list ")
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
    
    if looking_for.find(".txt") == -1 or file_input.find(".txt") == -1:
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
input_file = open(str(file_input), "r")
editor = []
secondary_iterations = 0
times = 0
buffer = -1
editor = file.readlines()
input_editor = input_file.readlines()
length = 0
print('editor', editor)
edit = []
input_times = 2

placeholder = open(str(file_to_concat), 'r').readlines()
input_placeholder = open(str(file_input), 'r').readlines()


if len(editor) > len(input_editor):
        length = len(editor)
elif len(editor) < len(input_editor):
        length = len(input_editor)
elif len(editor) == len(input_editor):
        length = len(editor)



print('input placeholder', input_placeholder)
    
# Create a new file to store the concatenated word list

new_file = open('append.txt', 'x')
word_length_one = 0
word_length_two = 1



# While iterations are less than the amount of lines in the input file, append input word and add to new file
while secondary_iterations < length:
    
    times = 0
    buffer = -1
    
    if len(editor) > len(input_editor):
        length = len(editor)
    elif len(editor) < len(input_editor):
        length = len(input_editor)
    elif len(editor) == len(input_editor):
        length = len(editor)

    while iterations < length:


        times = times + 1
        buffer = buffer + 1

        edit = placeholder[buffer:times]
        input_edit = str(input_placeholder[word_length_one:word_length_two])

        word_one = str(input_edit)[2:len(input_edit)-4]
        print('word one: ', word_one)
        print('word one length: ', input_edit)
        

        
        input_edited = str(input_edit)[2:len(input_edit)-4]
        edited = str(edit)[2:len(edit)-5]
    
        print('edited', edited)
        print('edited', input_edited)
    
        print(times, buffer)
    
    
    
        new = edited + word_one + '\n'
    
        print('first file:', edited, '\n')
    
        print('output:', edited + word_one + "\n")
    
    
    
        new_file.writelines([str(new)])

    
        
    
    
        iterations = iterations + 1
        print("\niterations", iterations)
        input_times = input_times + 1
        
        
    
    iterations = 0
    word_length_one = word_length_one + 1
    word_length_two = word_length_two + 1
    secondary_iterations = secondary_iterations + 1