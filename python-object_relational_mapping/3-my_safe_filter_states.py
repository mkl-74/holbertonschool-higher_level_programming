#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 5:
        print("Usage: {} username password database_name state_name".format(argv[0]))
        exit(1)

    # Connect to the MySQL database
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()

    # Prepare the SQL query with a parameter placeholder
    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"

    # Execute the query with the parameter value passed as a tuple
    cur.execute(query, (argv[4],))

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    conn.close()
