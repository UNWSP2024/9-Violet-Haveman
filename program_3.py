# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    ######################
    with open("numbers.txt", "r") as file1:
        lines = file1.readlines()

    number_list = []

    for line in lines:
        numbers = line.rstrip('\n').split(',')
        number_list.extend(numbers)

    number_list = [int(num) for num in number_list]

    total = sum(number_list)

    print(f"Sum of numbers: {total}")

    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()