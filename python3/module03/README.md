# Module 0.3.0 - Loops & Iteration
- loops, run a set of code multiple times
- an iteration is each time a loop reruns

## 0.3.1 - While Loops
evaluates code "as long as" a condition is true, if fasle, loop will end [break]
```
i = 0

while i <= 5:
	i += 1
	print(i)
	
print("loop has ended")

>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> "loop has ended"
```
loops can be infinite
```
while True:
	print("This will not stop running")
```
- to end a program from running, enter `ctrl` + `c`
- "break" statement ends loops 
```
i = 0

while i <= 5:
	i += 1
	print(i)
	
	if i == 3:
		print("ending loop")
		break

print("loop has ended")

>>> 1
>>> 2
>>> 3
>>> "ending loop"
>>> "loop has ended"
```
"continue" statement, cancels current iteration and meves to the next one
```
i = 0

while i <= 10:
	i += 1
    print(i)
	
    if i == 5:
        print("halfway there")
        continue

>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
>>> "halfway there"
>>> 6
>>> 7
>>> 8
>>> 9
>>> 10
>>> 11		
```

## 0.3.2 - Range
a function that creates a sequence of numbers
- the first argument is the start, leave blank to start from 0
- the second argument is the end
- the third argument is the interval, leave blank for no interval
```
num_list = list(range(10))
print(num_list)
>>> [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
```
- list function, creates a list [a type of data structure] using an argument
- remember, indexing starts from 0. so this list will have 10 values but will only go up to 9
- removing the list function will make the variable an object, good for iteration
```
print(list(range(1, 16)))
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```
listed range with an iterval of 2
```
even_nums_lessThan_10 = list(range(0,11,2))
print(even_nums_lessThan_10)
>>> [0, 2, 4, 6, 8, 10]
```

## 0.3.3 - For Loops
- iterating through a set of data is excessive with "while" loops
- "for" loops evaluates code "for each" item in a certain set of data
```
for i in range(5):
	print("hello")

print("loop has ended")

>>> "hello"
>>> "hello"
>>> "hello"
>>> "hello"
>>> "hello"
>>> "loop has ended"
```
break and continue statements also work with for loops

## 0.3.4 - Looping With Conditionals
- the "else" statement can also be used with loops.
- it will run it's segmented code if the loop before it runs sucessfully
```
for i in range(5):
	print("hello")
	
	if i == 7:
		break
		
print("loop has ended")

else:
	print("loop ran sucessfully")
	
>>> "hello"
>>> "hello"
>>> "hello"
>>> "hello"
>>> "hello"
>>> "loop has ended"
>>> "loop ran sucessfully"
```
