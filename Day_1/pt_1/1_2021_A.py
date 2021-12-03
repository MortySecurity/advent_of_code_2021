'''
ADVENT OF CODE: Day 1 - Part 1 - December 01, 2021
FILE: 1_2021_A.py
INPUT: 1_2021_A.txt
LIBRARIES IMPORTED: NONE
NOTE:
    1. The input file is not in the same directory as this file.
'''


'''
The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - 
you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. 
(There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
'''

INPUT_FILE = 'Day_1/pt_1/1_2021_A.txt'

# open_file function will open a file, and parse the data into a list of integers.
def open_file(file_name):
    input_data = []
    try:
        file = open(file_name, 'r')
        data = file.read()
        file.close()
        # Every new line is an integer.
        input_data = [int(x) for x in data.split('\n')]
    except FileNotFoundError:
        print('File not found.')
        exit()
    except PermissionError:
        print('Permission denied.')
        exit()
    except:
        print('An unknown error occurred.')
        exit()
    return input_data

# count_increases function will return the number of times a depth measurement increases from the previous measurement.
def count_increases(input_data):
    count = 0
    for i in range(1, len(input_data)):
        if input_data[i] > input_data[i - 1]:
            count += 1
    return count

if __name__ == '__main__':
    input_data = open_file(INPUT_FILE)
    print(count_increases(input_data))
