import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=4006,
        user="maxuser",
        password="maxpwd",
        database="test"        # Tests if  this database exists
    )

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")  # Test query

    for table in cursor:
        print(table)

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
