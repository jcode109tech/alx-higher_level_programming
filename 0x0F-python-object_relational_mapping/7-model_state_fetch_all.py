#!/usr/bin/python3

"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string (engine for database)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all State objects, sorted by id
    # Displaying the results
    for state in session.query(State).order_by(State.id).all():
        print("{:d}: {:s}".format(state.id, state.name))

    # Closing the session
    session.close()
