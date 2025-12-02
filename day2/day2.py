from pathlib import Path

# file reader, ensures it can be found
def read_file():
    script_dir = Path(__file__).parent
    file_path = script_dir / "day2-puzzle-input.txt"
    with open(file_path, "r") as file:
        content = file.read()
        lines = content.split(",")
        return lines
    

# algo: loop through every iteration of start and end, and check if the snippet matches front to back
# if so, add it, do this for each item, time is O(n^2)
def get_all_invalids(start_num, end_num) -> int:
    invalidTotal = 0

    for num in range(start_num, end_num + 1):
        snippet = str(num)
        chars = len(snippet)
        if (chars % 2 == 0 and snippet[:chars//2] == snippet[chars//2:]):
            invalidTotal += num

    return invalidTotal

# we just have to brute force this
def validate_ID(num) -> bool:
    snippet = str(num)
    chars = len(snippet)

    for i in range(1, chars):
        all_groups = set()
        if chars % i == 0:
            n_groups = chars // i
            for j in range(n_groups):
                group = snippet[j * i : (j+1) * i]
                all_groups.add(group)
            if len(all_groups) == 1: 
                return True
    return False
    

# part 1 solver
def check_IDs(inputs) -> int:
    total_number = 0
    # first, split the numbers
    for item in inputs:
        items = item.split("-")
        start_num = int(items[0])
        end_num = int(items[1])
        total_number += get_all_invalids(start_num, end_num)
    return total_number

# part 2 solver
def check_all_IDs(inputs) -> int:
    total_number = 0
    # first, split the numbers
    for item in inputs:
        items = item.split("-")
        start_num = int(items[0])
        end_num = int(items[1])
        for num in range(start_num, end_num + 1):
            if(validate_ID(num)):
                total_number += num
    
    return total_number


inputs = read_file()
day2_part1_sol = check_IDs(inputs)
day2_part2_sol = check_all_IDs(inputs)
print(day2_part1_sol)
print(day2_part2_sol)