'''
ADVENT OF CODE: Day 1 - Part 2 - December 01, 2021
FILE: 1_2021_B.py
INPUT: 1_2021_B.txt
LIBRARIES IMPORTED: NONE
NOTE:
    1. The input file is not in the same directory as this file.
'''

'''
Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); 
their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. 
The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. 
So, compare A with B, then compare B with C, then C with D, and so on. 
Stop when there aren't enough measurements left to create a new three-measurement sum.
'''

INPUT_FILE = 'Day_1/pt_2/1_2021_B.txt'

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

# get_sums function will get the sum of the first n numbers in the list. Once the sum is calculated, it will be added to a list of sums.
# Keep calculating n amount of sums until there arent enough measurements left to calculate n amount of sums.
def get_sums(input_data, n):
    # We don't use the sum list because we only need the count. It is only added for testing purposes.
    sums = []
    sum = 0
    count = 0
    for i in range(0, len(input_data)):
        sum += input_data[i]
        if i + 1 >= n:
            sums.append(sum)
            sum = 0
        # How many sums are larger than the previous sum
        if i + 1 >= n and input_data[i] > input_data[i - n]:
            count += 1
    return sums, count

if __name__ == '__main__':
    input_data = open_file(INPUT_FILE)
    all_sums, count = get_sums(input_data, 3)
    print(count)

