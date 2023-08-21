#!/usr/bin/python3
'''
A script that takes in an argument and displays 
all values where name matches the argument '''

import MySQLdb
import sys


def filter_states_by_name():
    '''Displays values where name matches the argument'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    try:
        conn = MySQLdb.connect(host=host,
                               port=port,
                               user=username,
                               passwd=password,
                               db=database)

        cursor = conn.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()

        ''' Print the results '''
        for state in results:
            print(state)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == '__main__':
    filter_states_by_name()
