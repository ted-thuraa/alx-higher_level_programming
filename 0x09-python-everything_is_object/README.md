# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---

What is an object
Something that exists in computer magic and has an id and is something.


What is the difference between a class and an object or instance
Class is a blueprint, object is the houses built from it, and instance is one
specific house



What is the difference between immutable object and mutable object
immutable cannot be modified or changed. Mutable can.



What is a reference
Kinda like pointers. A variable references an object. It can reference a
different object later with reassignment.



What is an assignment
When you do =.


What is an alias
Another name that points to the same object.



How to know if two variables are identical
Use ==.



How to know if two variables are linked to the same object
Use is.



How to display the variable identifier (which is the memory address in the CPython implementation)
id()



What is mutable and immutable
changable and not changable.



What are the builtin mutable types
List, set, dict.



What are the builtin immutable types
Booleans, integers, float, tuples, strings, frozensets.



How does Python pass variables to functions
By reference.






EXTRA INFO:
we can test is 2 variables have the same value with == but we can also test if
they refer to the same object using is. a==b and a is b.

Strings are immutable in python so it optimaizes resources by refering to the
same string object. This is not the case for lists.

if 2 variables or names refer to the same object, they are aliases. 

clone a list to keep a copy of the original.
