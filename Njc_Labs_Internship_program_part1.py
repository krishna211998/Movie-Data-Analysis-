"""
Importing the Mysql connector python package
"""
import mysql.connector

"""
Establishing the connection by passing the Paramaters(host, username, password).
"""
try:
	connection_response=mysql.connector.connect(host="localhost",user="krishna",passwd="AimTcs@21")

	"""
	As MySQL server is running without Error,
	I am Creating a Database named "Movie_Details" 
	and executing the Sql command.
	"""
	create_db_query = "CREATE DATABASE Movie_Details"
	with connection_response.cursor() as cursor:
	    cursor.execute(create_db_query)

	"""
	To see all the Databases located in the server,
	Executing the sql command
	"""
	show_db_query = "SHOW DATABASES"
	with connection_response.cursor() as cursor:
	    cursor.execute(show_db_query)
	    for db in cursor:
	        print(db)
	        
except Exception as e:
	print(e)