#!/usr/bin/python3
"""
A script that lists all State objects that
contain the letter 'a' from the database
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
