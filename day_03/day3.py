def parse_input():
    with open('input', 'r') as file:
        for line in file:
            return line


def puzzle1(instructions: str):
    x, y = 0, 0
    visited = {tuple([x, y])}
    for instruction in instructions:
        # Move.
        if instruction == '^':
            y += 1
        elif instruction == 'v':
            y -= 1
        elif instruction == '>':
            x += 1
        elif instruction == '<':
            x -= 1
        # Add location
        visited.add(tuple([x, y]))
    return len(visited)


def puzzle2():
    return 0


if __name__ == '__main__':
    parsed_input = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_input)}')
    print(f'Puzzle 2 solution: {puzzle2()}')
