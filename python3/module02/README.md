# Module 0.2.0 - Booleans & Conditionals
- learn about the boolean datatype
- how to run code based on certain conditions

## 0.2.1 - Boolean Values
```
True - value exists and is correct
False - value doesn't exist and is wrong
None - value is absent
```

## 0.2.2 - Boolean Operators
```
== - equal to
!= - not equal to
<  - less than
>  - greater than
<= - less than or equal to
>= - greater than or equal to
```
Example:
```
print(True == True)
>>> True

print(True == False)
>>> False

print(1 == 2)
>>> False

print(5 <= 10)
>>> True
```

## 0.2.3 - If Statement
- runs expression[s] if a condition is true
- code that runs if a condition is true[expression] is tabbed under the conditonal
- this area of tabbed code is the scope 
```
if 5 < 10:
	print("5 is less than 10")
print("not part of the if statement")

>>> "5 is less than 10"
>>> "not part of the if statement"
```
"if" statements can be nested
```
number = 25

if number < 50:
	print("the number is less than 50")
	
	if number > 20:
		print("number is greater than 20 and less than 50")
		
>>> "the number is less than 50"
>>> "number is greater than 20 and less than 50"
```

## 0.2.4 - Else Statement
runs code if the aforementioned "if" statement is false
```
password = "SecurePassord"

if password == "SecurePassord":
	print("password is true")
	
else:
	print("Password is false")
	
>>> "password is true"
```

## 0.2.5 - Elif [Else if] Statement
a chain of "if" "else" statements
```
number = 2

if number == 1:
	print(1)
else:
	if number == 2:
		print(2)
	else:
		if number == 3:
			print(3)
		else:
			None
			
>>> 2
```
"elif" statement, a shortcut for connecting mulitiple "if" "else" statements
```
number = 2

if number == 1:
	print(1)
elif number == 2:
	print(2)
else:
	None
	
>>> 2
```

## 0.2.6 - Boolean Logic
runs code if multiple conditions are true
- boolean operations follow the mathematical "Order of Operations" [PEMDAS]

1. and
the "and" operator takes two arguments, if both are true it will return as true
```
print(True and True)
>>> True

print(True and False)
>>> False

print(False and False)
>>> True
```

2. or
the "or" operator takes two arguments, if one or both are true it will return as true
```
print(True or True)
>>> True

print(True or False)
>>> True

print(False or False)
>>> False
```

3. not
the "not" operator takes one argument and inverts its boolean value
```
print(not True)
>>> False

print(not False)
>>> True
```

4. in
the "in" operator takes two arguments, if the first argument exists in the second argument, it will return as true
```
print("a" in "apple")
>>> True
```

## 0.2.7 - Ternary Operator
create value based on a rule or condition
```
age = 15
movieRating = 13

canWatchMovie = True if age >= movieRating else False
print(canWatchMovie)
>>> True
```

## 0.2.8 - Helpful Boolean Syntax
```
# Test if a number is positive  
number > 0

# Test if a number is negative  
number < 0

# Test if a number is even by seeing if the remainder is 0 when divided by 2  
number % 2 == 0

# Test if a number is odd by seeing if there is a remainder when divided by 2  
number % 2 > 0

# Test if a number is a multiple of x (or divisible by x with no remainder)  
number % x == 0
```