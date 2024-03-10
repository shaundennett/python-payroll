import mysql.connector

def select_users_by_surname(surname):
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="payroll"
        )

        # Create cursor
        cursor = conn.cursor()

        # Define query with placeholder for surname
        query = "SELECT * FROM User WHERE lastname = %s"

        # Execute query with parameter
        cursor.execute(query, (surname,))

        # Fetch and print results
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Input the surname to search for
    surname = input("Enter surname: ")

    # Call function to select users by surname
    select_users_by_surname(surname)
