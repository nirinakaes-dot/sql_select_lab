# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("database.db")  # update this file name to your actual SQLite database

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql_query(
    "SELECT * FROM employees LIMIT 5",
    conn,
)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql_query(
    "SELECT * FROM employees ORDER BY EmployeeID DESC LIMIT 5",
    conn,
)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql_query(
    "SELECT EmployeeID AS employee_id, FirstName AS first_name, LastName AS last_name, Title AS job_title FROM employees LIMIT 5",
    conn,
)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql_query(
    "SELECT * FROM employees WHERE Title LIKE '%Executive%'",
    conn,
)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql_query(
    "SELECT EmployeeID, FirstName, LastName, LENGTH(FirstName || ' ' || LastName) AS name_length FROM employees",
    conn,
)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql_query(
    "SELECT * FROM employees WHERE LENGTH(Title) <= 20",
    conn,
)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql_query(
    "SELECT SUM(UnitPrice * Quantity) AS total_price FROM order_items",
    conn,
).iloc[0, 0]

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql_query(
    "SELECT OrderID, OrderDate, strftime('%d-%m-%Y', OrderDate) AS day_month_year FROM orders",
    conn,
)