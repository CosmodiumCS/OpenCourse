# Module 0.1.0 - Fundamentals
- python is case sensitive

## 0.1.1 - Datatypes
- There are different data types for handling the different types of data
	- string - datatype for text values
	- integer - datatype for whole number values
	- float - datatype for decimal values
	- boolean - datatype for true or false values
	
## 0.1.2 - Comments
- comments can be used to make notes or comments in your code
- comments are not executed by the interpreter
```
# this is a comment
```

## 0.1.3 - Errors
if your code is outputting something like this
```
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    ...
NameError: name '' is not defined
...
```
- then there is an error in your code, the last line tells you what's wrong
- we will go over errors and exceptions in module 0.9.0
	- exception, handling an error in your code
- but you probably typed something wrong or you tried to make your syntax [code in text form] do something that it can't

## 0.1.4 - Strings & Output
- single or double quotes can be used to represent strings
- the "print" function can be used to output datatypes
	- function, a statement that [typically] takes an input [argument], uses that input to perform an operation, and will return some output.
```python

print('Hello, World!')
print("Hello, World!")

# to include quotes within strings

print('My name is "Cosmo"')
print("I can't code well")
```
- the above can also be done with something called escape sequences
- escape sequences are strings that use specialized character to achieve a certain task
	- they use a backslash to innitiate
```
\" - double quote escape sequence
\' - single quote escape sequence
\n - new line escape sequence
\t - tab escape sequence
\\ - backslash escape sequence
```
Example:
```
print("My name is \"Cosmo\"")
>>> My name is "Cosmo"
```
Docstrings, multilined strings
- created by putting string text between three double quotes
```
"This srtring is one line"

"""
This string has multiple lines
first line
second line
"""
```

## 0.1.5 - Operators
Keep order of operations (PEMDAS) in mind
```python
# addition
print(1+1)

# subtraction
print(1 - 1)

# multiplication
print(1*1)

# division
print(1/1)

# exponets
print(1**1)

# remainders
print(1%1)

# quotiants
print(1//1)
```

## 0.1.6 - Operations with Strings
Concatenation, connecting two or more datatypes in one value
```
print("Hello, " + "World!"")
>>> "Hello, World!""
```
if a string is multiplied by a numeric value, it will append it's value to itself (however many times as instructed)
```
print("Hello"*3)
>>> "HelloHelloHello"
```

## 0.1.7 - Converting Datatypes 
```
String - str()
Integer - int()
Float - float()
```
Example:
```
print("1"+"1")
>>> "11"

print(int("1")+int("1"))
>>> 2
```

## 0.1.8 - Variables
assign data to a name of your choice
- acheived through assignment operator, "="
- can't start with a number
- use underscores instead of a space
```
my_varaible = 5
print(my_variable)
>>> 5
```
variables can be reassigned
```
my_variable = "Subscribe to CosmodiumCS"
print(my_variable)
>>> "Subscribe to CosmodiumCS"
```
variables can be deleted with the "del" command
```
del my_variable
```

## 0.1.9 - Variable Operations
```
# assignment operator
x = 5

# add on to saved data
x = x + 1
# or 
x += 1

# works with other datatypes
full_name = "Blue "
full_name += "Cosmo"
print(full_name)
>>> "Blue Cosmo"

# works with other operators
x = x - 1
# or
x -= 1

# others
x /= 2
x *= 2
```

## 0.1.10 - Input
get user input using the "input" function
```
input("What is your name? : ")
>>> What is your name? : cosmo
```
let's save this input to a variable and output it
```
name = input("What is your name? : ")
>>> What is your name? : cosmo

print("Your name is " + name)
>>> "Your name is cosmo"
```

## 0.1.11 - String Formatting
embed other data within a string
- accomplished by using the "format" method
- curly braces "{}" are replaced by the formatted data [seperated by commas]
```
formatted_string = "Cosmodium's birthday is on June {}, {}".format(9, 2020) 
print(formatted_string)
>>> "Cosmodium's birthday is on June 9, 2020"
```
values can be assigned to the formatted data using their index's
- an index is the placement or position of a character in a set of data
```
age = 100

msg = "I am {0} years {1}, how {1} are you".format(age, "old")
print(msg)
>>> "I am 100 years old, how old are you"
```
"F" strings are a shortcut for formatting
- indicated by placing an "f" before the single or double quotes of the string
- formatted data is placed directly in the curly braces "{}"
```
name = "bob"
age = 30

print(f"My name is {name} and I am {age} years old")
>>> "My name is bob and I am 30 years old"
```
this formatted data can be operations, variables, integers, and more
