# Syntax Cheat Sheet

## Variables

```python
a = 2 # Assigns the integer value 2 to the variable a
b = 3
c = a + b # Assigns the value of a plus b to the variable c
s = 'some string'
```

## Control Structures

### While loops

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

### If statements

```python
a = 1
b = 2
if a == b:
    print('a and b are equivalent')
elif a < b:
    print('a is smaller than b')
else:
    print('a is greater than b')
```

|operator|function|
|:-|-:|
|`<`|less than|
|`<=`|less than or equal to|
|`>`|greater than|
|`>=`|greater than or equal to|
|`==`|equal|
|`!=`|not equal|

### For loops

```python
for i in range(10):
    print(i)

for letter in 'my string':
    print(letter)
```

### Nesting

```python
for i in range(20):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')
```

## Functions

```python
def my_function(parameter_1, parameter_2):
    print(parameter_1, parameter_2)

# Then you can call your function like this
my_function('high', 'school')
# prints "high school" to the console
```

Standard convention for Python files:

```python
def main():
    # put your program's code here


if __name__ == '__main__':
    main()
```

## Data structures

All of the following can also use the `len()` call to get their length

```python
my_list = [0, 1, 2, 3, 4]
print(len(my_list)) # 5
```

### Lists

```python
empty_list = []
empty_list = list()

my_list = [0, 1, 2, 3, 4]
my_list = list(range(5))

my_list = ['a', 'b', 'c']
print(my_list[0]) # a
print(my_list[1]) # b
print(my_list[len(my_list) - 1]) # c
print(my_list[-1]) # shorthand of the previous call
```

### Tuples

```python
empty_tuple = ()
empty_tuple = tuple()

my_tuple = (0, 1, 2, 3, 4)
my_tuple = tuple(range(5))
```

### Dictionaries

```python
empty_dict = {}
empty_dict = dict()

my_dict = {'one': 'eins', 'two': 'zwei', 'three': 'drei'}
print(my_dict['one']) # eins
my_dict['four'] = 'vier' # this adds the entry to the dictionary
my_dict.keys() # returns an iterable of the keys
my_dict.values() # returns an iterable of the values
for key in my_dict.keys():
    print(my_dict[key]) # this will print all the values
```

## Other helpful info

### User input

```python
user_input = input('What would you like to input? ')
```

### Keyboard shortcuts

Press `Ctrl + c` to break out of a runaway loop

Press `Ctrl + d` to exit the Python interpreter
