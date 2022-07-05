# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---   
Resources:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions
https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf
https://docs.python.org/3/library/json.html
https://automatetheboringstuff.com/
  



How to open a file
f = open('name' , 'permission')

How to write text in a file
f.write("stuff\n")

How to read the full content of a file
f.read()
d.readlines()


How to read a file line by line
f.readline()

How to move the cursor in a file
f.seek()


How to make sure a file is closed after using it
use with so...
with open('file', 'r') as f:
    stuff...
f.closed


What is and how to use the with statement
with. allows stuff without the try except stuff. 
\_\_enter\_\_ is invoked, \_\_exit\_\_ is loaded for later use


What is JSON
Javascript object notation. data. 

What is serialization
pickling. a process where a python object heirarchy is converted into a byte stream.
also known as pickle module, marshalling, flattening.

What is deserialization
unpickling. the opposite of serialization. a byte stream is converted back into an object heirarchy. 


How to convert a Python data structure to a JSON string
take massive json dumps.

How to convert a JSON string to a Python data structure
load it. take all the loads. big hot loads. load the massive object. 
