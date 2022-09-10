#!/usr/bin/pyhon3
def getAllStates(user2, passward2, db2, uinput):
    """ script that gets all the states when called on """
    import MySQLdb
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user2,
            passwd=passward2,
            db=db2
    )
    cur = conn.cursor()
    cmd = """SELECT * FROM states WHERE `name` = %s ORDER BY
        states.id ASC"""
    cur.execute(cmd, (uinput,))
    row_states = cur.fetchall()
    for row in row_states:
        print(row)
    cur.close()
    conn.close()
    
if __name__ == "__main__":
    import sys
    """main entry"""
    getAllStates(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
