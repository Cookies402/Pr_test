import mysql.connector

def connect_to_database():
    # Replace the placeholder values with your actual MySQL database information
    return mysql.connector.connect(
        host="your_mysql_host",
        user="your_mysql_username",
        password="your_mysql_password",
        database="users"
    )

def create_user_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS user_info (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

def sign_up(username, password):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        create_user_table(cursor)

        # Check if the username already exists
        cursor.execute("SELECT * FROM user_info WHERE username = %s", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already exists. Please choose another username.")
        else:
            # Insert new user into the database
            cursor.execute("INSERT INTO user_info (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            print("Sign-up successful. You can now log in.")
    
    finally:
        cursor.close()
        connection.close()

def login(username, password):
    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        create_user_table(cursor)

        # Check if the username and password match
        cursor.execute("SELECT * FROM user_info WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            print("Login successful.")
        else:
            print("Invalid username or password. Please try again.")
    
    finally:
        cursor.close()
        connection.close()

# Example usage:
# sign_up("john_doe", "password123")
# login("john_doe", "password123")
