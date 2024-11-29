import sqlite3
import pandas as pd

# Create a connection to a database called database.db
conn = sqlite3.connect('database.db')

# Function to read SQL query results into a pandas DataFrame
def read_sql():
    query = "SELECT * FROM orders"
    # Use pandas to execute the query and load the results into a DataFrame
    df = pd.read_sql_query(query, conn)
    return df

# Example usage
# df = read_sql()
# print(df)

# Close the connection when done
# conn.close()
