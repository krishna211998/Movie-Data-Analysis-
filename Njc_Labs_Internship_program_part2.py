"""
Importing the Mysql connector python package
"""
import mysql.connector

"""
as we have created the database , we need to connect the Database.
for that, i will supplement the connect call with a parameter
Movie_Details Databse
"""
try:
	"""
	Establishing the connection by passing the additional database name.
	"""
	connection_response=mysql.connector.connect(host="localhost",user="krishna",passwd="AimTcs@21",database="Movie_Details")

	"""
	Creating The table named movie
	"""
	create_movie_table_with_query = """
	CREATE TABLE movie(
	    id INT AUTO_INCREMENT PRIMARY KEY,
	    movie_name VARCHAR(100),
	    lead_actor VARCHAR(100),
	    lead_actress VARCHAR(100),
	    year_of_release YEAR(4),
	    director_name VARCHAR(100)
	)
	"""
	with connection_response.cursor() as cursor:
	    cursor.execute(create_movie_table_with_query)
	    connection_response.commit()

	"""
	Insert the Values into movie table
	"""
	insert_movie_with_query = """
	INSERT INTO movie (movie_name, lead_actor, lead_actress, year_of_release, director_name)
	VALUES
	    ("M.S. Dhoni: The Untold Story", "Sushant Singh Rajput", "Disha Patani", 2016, "Neeraj Pandey"),
	    ("3 Idiots", "Aamir Khan", "Kareena Kapoor", 2009, "Rajkumar Hirani"),
	    ("joker", "Joaquin Phoenix", "Zazie Beetz", 2019, "Todd Phillips"),
	    ("Lagaan", "Aamir Khan", "Gracy Singh", 2001, "Ashutosh Gowariker"),
	    ("Mary Kom", "Darshan Kumaar", "Priyanka Chopra", 2014, "Omung Kumar"),
	    ("Bhaag Milkha Bhaag", "Farhan Akhtar", "sonam kapoor", 2013, "Rakeysh Omprakash Mehra"),
	    ("The Wolf of Wall Street", "Leonardo DiCaprio", "Margot Robbie", 2014, "Martin Scorsese")  
	"""
	with connection_response.cursor() as cursor:
	    cursor.execute(insert_movie_with_query)
	    connection_response.commit()

	"""
	Retriving all the details row wise stored in the movie table
	using select sql query
	"""
	select_movies_query = "SELECT * FROM movie"
	with connection_response.cursor() as cursor:
	    cursor.execute(select_movies_query)
	    for row in cursor.fetchall():
	        print(row)

	"""
	Get movie_name by passing lead_actor as parameter
	"""
	select_movies_query = """
	SELECT movie_name FROM movie where lead_actor="Aamir Khan"
	"""
	with connection_response.cursor() as cursor:
	    cursor.execute(select_movies_query)
	    for row in cursor.fetchall():
	        print(row)

except Exception as e:
	print(e)

