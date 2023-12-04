import re

valid_digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


def get_cal(line: str) -> int:
    first = None
    first_pos = 99999
    last = None
    last_pos = -1

    for k, v in valid_digits.items():
        r = [m.start() for m in re.finditer(k, line)]
        ll = len(r)
        if ll < 1:
            continue

        b = r[0]
        e = r[ll - 1]

        if b < first_pos:
            first = v
            first_pos = b
        if e > last_pos:
            last = v
            last_pos = e
    cal = int(f'{first}{last}')
    return cal


def main():
    print('calculating calibration...\n')
    cal = 0
    with open('input.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            cal += get_cal(line)

    print(f'calibration = {cal}')


if __name__ == '__main__':
    main()
