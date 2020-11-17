import hashlib


def puzzle1(instructions: str):
    current = 0
    while True:
        result = hashlib.md5(f'{instructions}{current}'.encode())
        if result.hexdigest()[0:5] == '00000':
            return current
        current += 1


def puzzle2(instructions: str):
    current = 0
    while True:
        result = hashlib.md5(f'{instructions}{current}'.encode())
        if result.hexdigest()[0:6] == '000000':
            return current
        current += 1


if __name__ == '__main__':
    puzzle_input = 'bgvyzdsv'
    print(f'Puzzle 1 solution: {puzzle1(instructions=puzzle_input)}')
    print(f'Puzzle 2 solution: {puzzle2(instructions=puzzle_input)}')
