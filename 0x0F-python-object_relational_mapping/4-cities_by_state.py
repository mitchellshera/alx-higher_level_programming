#!/usr/bin/python3
'''
A script that takes in an argument and displays
all values where name matches the argument
'''

import MySQLdb
import sys


def list_all():
    '''lists all cities from db'''
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host, user=username, passwd=password,
                         db=db_name, port=port)
    c = conn.cursor()
    c.execute('SELECT c.id, c.name, s.name FROM cities c LEFT ' +
                'JOIN states s ON c.state_id = s.id ORDER BY c.id ASC;')
    result = c.fetchall()
    c.close()
    conn.close()

    if result:
        for city in result:
            print(city)


if __name__ == '__main__':
    list_all()
