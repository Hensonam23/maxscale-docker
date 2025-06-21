# Aaron Henson
# CNE 370 - Introduction to Virtualization
# Spring 2025
# amhenson@student.rtc.edu
# This script will connect to the MaxScale instance and run SQL queries

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",  # Or you can use your VM IP ("192.168.1.13")
        port=4006,
        user="maxuser",
        password="maxpwd"
        # No database is specified, because MaxScale uses schemarouter
    )

    cursor = conn.cursor()

    print("Largest zipcode in zipcodes_one:") # For the largest zipcode in zipcodes_one
    cursor.execute("SELECT MAX(Zipcode) FROM zipcodes_one.zipcodes_one;")
    for row in cursor:
        print("  Max Zipcode:", row[0])
    print()

    print("All zipcodes where state = 'KY':") # All zipcodes where state is 'KY'

    # First query from shard1
    cursor.execute("SELECT Zipcode, State, City, TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'KY';")
    results = cursor.fetchall()

    # Second query from shard2
    cursor.execute("SELECT Zipcode, State, City, TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'KY';")
    results += cursor.fetchall()

    for row in results:
        print(" ", row)
    print()

    print("All zipcodes between 40000 and 41000:") # All zipcodes between 40000 and 41000

    # First query from shard1
    cursor.execute("SELECT Zipcode, State, City, TotalWages FROM zipcodes_one.zipcodes_one WHERE Zipcode BETWEEN 40000 AND 41000;")
    results = cursor.fetchall()

    # Second query from shard2
    cursor.execute("SELECT Zipcode, State, City, TotalWages FROM zipcodes_two.zipcodes_two WHERE Zipcode BETWEEN 40000 AND 41000;")
    results += cursor.fetchall()

    for row in results:
        print(" ", row)
    print()

    print("TotalWages where state = 'PA':") # The totalWages if state is 'PA'

    # First query from shard1
    cursor.execute(
        "SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE State = 'PA' AND TotalWages IS NOT NULL AND TotalWages != '';")
    results = cursor.fetchall()

    # Second query from shard2
    cursor.execute(
        "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE State = 'PA' AND TotalWages IS NOT NULL AND TotalWages != '';")
    results += cursor.fetchall()

    for row in results:
        print("  TotalWages:", row[0])

    # Clean up
    cursor.close()
    conn.close()

    print("\n+++ Machine Spirit appeased. But still hungers for more queries... more souls. +++")

except mysql.connector.Error as err:
    print(f"Error: {err}")