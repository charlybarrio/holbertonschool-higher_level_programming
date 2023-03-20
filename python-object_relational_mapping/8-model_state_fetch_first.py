#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}". format(
        user, pwd, db_name))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")
