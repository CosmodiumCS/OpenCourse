# Module 0.7.0 - Methods and Functions
- a method is a function of a class, module, or object

## 0.7.1 - String Methods
"join" method, joins or connects a list of strings with an indicated seperator
```
print(','.join(["Hello","World"]))
>>> "Hello,World"
```
"split" method, splits a string into a list of substrings
```
print("Hello,World".split(","))
>>> ['Hello', 'World']
```
- "strip" method, strips all leading and trailing characters
	- removes [leading and trailing] spaces by default
```
print("             Hello, World!               ".strip())
>>> "Hello, World!"
```
- "replace" method, replaces a substring with a different string
- "substring", part of a string
```
print("Hello World".replace("World", "Earth"))
>>> "Hello Earth"
```
- "startswith" method, detect if a string starts with a certain character
	- returns a boolean value
```
print("Hello, World!".startswith("H"))
>>> True
```
- "endswith" method, detect if a string ends with a certain character
	- returns a boolean value
```
print("Hello, World!".endswith("?"))
>>> False
```
"upper" method, makes string text uppercase
```
print("Hello, World!".upper())
>>> "HELLO, WORLD!"
```
"lower" method, makes string text lowercase
```
print("Hello, World!".lower())
>>> "hello, world!"
```
"title" method, makes every substring start with a capital
```
print("hello, world!".title())
>>> "Hello, World!"
```
"isupper" method, returns boolean if string text is uppercase
```
print("HELLO, WORLD!".isupper())
>>> True
```
"islower" method, returns boolean if string text is lowercase
```
print("hello, world!".islower())
>>> True
```

## 0.7.2 - Numeric Functions
"abs" function, gets the absolute value
```
print(abs(-50))
>>> 50
```
"round" function, rounds a float to the nearest decimal place
```
print(round(9.8))
>>> 10
```
"sum" function, adds all the values in a list
```
print(sum([1, 3, 4, 10, 6, 8]))
>>> 32
```
"max" function, find the highest number in a list
```
print(max([1, 3, 4, 10, 6, 8]))
>>> 10
```
"min" function, find the lowest number in a list
```
print(min([1, 3, 4, 10, 6, 8]))
>>> 1
```

## 0.7.3 - Iterable Functions
- "any" function,checks to see if any values of a list follow an argument
	- returns boolean value
```
num_list = [1, 3, 4, 10, 6, 8]
if any(i < 10 for i in num_list):
	print("There are numbers less than 10")
	
>>> "There are numbers less than 10"
```
- "all" function, checks to see if all values of a list follow an argument
	- returns boolean value
```
num_list = [1, 3, 4, 9, 6, 8]
if all(i < 10 for i in num_list):
	print("All of the numbers are less than 10")

	
>>> "All of the numbers are less than 10"
```
"enumerate" function, iterates through the indexes and values of a list
```
num_list = [10, 15, 20, 25, 30]
for num in enumerate(num_list):
	print(num)
	
>>> (0, 10)
>>> (1, 15)
>>> (2, 20)
>>> (3, 25)
>>> (4, 30)
```
"items" function, seperates dictionary keys and values for iteration
```
laptops = {"Razer Blade":"$2200", "MacBook":"$1500", "Dell XPS": "$1800"}

for laptop, price in laptops.items():
	print(f"The {laptop} costs {price}")
	
>>> "The Razer Blade costs $2200"
>>> "The MacBook costs $1500"
>>> "The Dell XPS costs $1800"
```
