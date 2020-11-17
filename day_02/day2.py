import numpy as np


def parse_input():
    dimensions = []
    with open('input', 'r') as file:
        for line in file:
            line = line.strip()
            dimensions.append(line.split('x'))
    return dimensions


def puzzle1(instructions: []):
    wrapping_paper = 0
    for instruction in instructions:
        lw = int(instruction[0]) * int(instruction[1])
        wh = int(instruction[1]) * int(instruction[2])
        lh = int(instruction[0]) * int(instruction[2])
        wrapping_paper += 2*lw + 2*wh + 2*lh + min(lw, wh, lh)
    return wrapping_paper


def puzzle2(instructions: []):
    total_ribbon = 0
    for instruction in instructions:
        instruction = [int(x) for x in instruction]
        # Ribbon: Shortest distance around its sides, or the smallest perimeter of any one face.
        A, B = np.partition(instruction, 1)[0:2]
        ribbon = 2*A + 2*B
        # Bow: Cubic feet of volume of the present
        bow = instruction[0] * instruction[1] * instruction[2]
        total_ribbon += ribbon + bow
    return total_ribbon


if __name__ == '__main__':
    parsed_input = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_input)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_input)}')
