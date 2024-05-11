# open a file
file = open("Downloads/file.txt.txt", "r")

# read a file
print(file.read()) # prints the contents of a file

# always close a file
file.close()

# another way to read a file
with open("Downloads/file.txt.txt", "r") as file:
    print(file.read())  # prints the contents of a file

# read all lines in a file
with open("Downloads/file.txt.txt", "r") as file:
    print(file.readlines())  # prints the contents of a file and puts '\n' for all blank lines

# read a single line in a file, put it in a variable, print it in a list
with open("Downloads/file.txt.txt", "r") as file:
    line1 = file.readlines()[0]
    print([line1])  # will also print the '\n' in the list for example: ['hello world!\n']

# read a single line in a file and take off the '/n'
with open("Downloads/file.txt.txt", "r") as file:
    line1 = file.readlines()[0]
    print([line1.strip()]) # will exclude the '\n' and white spaces from the beginning and end of line but not in the middle

# get rid of all '\n' even if they are in the middle of a line
with open("Downloads/file.txt.txt", "r") as file:
    line1 = file.readlines()[0]
    line1 = line1.replace("\n", "")
    print([line1])

# write a new file (be careful because this can erase an existing file)
with open("Downloads/file2.txt", "w") as file:
    file.write("hello world this is a new file!")

with open("Downloads/file2.txt", "r") as file:
    print(file.read())

# append to an already existing file
with open("Downloads/file2.txt", "a") as file:
    file.write("hello again") # this writes to the same line as the last line in the file
    file.write("\nHello") # this writes to the next line

with open("Downloads/file2.txt", "r") as file:
    print(file.read())

# open a file for reading and writing
with open("Downloads/file2.txt", "r+") as file:
    file.write("\ntest") # this will over write the beginning of an existing file

with open("Downloads/file2.txt", "r") as file:
    print(file.read())

'''
# put just the number 5 in the file then use it in r+ mode
with open("Downloads/file2.txt", "r+") as file:
    score = file.read()
    new_score = int(score) + 1
    file.seek(0) # put pointer at beginning of file
    file.write(str(new_score)) # overwrite the number 5 with a new score
'''

# read just the first 3 lines in a file
with open("Downloads/file2.txt", "r+") as file:
    for i, line in enumerate(file):
        print(line, end="")
        if i == 2:
            break

# read a certain number of characters
with open("Downloads/file2.txt", "r+") as file:
    print(file.read(7)) # this will also print the '\n'

'''
Open a file named "programmingExpert.txt" that is located in the data directory and print how many words are present in the file.

Escape characters like \n and \t, periods, commas, and dashes(-) are not considered words. You may assume that all other text in 
the file that is separated by a space is a word
'''

text = ""

with open("data/programmingExpert.txt", "r") as file:
    text = file.read()

escape_characters_removed = text.replace("\n", " ")
punctuation_removed = escape_characters_removed.replace(",", "").replace("-", "").replace(".", "")

words = punctuation_removed.split(" ")
empty_strings = words.count("")
number_of_words = len(words) - empty_strings

print(number_of_words)

'''
Within the current directory, create a new file named "programmingExpert.txt" that contains the 
squares of numbers in the range 1 to 50, each on a new line.
'''
with open("Downloads/file2.txt", "w") as file:
    for i in range(1, 51):
        file.write(str(i * i) + "\n")