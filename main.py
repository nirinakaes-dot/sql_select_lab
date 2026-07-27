import os
import sqlite3
import pandas as pd

# STEP 1A
# Import SQL Library and Pandas (done above)

# STEP 1B
# Connect to the database
db_path = os.path.join(os.path.dirname(__file__), 'data.sqlite')
conn = sqlite3.connect(db_path)

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Employee number and last name, for all employees
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees;
""", conn)


# STEP 3
# Same as Step 2, but lastName comes before employeeNumber
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees;
""", conn)


# STEP 4
# Same as Step 3, but alias employeeNumber as 'ID'
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees;
""", conn)


# STEP 5
# CASE: President/VP Sales/VP Marketing -> Executive, else Not Executive
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
""", conn)


# STEP 6
# Length of last name for all employees
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
""", conn)


# STEP 7
# First two letters of job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
""", conn)


# STEP 8
# Sum of total price across all order line items
sum_total_price = pd.read_sql("""
    SELECT SUM(quantityOrdered) AS total_price
    FROM orderdetails;
""", conn).iloc[0]


# STEP 9
# Break out order date into day/month/year
df_day_month_year = pd.read_sql("""
    SELECT orderNumber,
           orderDate AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders;
""", conn)