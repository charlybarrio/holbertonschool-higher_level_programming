#!/usr/bin/python3
"""
name of a state as an argument and lists all cities of that state
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

    cur.execute("""SELECT cities.name
                FROM cities JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY '{}'
                ORDER BY cities.id ASC""".format(state_name,))

    # fetchall statement select the data of the tables
    records = cur.fetchall()

    for i, element in enumerate(records):
        if i != 0:
            print(", ", end="")
        print(element[0], end="")
    print()
