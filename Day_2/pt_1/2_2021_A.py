'''
ADVENT OF CODE: Day 2 - Part 1 - December 02, 2021
FILE: 2_2021_A.py
INPUT: 2_2021_A.txt
LIBRARIES IMPORTED: NONE
NOTE:
    1. The input file is not in the same directory as this file.
'''

INPUT_FILE = 'Day_2/pt_1/2_2021_A.txt'


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

    The function will return the new position of the submarine. The position starts at 0.
    '''
def parse_commands(commands):
    position = 0
    depth = 0
    for command in commands:
        command = command.split(' ')
        if command[0] == 'forward':
            position += int(command[1])
        elif command[0] == 'up':
            depth -= int(command[1])
        elif command[0] == 'down':
            depth += int(command[1])
    return position, depth

if __name__ == '__main__':
    data = open_file(INPUT_FILE)
    position, depth = parse_commands(data)
    print(position, depth)
    total = position * depth
    print(total)

