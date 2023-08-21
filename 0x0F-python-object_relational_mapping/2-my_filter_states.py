#!/usr/bin/python3
'''
A script that takes in an argument and displays 
all values where name matches the argument '''

import MySQLdb
import sys


def display_tables():
    '''displays values where name matches arg '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    display_tables()
