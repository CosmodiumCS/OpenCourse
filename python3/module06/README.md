# Module 0.6.0 - Working With Modules
- python is a very dynamic language
- one effect of this is how modular it is
- in python, and some other languages, we can import modules to give our code more funcitonality

## 0.6.1 - Importing Modules
"import" command, imports a module
```
import MODULE
```
"as" operator, module to a variable name
```
import MODULE as VARIABLE
```
- "from" statement, import specific method[s] from certain modules
```
from MODULE import METHOD
```
"as" statement can be used with "from"
```
from MODULE import METHOD as VARIABLE
```

## 0.6.2 - The Zen of Python
a set of rules on how to write python code effeciently
```
import this 

>>> The Zen of Python, by Tim Peters

>>> Beautiful is better than ugly.
>>> Explicit is better than implicit.
>>> Simple is better than complex.
>>> Complex is better than complicated.
>>> Flat is better than nested.
>>> Sparse is better than dense.
>>> Readability counts.
>>> Special cases aren't special enough to break the rules.
>>> Although practicality beats purity.
>>> Errors should never pass silently.
>>> Unless explicitly silenced.
>>> In the face of ambiguity, refuse the temptation to guess.
>>> There should be one-- and preferably only one --obvious way to do it.
>>> Although that way may not be obvious at first unless you're Dutch.
>>> Now is better than never.
>>> Although never is often better than \*right\* now.
>>> If the implementation is hard to explain, it's a bad idea.
>>> If the implementation is easy to explain, it may be a good idea.
>>> Namespaces are one honking great idea -- let's do more of those!
```

## 0.6.3 - Random Module
- module used ot generate random values
- import the random module
```
import random
```
assign module to variable name "r"
```
import random as r
```
"random" method, returns random value between 0 and 0.999...
```
print(r.random())
>>> 0.6000450210967234
```
"uniform" method, returns random value between two points as a float
- values put as the first argument are inclusive, they are included as a possible output
- values put as the second argument are noninclusive, they are not included as a possible output
```
print(r.uniform(1, 10))
>>> 7.20157760130375
```
"randint" method, returns value between two points as integrs [inclusive]
```
print(r.randint(1, 10))
>>> 5
```
"choice" method, returns random value from a group
```
dice = [1, 2, 3, 4, 5, 6]
print(r.choice(dice))
>>> 4
```
"choices" method, returns multiple values from a group
- k variable = number of values we wish to return
```
print(dice, k = 3)
```
"shuffle" method, returns shuffled values
```
numbers = [5, 4, 6, 7, 3]
r.shuffle(numbers)
print(numbers)
>>> [6, 7, 5, 4, 3]
```
"sample" method, returns random values [none of witch are repeated]
```
pick_numbers = r.sample(numbers, k=3)
print(pick_numbers)
>>> [4, 3, 7]
```

## 0.6.4 - Python Package Index [PYPI]
- python does come preinstalled with modules, but you can install more modules for more functionality
- you can do this from the PYPI: 'https://pypi.org/'
---
- "pip", installs modules
	- you should have pip if you installed python properly
	- if you don't navigate here: 'https://packaging.python.org/tutorials/installing-packages/'
- naviagate to your command line [Command Prompt [CMD], powershell, or terminal; depends on your operating system]
```
pip install MODULE
```
