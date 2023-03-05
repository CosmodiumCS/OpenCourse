# Module 0.9.0 - Exception Handling
- handling errors [exceptions] in python
	- prevents code from breaking

## 0.9.1 - Error Types
- in most programming languages, there are three main types of erros
1. Syntax Error - occurs when the syntax of a program is incorrect
```
# the "print" function is spelled incorrectly [pint]
pint("Hello, World")
>>> ERROR
```
2. Run-Time Error - occurs when invalid data is inputted during "runtime"
	- runtime, any time after a program starts running
```
# this program asks for integer input, the user inputs a string
int(input("What is your favorite number? : "))
>>> What is your favorite number? : tree
>>> ERROR
```
3. Logical Error - Program runs as normal but not as intended
	- typically the hardest to find
```
# the program is intended to print their name before their age
name = "bob"
age = "100"
print(f"Hello, my name is {age} and I am {name} years old")

>>> "Hello, my name is 100 and I am bob years old"
```

## 0.9.2 - Try & Except Statements
- permits the developer to *try* a code segment, *except* if it doesn't work, it will run a different code segment 
- "try" statement, try code that may cause an exception
- "except" statement, if an exception occurs in the try block, it will stop running, and run a different segment of code
```
try:
	print(2/0)
	print("This will not print")
	
except:
	print("You can't divide by zero")
```
it is good practice to specify the exception the program is looking for
```
try:
	print(2/0)
	print("This will not print")
	
except ZeroDivisionError:
	print("You can't divide by zero")
```
you can specify multiple exceptions in the exception block
```
try:
	print(2/0)
	print("This will not print")
	
except ZeroDivisionError, TypeError:
	print("Error)
```
you can chain except statements to specify multiple exceptions
```
try:
	money = "10"
	# "money" is a string, the following will cause a type error
	print(money - 3)
	print("This will not print")
	
except ZeroDivisionError:
	print("You can't divide by zero")
	
except TypeError:
	print("You can't subtract an integer from a string")
```

## 0.9.3 - Raise
- "raise" statement, displays the error that occured in the "try" statement
- good for figuring out what error you are dealing with
```
try:
	print(2/0)
	print("This will not print")
	
except:
	print("Error")
	raise
```
"raise" can also be used to throw an exception into runtime
```
print("Hello World!")
raise ZeroDivisionError
print("Will not run")
```
you can add a description with raised errors
```
print("Hello World!")
raise ZeroDivisionError("incorrect value")
print("Will not run")
```

## 0.9.4 - Finally
- "finally" statement, runs code no matter what 
 - comes last when creating "try" and "except" statements
 ```
try:
	print(2/0)
	print("This will not print")
	
except ZeroDivisionError:
	print("You can't divide by zero")
	
finally:
	print("This will print no matter what")
 ```

## 0.9.5 - Assertion
- "assert" statement, uses boolean operators to test an expression
	- if true, the code will run as normal
	- if false, the code will raise an "AssertionError" exception
	- good for testing
```
account = 100

# checks to see if account has the proper value
assert account == 50 
>>> AssertionError
```
an argument can be added to the "assert" statement where it returns said argument in the exception message
```
account = 100

# checks to see if account has the proper value
assert account == 50, "account should equal '100'"
>>> AssertionError: account should equal '100'
```

## 0.9.6 - Handling Exceptions With Conditionals
- the else statement can be used to handle exceptions
- it will run its segmented code if no exceptions occur withing the try statement
```
try:
	print(2/0)
	print("This will not print")
	
except ZeroDivisionError:
	print("You can't divide by zero")
	
else: 
	print("This will print if there are no errors")
	
finally:
	print("This will print no matter what")
```

## 0.9.7 - Helpful Summary
If you are still confused, here is a helpful summary
```
try - tries to run a segment of code
except - runs if an error occurs
else - runs if no errors occur
finally - runs no matter what
```