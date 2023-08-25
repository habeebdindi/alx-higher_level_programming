#!/usr/bin/python3
"""
Script lists state that that matches a string from the db hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    """
    function to that runs everything
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    match = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name \
            LIKE '{}%' ORDER BY id ASC".format(match)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
