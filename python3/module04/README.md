# Module 0.4.0 - Data Structures & Lists 
- lists [or arrays] are a type of data structure that can hold multiple values 
	- "arrays" in python are very different than other languages because they can hold multiple datatypes
- the index is the placement or location of a value in an array
- the index for the first item in an array is 0, the second item's index is 1, the third's is 2, and so on...

## 0.4.1 - Initializing Lists
lists allocate an area in memory to store multiple values in one variable
- created using square brackets "[]"
- the values stored in the brackets are seperated by commas ","
	- the values can be of any datatype
```
list1 = [1, 2, 3]
print(list1)
>>> [1, 2, 3]
```
lists can be added together
```
list2 = [4, 5, 3]
my_list = list1 + list2
print(my_list)
>>> [1, 2, 3, 4, 5, 3]
```
you can print the index of a list
```
print(my_list[2])
>>> 3
```

## 0.4.2 - List Functions & Methods
- a method is a function that relates directly to an object or statement
- "append" method, adds a value to the end of a list
```
my_list.append(6)
print(my_list)
>>> [1, 2, 3, 4, 5, 3, 6]
```
 "insert" method, inserts a value at specific index
- input the index of where you want the value to be stored and then the new value
```
my_list.insert(2, 9)
print(my_list)
>>> [1, 2, 9, 3, 4, 5, 3, 6]
```
"index" method, returns the index of the first occurance of the argument
```
print(my_list.index(2))
>>> 9
```
"count" method, retutns how many times a value appears in a list
```
print(my_list.count(3))
>>> 2
```
"remove" method, removes first occurance of a value 
```
my_list.remove(3)
print(my_list)
>>> [1, 2, 9, 4, 5, 3, 6]
```
"pop" method, removes the last value of a list
```
my_list.pop()
>>> 5
print(my_list)
>>> [1, 2, 9, 4, 3, 6]
```
"reverse" method, reverses the order of a list
```
my_list.reverse()
print(my_list)
>>> [6, 3, 4, 9, 2, 1]
```
"len" function, returns the length of the list, takes list as argument
```
print(len(my_list))
>>> 6
```
"max" function, returns the largest value in a list, takes list as argument
```
print(max(my_list))
>>> 9
```
"min" function, returns the lowest value in a list, takes list as argument
```
print(min(my_list))
>>> 1
```

## 0.4.3 - Boolean Operations With Lists
"in" boolean operator, checks to see if an item is in a list
```
print(2 in my_list)
>>> True
```
"not" boolean operator, checks to see if an item is not in a list
```
print(10 not in my_list)
>>> True

print(not 10 in my_list)
>>> True
```

## 0.4.4 - List Slicing
generate new Lists between set indexes
- the first value will be the index that starts the list
- the second value will be the index that ends the list
```
list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

print(list[2:4])
>>> [15, 20, 25]
```
negative values count from the end of the list
```
list[3:-3]
>>> [20, 25, 30, 35]
```
leaving the first value empty will print the indexes until it reaches the listed index
```
print(list[:5])
>>> [5, 10, 15, 20, 25, 30]
```
leaving the second value empty will print the indexes until it reaches the final index
```
print(list[3:])
>>> [20, 25, 30, 35, 40, 45, 50]
```
leaving both values empty will print the indexes until it reaches the final index
```
print(list[:])
>>> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```
adding a third value will create an interval of the listed value
```
print(list[2:8:2])
>>> [15, 25, 35]
```
if a negative number is used as the interval, the slice is done backwards
```
list[::-1]
>>> [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
```

## 0.4.5 - List Comprehension
generate lists using some sort of rule or conditional
```
count_by_2 = [i * 2 for i in range(10)]
```
conditionals can be added
```
odd_numbers_lessThan_5 = [i for i in range(5) if i % 2 > 0]
>>> [1, 3]
```
