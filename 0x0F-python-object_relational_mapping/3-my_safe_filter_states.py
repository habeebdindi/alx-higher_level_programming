#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
-now safe from MySQL injections
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name=%s
                ORDER BY states.id ASC""", (argv[4],))
    states = cur.fetchall()
    for row in states:
        print(row)
