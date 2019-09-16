# Functions

Reusable pieces of code that can also make things easier to read

## Example

Let's write a program that outputs the happy birthday song lyrics to our two friends, Alice and Bob.

```python
print('Happy Birthday to you!')
print('Happy Birthday to you!')
print('Happy Birthday, dear Alice.')
print('Happy Birthday to you!')

print('Happy Birthday to you!')
print('Happy Birthday to you!')
print('Happy Birthday, dear Bob.')
print('Happy Birthday to you!')
```

And now, the same, using functions

```python
def happy_birthday(name):
    print_verse()
    print_verse()
    print('Happy Birthday, dear', name, '.')
    print_verse()

def print_verse():
    print('Happy Birthday to you!')

happy_birthday('Alice')
happy_birthday('Bob')
```

## Parameters

```python
def my_funcation(first, second, third):
    print(first, second, third)
```

## Excercise

Write a calculator program that asks a user for their name, and then asks them if they'd like to compute the area of a square, rectangle, or circle. Receive their input and print out the result.

Sample run:

```text
Your name: Charlie
Hello!
Welcome, Charlie!

What shape would you like to compute the area of (s, c, or r)? r

Width: 4
Height: 5

The area of the rectangle is 20.
```
