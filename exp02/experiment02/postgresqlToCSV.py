# this file will be used to export the postgresql table onto a csv file, as required.
import psycopg2, csv
from dotenv import load_dotenv
import os

load_dotenv()

# connect to the database
conn = psycopg2.connect(
    host=os.getenv("HOST"),
    database= os.getenv("NAME"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    port=os.getenv("PORT"),
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







