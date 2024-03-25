#!/usr/bin/python3
"""Lists cities of a given state"""

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

    # Prepare the SQL query
    query = """
    SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    # Execute the query
    cur.execute(query, (argv[4],))

    # Fetch and display the result
    result = cur.fetchone()
    if result[0]:
        print(result[0])
    else:
        print("No cities found for the given state.")

    # Close the cursor and the database connection
    cur.close()
    conn.close()
