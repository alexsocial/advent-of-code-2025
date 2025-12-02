from pathlib import Path

# file reader, ensures it can be found
def readFile():
    script_dir = Path(__file__).parent
    file_path = script_dir / "day1-puzzle-input.txt"
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.splitlines()
        return lines

# part 1 solver
def find_zeroes(inputs, starting_pos):
    total_zeroes = 0
    for line in inputs:
        direction = line[0]
        num = int(line.split(direction)[1])

        # add or sub based on direction
        if (direction == 'L'):
            starting_pos = starting_pos - num
        else:
            starting_pos = starting_pos + num

        # next, filter the number based on if higher than 100 or negative
        if starting_pos > 99:
            starting_pos = starting_pos % 100
        elif(starting_pos < 0):
            starting_pos = abs(starting_pos) % 100
            if(starting_pos != 0):
                starting_pos = 100 - abs(starting_pos % 100)
        if(starting_pos == 0):  
            total_zeroes += 1

        
    return total_zeroes

# part 2 passes
def find_passes(inputs, starting_pos):
    total_zeroes = 0
    for line in inputs:
        direction = line[0]
        num = int(line.split(direction)[1])

        # add or sub based on direction, remove a zero SPECIFICALLY on negatives because of the add 1 fallacy later
        if (direction == 'L' and starting_pos == 0):
            starting_pos = starting_pos - num
            total_zeroes -= 1
        elif(direction == 'L'):
            starting_pos = starting_pos - num
        else:
            starting_pos = starting_pos + num

        # next, filter the number based on if higher than 100 or negative
        if starting_pos > 99:
            total_zeroes += (starting_pos // 100)
            starting_pos = starting_pos % 100
        elif (starting_pos == 0):
            total_zeroes += 1
        elif(starting_pos < 0):
            total_zeroes += (abs(starting_pos) // 100) + 1 # add one because zero is guarantee passed
            starting_pos = abs(starting_pos) % 100
            if(starting_pos != 0):
                starting_pos = 100 - abs(starting_pos % 100)

        
    return total_zeroes

# begin sequence
inputs = readFile()
starting_pos = 50
day_1_sol = find_zeroes(inputs, starting_pos)
day_1_p2_sol = find_passes(inputs, starting_pos)
print(day_1_sol, day_1_p2_sol)