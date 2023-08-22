#!/usr/bin/python3
""" 
 a script that lists all State objects,
 and corresponding City objects, contained in the database
"""

if __name__ == "__main__":

    import sys
    from relationship_city import Base, City
    from relationship_state import State
    from sqlalchemy.schema import Table
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    for state in s.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    s.close()
