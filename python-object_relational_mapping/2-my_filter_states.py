#!/usr/bin/python3
"""
displays all values in the states table where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name)

    # Exectute the query
    cur = db.cursor()

    query = ("""SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC""".format(state_name))
    cur.execute(query)

    # fetchall statement select the data of the tables
    records = cur.fetchall()

    for element in records:
        print(element)
