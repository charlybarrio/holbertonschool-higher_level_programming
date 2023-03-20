#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connect with MySQL database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}". format(
        user, pwd, db_name))

    # Create tables in the engine
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states from the database
    results = session.query(State).all()

    # Print the results
    for element in results:
        print("{}: {}".format(element.id, element.name))

    session.close()
