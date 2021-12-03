'''
ADVENT OF CODE: Day 2 - Part 2 - December 02, 2021
FILE: 2_2021_B.py
INPUT: 2_2021_B.txt
LIBRARIES IMPORTED: NONE
NOTE:
    1. The input file is not in the same directory as this file.
'''

INPUT_FILE = 'Day_2/pt_2/2_2021_B.txt'

# open_file function will open a file, and parse the data into a list of integers.
def open_file(file_name):
    input_data = []
    try:
        file = open(file_name, 'r')
        data = file.read()
        data = data.split('\n')
        file.close()
        # Every new line is an integer.

    except FileNotFoundError:
        print('File not found.')
        exit()
    except PermissionError:
        print('Permission denied.')
        exit()
    except:
        print('An unknown error occurred.')
        exit()
    return data

'''
This function will parse the commands:
    1. forward(n)
    2. up(n)
    3. down(n)
    4. aim(n)

    The function will return the new position of the submarine. The HORIZONTAL, DEPTH, and AIM will all start at 0. 

    down x -> increasesyour AIM by x, resulting in a new AIM of x.
    up x -> decreases your AIM by x, resulting in a new AIM of x.
    forward x -> does two things:
        1. Adds x to the HORIZONTAL position a total of x.
        2. Increases your DEPTH by AIM * x, resulting in a new DEPTH of AIM * x.
'''
def parse_commands(commands):
    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        command = command.split()
        if command[0] == 'forward':
            horizontal += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
        elif command[0] == 'aim':
            aim = int(command[1])
    return horizontal, depth, aim

if __name__ == '__main__':
    data = open_file(INPUT_FILE)
    horizontal, depth, aim = parse_commands(data)
    total_distance = horizontal * depth
    print(f'The submarine is at position {horizontal} and depth {depth}.')
    print(f'The total distance is {total_distance}.')





