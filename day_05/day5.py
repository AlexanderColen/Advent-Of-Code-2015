from itertools import combinations


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


def puzzle2(instructions: []):
    nice = 0
    for s in instructions:
        pair = False
        triple = False
        for num, c in enumerate(s):
            # Check for pair.
            if not pair:
                if num + 1 < len(s):
                    p = s[num:num+2]
                    if p[0] != p[1]:
                        pair = s.count(p) > 1
                    else:
                        try:
                            if p[0] == s[num:num+3][2]:
                                pair = s.count(p) > 2
                            else:
                                pair = s.count(p) > 1
                        except IndexError:
                            pair = s.count(p) > 1
            # Check for triple.
            if not triple:
                if num + 2 < len(s):
                    triple = c == s[num:num+3][2]
            if pair and triple:
                nice += 1
                break
    return nice


if __name__ == '__main__':
    parsed_input = parse_input()
    print(f'Puzzle 1 solution: {puzzle1(instructions=parsed_input)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=parsed_input)}')