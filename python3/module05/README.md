# Module 0.5.0 - Dictionaries, Tuples, Sets
- more data structures

## 0.5.1 - Dictionaries
- an array type that can list multiple keys [items] and assign each key a value [definition]
- dictionaries have no order
> Initialization
- created using curly braces "{}"
- keys in between the curly braces are seperated by a comma ","
- each key is assigned  a value by using a colon ":"
```
my_dict = {"name":"cosmo", "age":100, "occupation":"hacker"}
```
dictionaries can be indexed
```
print(my_dict["name"])
>>> "cosmo"
```
values can be added or changed through the assignmetn operator
```
nums = {"one":1, "two":2, "three":5}
nums["four"] = 4
nums["three"] = 3
print(nums)
>>> {"one":1, "two":2, "three":3, "four":4}
```
"in" and "not" boolean operators in work with dictionary keys
```
print("two" in nums)
>>> True

print("one" not in nums)
>>> False
```
"get" method, returns the key's value, can return specified value if key is not found
- if no return value is specified, it will return "None"
```
print(nums.get("three"))
>>> 3

print(nums.get("five", "key does not exist"))
>>> "key does not exist"
```

## 0.5.2 - Tuples
- lists that can not be edited, immutable
- iterate faster than lists
- created using parenthesis "()" or just seperating values with commas ","
	- values are seperated by commas "."
```
my_tuple = (1, 2, 3, 4, 5)
my_other_tuple = 1, 2, 3, 4, 5
```
tuples can be indexed
```
print(my_tuple[3])
>>> 4
```
list slicing can also be done with tuples
```
print(my_tuple[1:3])
>>> (2, 3, 4)
```

## 0.5.3 - Sets
- assign multiple values to one variable
- sets are not ordered, they can not be indexed
- they can not contain duplicate items
- can use most of the list methods
- created using curly braces "{}" or the "set" function, takes list as argument
- each item is seperated by a comma ","
```
set_using_braces = {1, 2, 3, 4, 5}
set_using_function = set([1, 2, 3, 4, 5])
```
sets can use "in" and "not" boolean operators
```
my_set = {"apple", "orange", "bannana"}
print("apple" in my_set)
>>> True
```
"add" method, add item to end of set
- this replaces "append" method
```
my_set.add("pear")
print(my_set)
>>> {"apple", "orange", "bannana", "pear"}
```

## 0.5.4 - Set Operators
sets have unuiqe operators for comining with other sets
```
set1 = {0, 2, 4, 6, 8, 9}
set2 = {2, 3, 5, 7, 9, 6}
```
"union" operator, combines two sets into one [with no duplicate items]
- created using the pipe "|"
```
print(set1 | set2)
>>> {0, 2, 3, 4, 5, 6, 7, 8, 9}
```
"intersection" operator, combines two sets into one [with items only in both sets]
- created using the ampersand "&"
```
print(set1 & set2)
>>> {9, 2, 6}
```
"difference" operator, combines two sets into one [with items in the first, but not in the second]
- created using the minus "-"
```
print(set1 - set2)
>>> {0, 8, 4}
```
"symmetric difference" operator, combines two sets into one [with items in either set]
- created using carrot "^"
```
print(set1 ^ set2)
>>> {0, 3, 4, 5, 7, 8}
```

## 0.5.5 - Iterable Unpacking
assign each item in an iterable [lists, dictionaries, tuples, sets] to a variable
```
nums = (1, 2, 3)
one, two, three = nums

print(two)

>>> 2
```
allows for easy value swapping for variables
```
one, two = two, one
```
if there is an asterisk `*` placed before the variable, it will assign itself to the remaining values
```
lowest_num, *other_nums, highest_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(other_nums)
>>> [2, 3, 4, 5, 6, 7, 8, 9]
```
