import psycopg2
import csv

try:
    conn = psycopg2.connect(
        host="dpg-clniht5e89qs739ga8jg-a.frankfurt-postgres.render.com",
        database="exp02_emd1",
        user="kelvin",
        password="sKiMWw1Lfiy1Zr2EcFFlCMEhw8bBS0Vz",
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
    try:
        if cursor:
            cursor.close()
    except NameError:
        pass  # Cursor was not defined

    try:
        if conn:
            conn.close()
    except NameError:
        pass  # Connection was not defined
