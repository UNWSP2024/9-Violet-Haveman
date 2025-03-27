# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random
def rand_number_file_writer():
    file1 = open("numbers.txt", "w")
    numbers = int(input("How many numbers would you like the file to hold? (0-1000): "))
    if numbers <= -1:
        print("Input must be between 0 and 1000")
        return rand_number_file_writer()
    if numbers >= 1001:
        print("Input must be between 0 and 1000")
        return rand_number_file_writer()
    else:
        while numbers != 0:
            randoms = str(random.randint(1, 500))
            file1.write(randoms + "\n")
            numbers -= 1
    file1.close()
    file2 = open("numbers.txt", "r")
    print("Numbers Generated: ")
    print(file2.read())
    file2.close()


rand_number_file_writer()
