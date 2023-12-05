import psycopg2

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

    with open('demographics.csv', 'w') as f:
        for row in cursor:
            f.write("%s\n" % str(row))

    print("CSV file created/updated successfully!")

except psycopg2.Error as e:
    print("Error occurred while connecting to PostgreSQL:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
