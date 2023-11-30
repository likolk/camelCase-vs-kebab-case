# this file will be used to export the postgresql table onto a csv file, as required.
import psycopg2, csv
from dotenv import load_dotenv
import os

load_dotenv()

# connect to the database
conn = psycopg2.connect(
    host="dpg-cljgru6g1b2c73apkn90-a.frankfurt-postgres.render.com",
    database= "exp02",
    user= "kelvin",
    password="8r9aws8VsQyRxv3a9vcqB9PFcA6VUKYz",
    port="5432"
)

# create a cursor
cursor = conn.cursor()

# fetch all the table content
cursor.execute("SELECT * FROM myapp_demographics")

# store into demographics.csv file
with open('demographics.csv', 'w') as f:
    for row in cursor:
        f.write("%s\n" % str(row))

# close connection and cursor
cursor.close()
conn.close()







