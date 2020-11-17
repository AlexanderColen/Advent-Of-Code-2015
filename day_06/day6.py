import numpy as np


def parse_input():
    instructions = []
    with open('input', 'r') as file:
        for line in file:
            instructions.append(line.strip())
    return instructions


def puzzle1(instructions: []):
    grid = np.zeros((1000, 1000))
    for instruction in instructions:
        instruction = instruction.replace('turn ', '')
        instruction = instruction.replace(' through', '')
        whatdo, start, end = instruction.split()
        start_x, start_y = start.split(',')
        end_x, end_y = end.split(',')
        # Toggle lights
        if whatdo == 'toggle':
            for y in range(int(start_x), int(end_x) + 1):
                for x in range(int(start_y), int(end_y) + 1):
                    grid[x, y] = 0 if grid[x, y] == 1 else 1
        # Turn lights on/off
        else:
            new = 0 if whatdo == 'off' else 1
            for y in range(int(start_x), int(end_x) + 1):
                for x in range(int(start_y), int(end_y) + 1):
                    grid[x, y] = new

    count = 0
    for r in grid:
        for i in r:
            if i == 1:
                count += 1
    return count


def puzzle2():
    return 0


if __name__ == '__main__':
    parsed_input = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_input)}')
    print(f'Puzzle 2 solution: {puzzle2()}')
