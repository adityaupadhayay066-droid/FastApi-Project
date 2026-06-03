import mysql.connector 
from dotenv import load_dotenv
import os 

load_dotenv()
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cur = conn.cursor()

cur.execute("CREATE DATABASE IF  NOT EXISTS Notes")
cur.execute("USE Notes")

# cur.execute("DROP TABLE IF  EXISTS User_record")
# cur.execute(""" 
#     CREATE TABLE user_record(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         Work_type VARCHAR(50),
#         Content VARCHAR(200),
#             Creation DATE
#     )
# """)
cur.execute("SELECT * FROM User_record")
data = cur.fetchall()
print(data)