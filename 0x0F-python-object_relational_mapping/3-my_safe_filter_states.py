#!/usr/bin/python3
"""
List all values in the states table of hbtn_0e_0_usa
where name matches the argument. This script is safe
from MySOL injections.
"""

import MySQLdb
import sys

# When imported, code should not execute
if __name__ == "__main__":
    # Connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # Enables multiple separate working environments
    # using same database connection
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
                name = %s ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
        # Clean up process
    cur.close()
    db.close()
