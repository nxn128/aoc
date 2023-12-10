def get_int_list(input: list[str]) -> list[int]:
    return [int(i.strip()) for i in input.split()]


def get_points(line: str):
    all_nums = line.split(':')[1].split('|')
    winning_nums = get_int_list(all_nums[0])
    card_nums = get_int_list(all_nums[1])

    # could use set assuming no dups
    hit = -1
    for wn in winning_nums:
        if wn in card_nums:
            hit += 1

    return pow(2, hit) if hit >= 0 else 0


def main():
    with open('input.txt', 'r') as f:
        total = 0
        lines = f.readlines()
        for line in lines:
            total += get_points(line)
        print(total)


if __name__ == '__main__':
    main()
