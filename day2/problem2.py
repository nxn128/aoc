

def get_mins(line: str) -> dict():
    delimiters = [",", ";"]
    balls = {
        'blue': 0,
        'red': 0,
        'green': 0,
    }

    for delimiter in delimiters:
        line = '|'.join(line.split(delimiter))
    b = line.split('|')
    for p in b:
        p = p.strip()
        r = p.split()
        if balls[r[1]] < int(r[0]):
            balls[r[1]] = int(r[0])
    return balls


def main():
    with open('input.txt', 'r') as f:
        data = f.readlines()
        total = 0
        for line in data:
            g = line.split(':')
            p = 1
            for v in get_mins(g[1]).values():
                p *= v
            total += p
        print(total)


if __name__ == '__main__':
    main()
