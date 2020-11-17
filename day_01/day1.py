def parse_input():
    with open('input', 'r') as file:
        for line in file:
            return line


def puzzle1(instructions: str):
    up_count = instructions.count('(')
    down_count = instructions.count(')')
    return 0 + up_count - down_count


def puzzle2(instructions: str):
    floor = 0
    for num, c in enumerate(instructions):
        if c == '(':
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                return num + 1


if __name__ == '__main__':
    parsed_instructions = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_instructions)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_instructions)}')
