import pyodbc
import sqlite3
import csv
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

SERVER =os.getenv("SERVER")
DATABASE =os.getenv("DATABASE")
DB_USER =os.getenv("DB_USER")
DB_PASSWORD =os.getenv("DB_PASSWORD")

# print(SERVER)


# df = pd.read_csv("./mymoviedb.csv",lineterminator="\n")
# Open the CSV file for reading
# with open('mymoviedb.csv', 'r') as file:

#     # Create a CSV reader object
#     #reader = csv.reader(file)
#     reader = csv.reader('mymoviedb.csv')

#     # Skip the header row if it exists
#     next(reader)

#     # Iterate over the rows in the CSV file
#     for row in reader:
#         # Execute an SQL INSERT statement to insert the data into the database
#         cursor.execute('''INSERT INTO movies (Release_Date, Title, Overview, Popularity, Vote_Count, Vote_Average, Original_Language, Genre, Poster_Url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
# ,row.Release_Date, row.Title, row[3], row[4], row[5], row[6], row[7], row[8], row[9])

df = pd.read_csv("./mymoviedb.csv",lineterminator="\n")

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={DB_USER};PWD={DB_PASSWORD}')

cursor = conn.cursor()


# for row in df.itertuples():
#     cursor.execute(
#         """
#         INSERT INTO movies (Release_Date, Title, Overview, Popularity, Vote_Count, Vote_Average, Original_Language, Genre, Poster_Url)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """,
#         row.Release_Date,
#         row.Title,
#         row.Overview,
#         row.Popularity,
#         row.Vote_Count,
#         row.Vote_Average,
#         row.Original_Language,
#         row.Genre,
#         row.Poster_Url
#     )

df = pd.read_sql("SELECT * FROM movies",conn)
print(df)

# Commit the transaction
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()