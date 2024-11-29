import sqlite3

# Create a connection to a database called database.db
conn = sqlite3.connect('database.db')

# Create a cursor to perform database operations
cursor = conn.cursor()

# Create the orders table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_number INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    total REAL NOT NULL
)
''')
conn.commit()

# Function to insert a row into the orders table
def insert_row(order_number, customer_name, total):
    cursor.execute(
        "INSERT INTO orders (order_number, customer_name, total) VALUES (?, ?, ?)",
        (order_number, customer_name, total)
    )
    conn.commit()

# Function to select all data from the orders table
def select_all_data():
    cursor.execute("SELECT * FROM orders")
    return cursor.fetchall()

# Function to insert multiple rows of data
def insert_data(data):
    cursor.executemany(
        "INSERT INTO orders (order_number, customer_name, total) VALUES (?, ?, ?)",
        data
    )
    conn.commit()

# Function to update the total for a specific order_number
def update_data(order_number, total):
    cursor.execute(
        "UPDATE orders SET total = ? WHERE order_number = ?",
        (total, order_number)
    )
    conn.commit()

# Function to delete a specific row by order_number
def delete_data(order_number):
    cursor.execute(
        "DELETE FROM orders WHERE order_number = ?",
        (order_number,)
    )
    conn.commit()

# Example usage:
# insert_row(1, "John Doe", 150.75)
# print(select_all_data())
# insert_data([(2, "Jane Smith", 200.50), (3, "Alice Johnson", 300.75)])
# update_data(2, 220.00)
# delete_data(1)
# print(select_all_data())

# Close the connection when done
# conn.close()
