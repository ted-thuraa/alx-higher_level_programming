# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---  

**How to connect to a MySQL database from a Python script?**  
*MySQLdb module with SQLAlchemy.
Without ORM: Can connect and use cursor then execute a query then fetchall then print all and close the cursor and the connection.
Or we can use ORM to create an engine and create the base metadata from the engine and then have a session and then loop through each object in the db table. then just close the session.*   

**How to SELECT rows in a MySQL table from a Python script?**  
*No ORM: open a database connection, prepare a cursor object using cursor() method, execute the SQL query using execute() method, fetch all of the rows from the query, close cursor objects and the connection.
Select rows by execute.
Using an ORM: we create an engine that generates a queue pool. Make the base class and those columns will be mapped to the proper classes. We .select() and then we can .where() then execute that.*  

**How to INSERT rows in a MySQL table from a Python script?**  
*Pretty nuch like this:
\# insert data via insert() construct
ins = table.insert().values(
      l_name='Hello',
      f_name='World')
conn = engine.connect()
conn.execute(ins)
*   

**What ORM means?**  
*Object Relational Mapping.*   

**How to map a Python Class to a MySQL table?**  
*Declarative base class. Mapping.*   


## Each scripts and their output  
* Script 0 - Write a script that lists all states from the database hbtn_0e_0_usa.  
* Script 1 - Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.  
* Script 2 - Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.  
* Script 3 - ... write one that is safe from MySQL injections!    
* Script 4 - Write a script that lists all cities from the database hbtn_0e_4_usa.    
* Script 5 - Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.    
* Script 6 - Write a python file that contains the class definition of a State and an instance Base = declarative_base().    
* Script 7 - Write a script that lists all State objects from the database hbtn_0e_6_usa.    
* Script 8 - Write a script that prints the first State object from the database hbtn_0e_6_usa.    
* Script 9 - Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa    
* Script 10 - Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.    
* Script 11 - Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.    
* Script 12 - Write a script that changes the name of a State object from the database hbtn_0e_6_usa.    
* Script 13 - Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.    
* Script 14 - Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.    
* Script 100 - Write a program that prints the opcodes of its own main function.    
