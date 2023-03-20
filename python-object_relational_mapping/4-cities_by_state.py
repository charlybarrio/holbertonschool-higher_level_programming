#!/usr/bin/python3
"""
displays all values in the states where name matches the argument
And is safe from MySQL injections!
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name)

    # Exectute the query
    cur = db.cursor()

    cur.execute("""SELECT cities.id, cities.name, states.name 
                FROM cities LEFT JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")

    # fetchall statement select the data of the tables
    records = cur.fetchall()

    for element in records:
        print(element)
