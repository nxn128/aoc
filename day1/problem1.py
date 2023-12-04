def main():
    print('calculating calibration...\n')
    cal = 0
    with open('input.txt', 'r') as f:
        first_digit = last_digit = None
        data = f.readlines()
        for line in data:
            for c in line:
                if first_digit is None and c.isdigit():
                    first_digit = c
                    last_digit = c
                if c.isdigit():
                    last_digit = c
            line_cal = int(f'{first_digit}{last_digit}')
            first_digit = last_digit = None
            cal += line_cal

    print(f'calibration = {cal}')


if __name__ == '__main__':
    main()
