# Aaron Henson
# CNE 370 - Introduction to Virtualization
# Spring 2025
# amhenson@student.rtc.edu
# This script will connect to the MaxScale instance and run SQL queries

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # Or you can use your VM IP like "192.168.1.13"
        port=4006,
        user="maxuser",
        password="maxpwd"
        # No database is specified, because MaxScale uses schemarouter
    )

    cursor = conn.cursor()

    print("Largest zipcode in zipcodes_one:") # For the largest zipcode in zipcodes_one
    cursor.execute("SELECT MAX(Zip) FROM zipcodes_one.zipcodes_one;")
    for row in cursor:
        print("  Max Zipcode:", row[0])
    print()

    print("All zipcodes where state = 'KY':") # All zipcodes where state = 'KY'
    cursor.execute("""
        SELECT Zip, State, City, TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'KY'
        UNION
        SELECT Zip, State, City, TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'KY';
    """)
    for row in cursor:
        print(" ", row)
    print()

    print("All zipcodes between 40000 and 41000:")
    cursor.execute("""
        SELECT Zip, State, City, TotalWages FROM zipcodes_one.zipcodes_one WHERE Zip BETWEEN 40000 AND 41000
        UNION
        SELECT Zip, State, City, TotalWages FROM zipcodes_two.zipcodes_two WHERE Zip BETWEEN 40000 AND 41000;
    """)
    for row in cursor:
        print(" ", row)
    print()

    print("TotalWages where state = 'PA':")
    cursor.execute("""
        SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA'
        UNION
        SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA';
    """)
    for row in cursor:
        print("  TotalWages:", row[0])

    # Clean up
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
