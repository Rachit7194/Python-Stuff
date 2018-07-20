#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","quixom","bookdata" )
print db
# prepare a cursor object using cursor() method
cursor = db.cursor()
print cursor
# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")



# disconnect from server
db.close()