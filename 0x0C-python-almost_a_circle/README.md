# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---   

## Each scripts   
* Script 0 - .    
* Script 0 - This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs).


* Script 1 - Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.


* Script 3 - .  
* Script 4 - .  
* Script 5 - .  
* Script 6 - .  
* Script 7 - .  
* Script 7 - This type of argument is called a “no-keyword argument” - Argument order is super important.


* Script 8 - This type of argument is called a “key-worded argument”. Argument order is not important.


* Script 9 - As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.


* Script 11 - .  
* Script 12 - .  
* Script 13 - .  
* Script 14 - .  
* Script 15 - .  
* Script 16 - .  
* Script 17 - .  
* Script 18 - .  
* Script 19 - .  
* Script 20 - .  
* Script 21 - .  
* Script 100 - .    
* Script 101 - .    
* Script 102 - .    
* Script 103 - .    








What is Unit testing and how to implement it in a large project
Unit testing is testing one specific cast. A unit. How we do dis?
https://www.pythonsheets.com/notes/python-tests.html



How to serialize and deserialize a Class
We can use pickle. Fornat and protocols. Which serialization scheme can
determine many things.
How fast the program is, how secure it is, how much freedom I have while
maintenance, how well it will communicate with other systems.
Use pickle, dump, dumps, load, and loads. 
dump() serializes into a string and load() deserializes from an open file-like
object. 
load() deserializes froma string.
Here is nice resource
https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183
First we load,
variable = pickle.loads("(string)")
Unpickle with assert variable\_name = parameter


How to write and read a JSON file
JSON module also has dumps, dump, load, loads. 
We need to use a CustomEncoder class for Json stuff and json.JSONEncoder.
https://docs.python.org/3/library/json.html


What is \*args and how to use it
args is a magic variable. args is used to send non keyworded variable length
argument list.
args is like ... or variadic functions. eg.
def test\_args(f\_arg, \*argv):
https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/


What is \*\*kwargs and how to use it
kwargs allows passed keyworded variable length arguments. Use this if i want to
handle named arguments into a function
eg. 
def greet\_me(\*\*kwargs):
So use this when i ass in some keyword parameters like list and a list or name
stuff.


How to handle named arguments in a function
kwags. 
some\_func(fargs,\*args,\*\*kwargs)









Other info/ concepts this project covers:

Import

Exceptions

Class

Private attribute

getter/setter

class method

static method

inheritance

unittest

read/write file
