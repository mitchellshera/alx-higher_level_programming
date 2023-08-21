#!/usr/bin/python3
''' Script to select all the states from a database
that start with N '''

import MySQLdb
import sys


def lists_N():
    '''lists all states with a name that starts with N'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name regexp "^N.*" ' +
                'ORDER BY states.id ASC')
    result = cur.fetchall()
    cur.close()
    db.close()
    if result:
        for state in result:
            if state[1][0] == "N":
                print(state)


if __name__ == "__main__":
    lists_N()
