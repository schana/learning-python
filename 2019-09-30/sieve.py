def main():
    end = int(input('To what number would you like to know primes? '))
    numbers = list(range(2, end + 1))
    is_prime = [True] * len(numbers)
    primes = []
    i = 0
    while i < len(numbers):
        if(is_prime[i]):
            primes.append(numbers[i])
            j = i + numbers[i]
            while j < len(numbers):
                is_prime[j] = False
                j += numbers[i]
        i += 1
    print('The primes through', end, 'are:')
    print(primes)


if __name__ == '__main__':
    main()
