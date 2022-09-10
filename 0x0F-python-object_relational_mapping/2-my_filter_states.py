#!/usr/bin/python3
def getAllStates(user2, passwd2, db2, input):
    import MySQLdb
    conn = MySQLdb.connect(
        user = user2,
        passwd = passwd2,
        pd = db2,
        host = "localhost",
        port = 3306
    )
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY `name` = "{}" ORDER BY states.id ASC""".format(input))
    row_states = cur.fetchall()
    for row in row_states:
        print(row)
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    """main entry"""
    import sys
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]) 