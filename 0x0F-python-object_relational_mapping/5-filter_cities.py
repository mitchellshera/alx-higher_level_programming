#!/usr/bin/python3
'''
A script that takes in an argument and displays
all values where name matches the argument
'''

import MySQLdb
import sys


def filter_cities_by_state():
    '''Lists cities of the given state name'''
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
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC;
        """
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        if cities:
            city_names = ', '.join([city[0] for city in cities])
            print(city_names)

        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == '__main__':
    filter_cities_by_state()
