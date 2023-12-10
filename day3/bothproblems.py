import math as m
import re


def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        char_pos = {(r, c): [] for r in range(140) for c in range(140)
                    if lines[r][c] not in '0123456789.'}
        for i, line in enumerate(lines):
            for n in re.finditer(r'\d+', line):
                edge = {(r, c) for r in (i-1, i, i+1)
                        for c in range(n.start() - 1, n.end() + 1)}
                for o in edge & char_pos.keys():
                    char_pos[o].append(int(n.group()))

        print(sum(sum(p) for p in char_pos.values()), sum(m.prod(p)
              for p in char_pos.values() if len(p) == 2))


if __name__ == '__main__':
    main()
