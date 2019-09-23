# Decisions

An introduction to if statements

## Example

```python
n = int(input('Number? '))
if n < 0:
   print('The absolute value of', n, 'is', -n)
else:
   print('The absolute value of', n, 'is', n)
```

## Equality tests

`if` is a check to see if an expression is true or false

|operator|function|
|:-|-:|
|`<`|less than|
|`<=`|less than or equal to|
|`>`|greater than|
|`>=`|greater than or equal to|
|`==`|equal|
|`!=`|not equal|

## `elif`

We can have complex if statements with multiple blocks.

```python
import random

n = random.randint(1, 6)

if n == 1:
    print('Signs point to yes')
elif n == 2:
    print('Outlook good')
elif n == 3:
    print('Reply hazy, try again')
elif n == 5:
    print('Most likely')
elif n == 4:
    print('My sources say no')
else:
    print('Ask again later')
```

## FizzBuzz

Write a program that prints each number from 1 to 100 on a new line. For each multiple of 3, print `Fizz` instead of the number. For each multiple of 5, print `Buzz` instead of the number. For number which are multiples of both 3 and 5, print `FizzBuzz` instead of the number.

Example:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
97
98
Fizz
Buzz
```
