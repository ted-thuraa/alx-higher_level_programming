#!/usr/bin/python3

def getAllStates(user1, passwd, db1):
    """ gets states and filters as required"""
    import MySQLdb
    conn = MySQLdb.connect(
        user = user1,
        passw = passwd,
        db = db1,
        host = "localhost",
        port = 3306
    )
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE `name` REGEXP BINARY '^N' 
    ORDER BY states.id ASC""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    import sys
    """ protected from executing when imported """
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3])