#!/usr/bin/python3

"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument.
"""

import MySQLdb
import sys

def list_states(username, password, db_name, st_name):
    # establishing a secure connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # creating a cursor object to execute SQL queries
    cursor = db.cursor()

    # using format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            st_name)
    cursor.execute(query)

    # fetching all the results
    states = cursor.fetchall()

    # display/print them out
    for state in states:
        if state[1] == st_name:
            print(state)

    # closing the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        exit()
    else:
        list_states(sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4])