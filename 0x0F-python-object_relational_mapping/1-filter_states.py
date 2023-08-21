#!/usr/bin/python3
''' Script to select all the states from a database
that start with N '''

import MySQLdb
import sys


def filter_states_with_n():
    '''Lists all states with names starting with N'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    try:
        db = MySQLdb.connect(host=host, user=username, passwd=password,
                             db=db_name, port=port)
        cur = db.cursor()
        cur.execute('SELECT * FROM states WHERE name LIKE "N%" ' +
                    'ORDER BY states.id ASC')
        result = cur.fetchall()
        cur.close()
        db.close()
        
        for state in result:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    filter_states_with_n()
