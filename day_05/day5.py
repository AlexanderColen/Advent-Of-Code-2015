def parse_input():
    strings = []
    with open('input', 'r') as file:
        for line in file:
            strings.append(line.strip())
    return strings


def puzzle1(instructions: []):
    nice = 0
    for s in instructions:
        # Skip if less than 3 vowels.
        if s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') < 3:
            continue
        # Skip if any banned substring exists.
        if s.count('ab') + s.count('cd') + s.count('pq') + s.count('xy') > 0:
            continue
        last = ''
        for c in s:
            if last == c:
                nice += 1
                break
            last = c
    return nice


def puzzle2():
    return 0


if __name__ == '__main__':
    parsed_input = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_input)}')
    print(f'Puzzle 2 solution: {puzzle2()}')