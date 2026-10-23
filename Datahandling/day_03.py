"""
This is the Personal Movie Tracker application.
"""
import json
from json import JSONDecodeError


def addNewMovie():
	try:
		title = input("Give the title of the movie: \n")
		genre = input("Genre of the movie: \n")
		rating = input("Rating of the movie: \n")

		new_data = {
			"title": title,
			"genre": genre,
			"rating": rating
		}
		try:
			with open("movie.json", "r") as file:
				data = file.read().strip()
				movies = json.loads(data) if data else []
		except FileNotFoundError:
			movies = []
			print("The file is not available!!")
		except JSONDecodeError:
			movies = []
			print("The data cannot be decoded to json!!")

		for movie in movies:
			if movie["title"].lower() == title.lower():
				print(f"Movie with the title {title}, already exists!")
				return
			 
		movies.append(new_data)

		with open("movie.json", "w") as file:
			json.dump(movies, file, indent=4)

		print("Movie added Successfully")

	except Exception as e:
		print(f"An unexpected error occurred!{e}")

def viewAllMovies():
	try:
		with open("movie.json", "r") as file:
			content = file.read()
			print(content)
	except FileNotFoundError:
		print("The file is not available!!")
	except JSONDecodeError:
		print("The data cannot be decoded to json!!")

def searchMovies():
	query = input("Enter the title or genre to search the movie: ")
	try:
		with open("movie.json", "r") as file:
			content = file.read().strip()
			movies = json.loads(content) if content else []

		results = [
			movie for movie in movies
			if query.lower() in movie["title"].lower()
			or query.lower() in movie["genre"].lower()
		]

		if results:
			print(results)
		else:
			print("No movies found matching your search.")
		
	except FileNotFoundError:
		print("The file is not available!!")
	except JSONDecodeError:
		print("The data cannot be decoded to json!!")
		

def showOptions():
	while True:
		print("Select the option from following: ")
		option = int(input("1. Add a new movie.\n2. View all movies.\n3. Search movies by title or genre.\n4. Exit\n"))
		if option == 1:
			addNewMovie()
			print("\n")
		elif option == 2:
			viewAllMovies()
			print("\n")
		elif option == 3:
			searchMovies()
			print("\n")
		else:
			print("Thank you for your time!!")
			print("\n")
			break
	

def main():
	print("======== Personal Movie Tracker ========")
	showOptions()

if __name__ == "__main__":
	main()