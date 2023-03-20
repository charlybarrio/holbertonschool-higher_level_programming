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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name)

    # Exectute the query
    cur = db.cursor()

    cur.execute("""SELECT * FROM states
                WHERE name LIKE %s
                ORDER BY states.id ASC""", (state_name,))

    # fetchall statement select the data of the tables
    records = cur.fetchall()

    for element in records:
        print(element)
