def main():
    width = input('How wide should the tree be? ')
    height = input('How tall should the tree be? ')
    print("Here's your tree:")
    print()

    width = int(width)
    height = int(height)

    # this is the call if we omit the height
    # print_tree(width, width // 2 + width % 2)
    print_tree(width, height)


def print_tree(width, height):
    # initialize i depending on whether the width is odd or even
    i = 2 - width % 2
    trunk_count = i
    h = 0
    # how often should we increment the number of leaves?
    increment_step = int(2 * height / width)

    while h < height:
        print(' ' * ((width - i) // 2), '*' * i)
        h += 1
        if h % increment_step == 0 and i < width:
            i += 2
    print_trunk(width, trunk_count)


def print_trunk(width, count):
    print(' ' * ((width - 1) // 2), '|' * count)


if __name__ == '__main__':
    main()
