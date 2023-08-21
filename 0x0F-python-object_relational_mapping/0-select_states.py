#!/usr/bin/python3
''' Script to select all the states from a database '''

import MySQLdb
import sys


def show():
    '''
    Gets MySQL username, password and database from the user input
    '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    host = 'localhost'
    port = 3306

    '''connect to the database given '''
    conn = MySQLdb.connect(host=host, port=port, user=username,
                           password=password, db=database)

    ''' A cursor object '''
    cursor = conn.cursor()

    '''
    SELECT statement that gets all states from database
    '''
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

    ''' Print the results found '''
    for row in cursor:
        print(row)

    ''' Close the connection '''
    conn.close()


if __name__ == '__main__':
    show()
