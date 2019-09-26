def main():
    text = input('What string would you like me to check? ')
    i = 0
    is_palindrome = True
    while i < len(text) / 2:
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
        i += 1

    if is_palindrome:
        print('Your string, "' + text + '", is a palindrome!')
    else:
        print('Your string, "' + text + '", is not a palindrome!')


if __name__ == '__main__':
    main()
