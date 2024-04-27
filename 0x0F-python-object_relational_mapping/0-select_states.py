#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa.
Parameters for script: mysql username, mysql password, database name.
"""

import MySQLdb
# from sys import argv
import sys

# if __name__ == '__main__':
def list_states(username, password, db_name):
    # establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
        # passwd=argv[2],
        # user=argv[1],
        # db=argv[3]
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # executing the cursor to retrieve states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetching all the results
    states = cursor.fetchall()

    # display/print them out
    for state in states:
        print(state)

    # closing the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1],
                    sys.argv[2],
                    sys.argv[3])
