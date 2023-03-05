 # Module 0.10.0 - Functional Programming
- a method of programming using funcitons
- function, a statement that [typically] takes an input, uses that input to perform an operation, and will return some output.
```
print("Hello, World")
>>> Hello, World
```
functions are typically structured as a statement, followed by some parenthesis "()"

## 0.10.1 - Defining and Calling Functions
- in python, and most programming languages, we can make our own functions
- in order to do this, we must define them
- "def" statement, defines function
```
# defines function
def my_func():
	print("Hello, World!")
```
- now we that we have a function defined, we can call it
- functions are called by placing the name of the function, followed by parenthesis "()" 
```
my_func()
>>> "Hello, World!"
```
- functions can be called multiple times

## 0.10.2 - Working With Arguments
- functions can take argument, allows for ease of use and optimal code
- argument, data that is inputted into a function [of some sort]
	- arguments [can] serve as varibles, only available in the functions scope
```
# this function squares numbers, "number" is the argument
def squared(number):
	print(number**2)
	
squared(2)
squared(3)
squared(4)

>>> 4
>>> 9
>>> 16
```
- multiple arguments can be used within a function.
- each argument is seperated by a comma.
```
# this function will add two numbers together
def add_together(num1, num2):
	print(num1 + num2)
	
add_together(1, 2)

>>> 3
```

## 0.10.3 - Returning Data
- functions can return data that can be assigned and used in operations
- "return" statement, returns data that can be used in operetions
	-  the function will stop once the "return" statement is used
```
# this function will double a number and return the value
def double(num):
	return num * 2

print(double(2))
>>> 4
```
- the function can now be used as an object, argument, or value; because it can be assigned a value
```
four = double(2)
multiply_by_2 = double
print(multiply_by_2(5))
print(multiply_by_2(four))

>>> 10
>>> 8
```
- the 'double' function above is a pure function, this is because it returns a value that only depends on the arguments attached
	- pure functions are more ideal in the programming world
- an impure function depends on an external value or datatpype
```
message = "Hello, "
def impure_function(text):
	return message + text 
	
greeting = impure_function
greeting("World!")

>>> "Hello, World!"
```

## 0.10.4 - Higher-Order Functions
a type of function that utilizes another function as an argument
```
# normal function
def talk(message):
	return message

uppercase_msg = talk
uppercase_msg("Hello, World!")

# higer-order function
def message(func):
	uppercase_msg = func("Hello, World")
	print(uppercase_msge)
	
message(talk)

>>> Hello, World!
>>> Hello, World
```
- this allows us to make our functions versatile, and add more functionality
- we can use this same example to output different types of text.
```
def title_case(text):
	return text.title()
	
def lower_case(text):
	return text.lower()
	
def upper_case(text):
	return text.upper()
	
def message(case, text):
	output = case(text)
	print(output)

hw = "Hello, World!"
message(upper_case, hw) 
message(lower_case, hw)
message(title_case, hw)

>>> HELLO, WORLD!
>>> hello, world!
>>> Hello, World!
```

## 0.10.5 - Special Arguments
- python has special arguments we can use in our functions
- defined arguments, assinging default values to arguments
	- in the event that they are not defined, avoids error
- defining arguments can be done with the assigment operator "="
```
def profile(name = "Enter name", age = "Enter age", status = "Enter status"):
	return f"Name : {name}\nAge : {age}\nStatus : {status}\n"
	
bobs_account = profile("bob", "25")
joes_account = profile("Joe", "48", "single")

print(bobs_account)
print(joes_account)
```
- "\*" args argument, allows you to pass an undefined amount of arguments to a function, and assigns them to a tuple labled after your args variable name
	- the default is "args"
```
def class_schedule(mandatory_class, *args):
	print(f"Period 1: {mandatory_class}")
	
	period_number = 2
	
	for course in args:
		print(f"Period {period_number}: {course}")
		period_number += 1
		
class_schedule("Homeroom", "Math", "Science", "English", "History")

>>> Period 1: Homeroom
>>> Period 2: Math
>>> Period 3: Science
>>> Period 4: English
>>> Period 5: History
```
- "\*\*" kwargs argument, passes defined arguments into a dictionary labled after your kwarg variable name
	- the default is "kwargs"
- dictionary key = argument name, dictionary value = argument value
```
def groceries(store_name, **kwargs):
    print("\n"+store_name)
    for food, price in kwargs.items():
        print(f"{food} --> {price}")
		
groceries("Giant", apples = "$1.50", oranges = "$2.50", bananas = "$1.75")
groceries("Publix", apples = "$1.00", oranges = "$3.50", bananas = "$2.00")

>>> Giant
>>> apples --> $1.50
>>> oranges --> $2.50
>>> bananas --> $1.75
>>> 
>>> Publix
>>> apples --> $1.00
>>> oranges --> $3.50
>>> bananas --> $2.00
```

## 0.10.6 - \_\_main\_\_
- allows your code to be both imported into other projects and scripts, or can run as is
- the conditional `if __name__ == "__main__:"` detects if the code is being ran or imported, respectively
	- the attached expression will run if the code is being ran
- let's make a file called 'script.py' and run it
- script.py syntax
```
def double(n):
	return n*2
	
def main():
	# write main code in here
	print(f"2 doubled is {double(2)}")
	
if __name__ == "__main__":
	main()
	
>>> "2 doubled is 4"
```
- we can now effeciently import other dictionaries it into another file
- calculator.py syntax
```
import script # name of file [in same directory]

print(script.double(4))

>>> 8
```

## 0.10.7 - Mapping and Filtering
- "map" function, use each item in a list as an argument to a function
	- the first argument is the function
	- the second argument is the iterable
```
def double(n):
	return n * 2
	
numbers = [1, 2, 3, 4]
mapped_list = map(double, numbers)
print(list(mapped_list))

>>> [2, 4, 6, 8]
```
- "filter" function, iterates through a list, only returns values that follow a certain argument
	- the first argument is the function
	- the second argument is the iterable
```
def even(n):
	return n % 2 == 0
	
numbers = [1, 2, 3, 4]
filtered_list = filter(even, numbers)
print(list(filtered_list))

>>> [2, 4]
```

## 0.10.8 - Lambda
- a less powerful function that works in one line
	- can take in many arguments but only returns one expression
```
double = lambda x : x * 2
double(2)
double(3)
double(4)

>>> 4
>>> 6
>>> 8
```
- lambda's can take more than one argument
```
add_together = lambda x, y = x + y
add_together(3, 7)

>>> 10
```
- lambda's aren't always assigned to varaibles
- they can be used as arguments for functions
```
num_list = list(range(-10, 11))
positive_values = list(filter(lambda x: x > 0, num_list))
print(positive_values)

>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```