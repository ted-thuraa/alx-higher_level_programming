# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---   

Resources:

https://docs.python.org/3/tutorial/classes.html#inheritance

https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

https://www.packt.com/inheritance-python/

https://www.youtube.com/watch?v=d8kCdLCi6Lk


What is a superclass, baseclass or parentclass
The outer, upper, heigher class..


What is a subclass
The class that is derived from the superclass, so the base or child class. Extended class in Java. Derived class.

How to list all attributes and methods of a class or instance
className.\_\_dict\_\_


When can an instance have new attributes
WHen you declare them in the subclass's init.


How to inherit class from another
class DerivedClassName(BaseClassName):


How to define a class with multiple base classes
class DerivedClassName(Base1, Base2, Base3):
inheritance is done as a depth first search from left to right.



What is the default class every class inherit from
classic class. in python 2 classic classes have no common root and do not inherit from any.
in python3, all classes are new style and inherit implicityly from object.
google old style and new style classes python.


How to override a method or attribute inherited from the base class
just redefine the def with the same name.


Which attributes or methods are available by heritage to subclasses
All of them.


What is the purpose of inheritance
What is the purpose of children or a tree or life?
Inherit, save code and effort, be smart.

What are, when and how to use isinstance, issubclass, type and super built-in functions
isinstance returns a boolean. is subclass returns a boolean. Type returns the data type.
super returns a proxy object that method calls a parent which is useful to access inherited stuff that were overridden. getattr() is also useful.
