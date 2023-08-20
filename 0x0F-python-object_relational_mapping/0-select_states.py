#!/usr/bin/env python3
''' Script to select all the states from a database '''

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC;")
        states = cursor.fetchall()

        for state in states:
            print(state)
            
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
