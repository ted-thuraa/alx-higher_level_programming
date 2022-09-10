#!/usr/bin/python3
"""main entry"""
if __name__ == '__main__':
    import sys
    import MySQLdb
    # Connect to an existing database
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Execute a command: this grabs all states in the table
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
