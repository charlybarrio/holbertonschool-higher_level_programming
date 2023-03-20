#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
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
    results = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    for result in results:
        print("{}: {}".format(result.id, result.name))
