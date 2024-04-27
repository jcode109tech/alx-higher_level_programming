#!/usr/bin/python3

"""
Script that prints the frist State object from the database hbtn_0e_6_usa.
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

    # Querying first State object
    state = session.query(State).order_by(State.id).first()

    # Displaying the result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Closing the session
    session.close()
