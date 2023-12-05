import psycopg2
import csv

try:
    conn = psycopg2.connect(
        host="dpg-cljgru6g1b2c73apkn90-a.frankfurt-postgres.render.com",
        database="exp02",
        user="kelvin",
        password="8r9aws8VsQyRxv3a9vcqB9PFcA6VUKYz",
        port="5432"
    )


    cursor = conn.cursor()

    cursor.execute("SELECT * FROM myapp_demographics")

    rows = cursor.fetchall()

    with open('demographics.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([desc[0] for desc in cursor.description])  
        csv_writer.writerows(rows)  

    print("CSV file created/updated successfully!")

except psycopg2.Error as e:
    print("Error occurred while connecting to PostgreSQL:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
