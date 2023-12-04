# only 12 red cubes, 13 green cubes, and 14 blue cubes

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def validate(line: str) -> bool:
    delimiters = [",", ";"]

    for delimiter in delimiters:
        line = '|'.join(line.split(delimiter))
    b = line.split('|')
    for p in b:
        p = p.strip()
        r = p.split()
        if int(r[0]) > limits[r[1]]:
            return False
    return True


def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        total = 0
        for line in data:
            g = line.split(':')
            game_id = int(g[0][5:])
            if validate(g[1]):
                total += game_id
        print(total)


if __name__ == '__main__':
    main()
