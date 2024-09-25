import sqlite3


def list_tables(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute a query to retrieve the names of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all rows (table names) from the result set
    tables = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Extract table names from the result set and return as a list
    return [table[0] for table in tables]


# Replace 'your_database.db' with the path to your SQLite database file
db_file = 'payroll-test.db'
tables = list_tables(db_file)

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table)
