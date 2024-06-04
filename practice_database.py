# import pyodbc
# import pandas as pd

# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=10.10.3.57;'
#                       'uid=sa;'
#                       'pwd=NewGrads2024;'
#                       'Database=GB新人研修_イテッパインムー;')

# SERVER = "10.10.3.57"
# DATABASE = "Test"
# DB_USER = "sa"
# DB_PASSWORD = "NewGrads2024"

# Create a cursor object
# Execute a query

# cursor.execute('DELETE FROM [dbo].[mic_拠点] WHERE id = 6')
# cursor.execute('SELECT * FROM [dbo].[mic_拠点]')


# conn.commit() ......実際にデータベースに影響を与える
#conn.close()
# for row in cursor:
#     print(row)

# cursor = conn.cursor()

# df = pd.read_sql("SELECT * FROM [dbo].[mic_拠点]",conn)
# print(df)




import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database connection parameters from environment variables
SERVER = os.getenv("SERVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DATABASE")

print(SERVER)
print(DB_USER)
print(DB_PASSWORD)
print(DATABASE)

# Establish a connection
conn = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={DB_USER};PWD={DB_PASSWORD}")


# Create a cursor object
cursor = conn.cursor()

df = pd.read_sql("SELECT * FROM users",conn)
print(df)


# create_table_query = '''
# CREATE TABLE myTable (
#     ID INT IDENTITY(1,1) PRIMARY KEY,
#     FirstName VARCHAR(50),
#     LastName VARCHAR(50),
#     Gender CHAR(1),
#     BirthDate DATE,
#     Age INT,
#     Department VARCHAR(50),
#     Salary DECIMAL(10, 2),
#     Address VARCHAR(100)
# )
# '''


# grade_list = [
#     {"course":"数学","grade":"60"},
#     {"course":"英語","grade":"70"},
#     {"course":"体育","grade":"65"},
# ]

# Execute queries, fetch data, etc.
# cursor.execute(create_table_query)

# insert_query = '''
# INSERT INTO user (Name, Age)
# VALUES (?, ?)
# '''

# Define the data to be inserted
# data = ('Ei Thet Paing Hmuu', 27)

# Execute the INSERT query
# cursor.execute(insert_query, data)

# cursor.execute("UPDATE users SET Age=37 WHERE ID=3")


# Commit the transaction
# conn.commit()

# Close the connection
conn.close()

