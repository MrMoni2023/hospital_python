import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='Mazam900', host='localhost', database='example')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
   "INSERT INTO new(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
   "VALUES (%s, %s, %s, %s, %s)"
)
data = ('Moni', 'Kashif', 22, 'M', 500000)

try:
   # Executing the SQL command
   cursor.execute(insert_stmt, data)
   
   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()