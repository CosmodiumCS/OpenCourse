# Module 0.8.0 - Working With Files
- python can edit files
	- read files
	- write files

## 0.8.1 -  Opening Files
- in python, we need to open files before we can read or edit them
	- just like how we do
- "open" function, opens files, takes filename as argument
```
file = open("file.txt")
```

## 0.8.2 - Opening File Arguments
- the first argument is the path to the file
	- if the file is within the same directory as the program, you can just enter the filename
- the second argument is the mode the file will be opened in
- the three modes we will cover [there are more] in this course are: 
1. "read" mode [r]
```
file = open("file.txt", "r")
```
- by default, files are opened in read mode
2. "write" mode [w]
```
file = open("file.txt", "w")
```
3. "append" mode [a]
```
file = open("file.txt", "a")
```

## 0.8.3 - Closing Files
- when we are done working with a file, we need to close it in order to effectly save our changes
- "close" method, closes files
```
file = open("file.txt", "w")
...
f.close()
```

## 0.8.4 - Reading Files
- python reads files from top to bottom, meaning that if a file is read, it needs to be reopened to be read again [so make sure to save the read content to a variable]
- "read" method, reads file contents
```
file = open("file.txt", "r")
read_file = f.read()
f.close()

# prints file contents
print(f"File Contents:\n{read_file}")
```
numbers can be used as an argument to read specific lines of a file
```
file = open("file.txt", "r")

# prints line 5
print(f.read(5))

file.close()
```
- "readlines" method, reads each line of the file rather than each character
- file data is iterable, they can be looped through
```
username = "cosmo"

# gets file data
file = open("file.txt", "r")
read_lines = file.readlines()
file.close()

# iterates through file data
for line in read_lines:
	if username in line:
		print("user exists")
```

## 0.8.5 - Writing Files
- writing to a file will empty it's current contents, and replace it with your inputed data
- if the file python opens doesn't exist, it will create it
- "write" method, writes string data to file
- the srting argument will be the content written to the file
```
file = open("file.txt", "w")

# write to a file
file.write("Hello, World!")
file.close

read_file = open("file.txt", "r").read()
read_file.close()

print(read_file)
```

## 0.8.6 - Appending Files
- as I mentioned before, writing to a file replaces the current existing data with the new attached data
	- this doesn't matter if you are generating a file or writing to a blank doucment
- one way we can acheive this is by reading a file, and writing the read data with our new data
```
old_data = open("file.txt", "r").read()
old_data.close()

file = open("file.txt", "w")
file.write(f"{old_data}\nNew Data")
```
- this is effective but there is an easier alternative, writing to a file in "append" mode
```
file = open("file.txt", "a")
file.write("this line was added on to the old data")
file.close()
```

## 0.8.7 - With Statement
- ensures that the file will close in case of exception [error]
- will create a variable only accessible within the "with" statements scope
- scope, the area where a variable can be accessed [more on this in the future]
```
with open("file.txt", "r") as f:
	print(f"File Contents: \n{f.read()})
```
- notice how the file did not need to be opened or closed, it was handled in the "with" statement
