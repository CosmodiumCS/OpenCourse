# Module 0.11.0 - Object Oriented Programming
- a programming style based on the use of classes and objects
- a class is a blueprint for an object
- an object is a variable created from a class's definition
- object's have attributes and behaviors
	- an attribute is an object's properties
	- a behavior [or method] is what an object does

## 0.11.1 - Class's Put Into Context
This will be our hypothetical for most of this lesson
- let's say you are making a game with python
- in this game, there will be different types of dogs
- instead of individually programming each dog, we can create a blueprint or class that all the dogs can follow
---
- let's say we make a dog class (or blueprint)
- we will need to account for a dog's attributes and behaviors
- the attributes of a dog:
	- name
	- color
	- breed
- the behaviors of a dog
	- bark
	- they play fetch
	- move forward, backward, left, and right 

## 0.11.2 - Creating A Class
- "class" statement, creates a class
	- it is a good programming practice to make class's start with a capital letter
		- to differentiate them from functions and modules
```
# this is our "Dog" class
class Dog:
```
- we now need to add our instance variables, these variables will contain the dogs' attributes
	- things like the dogs name and fur color
- "\_\_init\_\_" method, *init*ializes instance variables to the class [init = initialize]
	- this "\_\_init\_\_" method is reffered to as the class constructor
- class methods are structured like functions
- **all methods** in a class take "self" as their first parameter
	- "self" parameter, an access point to the current instance of the class
	- the "self" parameter doesn't actually have to be called self, it's just good practice
```
# this is our "Dog" class
class Dog:

	# init method, takes in the attributes "name" and "color"
	def __init__(self, name, color):
		self.name = name
		self.color = color
```
- we can now add our dog objects
```
duke = Dog("Duke", "White")
sam = Dog("Sam", "Black")
```
- we can output and use the dog object's attributes
```
dog_tuple = (duke, sam)

for dog in dog_tuple:
	print(f"{dog.name} has {dog.color} fur")
	
>>> "Duke has White fur"
>>> "Sam has Black fur"
```

## 0.11.3 - Adding Behaviors
- now that the dog objects have their own attributes, we can give them behaviors like barking or growling
```
# this is our "Dog" class
class Dog:

	# init method, takes in the attributes "name" and "color"
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	# barking method
	def bark(self):
		print("Woof")
		
	# growling method
	def growl(self):
		print("Grrr")

duke = Dog("Duke", "White")
sam = Dog("Sam", "Black")

duke.bark()
sam.growl()

>>> "Woof"
>>> "Grrr"
```
- class's can also have attributes that are only accessible to the class
- created by initializing variables in the class
```
# this is our "Dog" class
class Dog:

	# class specific attribute
	legs = 4

	# init method, takes in the attributes "name" and "color"
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	# barking method
	def bark(self):
		print("Woof")
		
	# growling method
	def growl(self):
		print("Grrr")

duke = Dog("Duke", "White")
sam = Dog("Sam", "Black")

duke.bark()
sam.legs

>>> "Woof"
>>> 4
```

## 0.11.4 - Inheritance
- congrats, the game is sucessful upon it's release
- eventually, people get tired of dogs, they want more animals like cats
- now we could make another entire class for cats, but cat's have the same attributes as dogs, but different behaviours
- for situations like this we can inherit attribues and behaviors from other class's.
---
- a super class is a class that other class's [subclass's] can inherit from
- let's make a super class called "Animal"
```
# this is our super class
class Animal:
```
let's say that all of the animals in our game share these same attributes
- name
- color
- breed
```
# this is our super class
class Animal:
	# intialize our shared attributes
	def __init__(self, name, color, breed):
		self.name = name
		self.color = color
		self.breed = breed	
```
- note that if an object doesn't have attributes or behaviours, you don't need to add them in the blueprint or class
- let's make our animal subclass's
- to inherit from a class, mention the super class's name in parenthesis "()" after the supclass
```
# this is our super class
class Animal:
	# intialize our shared attributes
	def __init__(self, name, color, breed):
		self.name = name
		self.color = color
		self.breed = breed	

# this dog subclass inherits from our "Animal" super class
class Dog(Animal):
	# we only need to initialize anything specific to dogs, no init needed
	
	# barking method
	def bark(self):
		print("Woof")
		
# this cat subclass inherits from our "Animal" super class
class Cat(Animal):
	# we only need to initialize anything specific to cats, no init needed
	
	# purring method
	def purr(self):
		print("Purr")
```
now we can make our animal objects
```
sam = Dog("Same", "Black", "Doberman")
jasper = Cat("Jasper", "White", "American Bobtail")

sam.bark()
jasper.purr()

>>> "Woof"
>>> "Purr"
```
when a subclass inherits from a super class, behaviors or attributes with the same name are overwritten by the subclass
```
# this is our super class
class Animal:
	# intialize our shared attributes
	def __init__(self, name, color, breed):
		self.name = name
		self.color = color
		self.breed = breed	
	
	# superclass speaking method
	def speak(self):
		print("Rawr")

# this dog subclass inherits from our "Animal" super class
class Dog(Animal):
	# we only need to initialize anything specific to dogs, no init needed
	
	# bsubclass speaking method overwrites superclass speaking method
	# because they share the same name
	def speak(self):
		print("Woof")

sam = Dog("Same", "Black", "Doberman")
sam.speak()

>>> "Woof"
```

## 0.11.5 - More Advanced Topics
- OOP [Object Oriented Programming] can get very complicated very quickly
- due to this being a beginner friendly, cybersecurity focused, curriculem we will end the topic of OOP here
- however, CosmodiumCS will be releasing an Advanced level Python course in the near future
	- here we will more advanced topics like generators, recursion, decorators, magic methods [dunders], hiding class data, class and static methods, properties, and more
- until then, I will link some free and open source resources for if you wish to continue learning
```
Tech With Tim, Python OOP - 'https://www.youtube.com/watch?v=JeznW_7DlB0'
W3Schools - 'https://www.w3schools.com/python/python_reference.asp'
```
