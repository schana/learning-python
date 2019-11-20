# Lists

Lists contain a collection of things that are indexed by numbers starting at zero

## Instantiation

```python
empty = []
empty = list()

numbers = [1, 2, 3, 4, 5]
string_to_list = list('something')
print(string_to_list) # ['s', 'o', 'm', 'e', ...]
''.join(['a', 's', 'd', 'f']) # returns a string joined by ''

strings = ['this', 'can', 'also', 'contain', 'strings']

my_crazy_list = ['or', 1, 'a', 2.0, 'mixture', numbers, 'of things']
print(my_crazy_list)
# ['or', 1, 'a', 2.0, 'mixture', [1, 2, 3, 4, 5], 'of things']
```

## Accessing

Items in the list are accessed by their *index*. The first item in the list has an index of `0`, the second has an index of `1`, etc.

```python
my_list = ['a', 'b', 'c', 'd']
my_list[0] # 'a'
my_list[2] # 'c'
len(my_list) # 4
```

### Fun note: Strings can be accessed like lists

```python
a = 'sample string'
len(a) # 13
a[2] # 'm'
```

## Excercise - Palindromes

Write a program that asks the user for a string, and tells them whether or not it is a palindrome (a word, phrase or sequence that is the same backwards as forwards).

Sample output:

```text
What string would you like me to check? abba
Your string, "abba", is a palinedrome!
```

```text
What string would you like me to check? crazy kids
Your string, "crazy kids", is not a palinedrome!
```

## Contains

How can we tell if an item is in a list? Use the `in` check

```python
my_list = [1, 2, 3]
if 2 in my_list:
    print('my_list contains 2')

if 5 not in my_list:
    print('my_list does not contain 5')
```

## Modification

```python
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers) # [1, 2, 3]

n = numbers.pop()
print(n) # 3
print(numbers) # [1, 2]

a = [1, 2]
b = [3, 4]
c = a + b
print(c) # [1, 2, 3, 4]
```

## Excercise - Sieve of Eratosthenes

Let's find all the prime numbers up to a given limit.

The Sieve works by using a list of numbers, and then iteratively marks out multiples until all that are left are primes.

For instance, imagine we have the list
>2, 3, 4, 5, 6, 7, 8, 9, 10

We begin with the first number, 2, which we know is a prime. We then mark out all the multiples of 2 from the list.
> 2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, 9, ~~10~~

Once we're finished, we move on to the next number, 3. We now know this is a prime. We now mark out multiples of 3 from the list.
> 2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~

We continue this process until we've worked through the entire list. All of the unmarked numbers are primes.
> 2, 3, 5, 7

The excercise is to write a program that asks the user to what number they would like to find all the primes. The program then finds them utilizing the Sieve of Eratosthenes and prints out a list for the user.

Sample output:

```text
To what number would you like to know primes? 10
The primes through 10 are:
2, 3, 5, 7
```
