# File input and output

We use file objects to manipulate files

```python
f = open('workfile', 'w')
```

The second argument is the mode

|mode|function|
|:-|-:|
|`r`|read only, default if mode is omitted|
|`w`|write, create a file to write; existing file will be erased|
|`a`|append, open for writing, but written data is added to the end|
|`r+`|read and write, keeping the file|
|`w+`|read and write, erasing the file|

Use the `with` statement for clean handling and closing of file objects

```python
with open('workfile') as f:
    # do things with the file object
```

When reading from a file, there is a cursor that advances. This ensures you will only ever read the file once.

```python
f.read() # reads and returns the entire file, but remember that the cursor will now be at the end

f.readline() # reads and returns until encountering a newline '\n' character

f.write('My new line\n') # writes the text to the open file

f.seek(0) # returns the cursor to the beginning of the file
```
