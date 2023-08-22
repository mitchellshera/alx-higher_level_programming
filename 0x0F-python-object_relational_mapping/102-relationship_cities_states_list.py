#!/usr/bin/python3
""" Script that lists all City
objects from the database hbtn_0e_101_usa """

if __name__ == "__main__":

    import sys
    from relationship_city import Base, City
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
    for city in s.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    s.close()
