
#!/usr/bin/python3
"""
    Get the states begin by user input of a data base avoiding SQL injection
"""
import MySQLdb
from sys import argv


def main():
    """Only executes when is not imported"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])
    c = db.cursor()
    command = """SELECT *
                 FROM states
                 WHERE BINARY states.name = %s
                 ORDER BY states.id ASC"""
    numrows = c.execute(command, (argv[4],))
    states = c.fetchall()
    for idstate in states:
        print(idstate)

if __name__ == "__main__":
    main()
