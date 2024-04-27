#!/usr/bin/python3

"""
Script that lists all State objects that contain the letter `a`
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
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

    # Querying State Objects that contain the letter `a`
    filt_states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()

    # Displaying the results
    for state in filt_states:
        print("{:d}: {:s}".format(state.id, state.name))

    # Closing the session
    session.close()
