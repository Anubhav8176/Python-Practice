"""
This is the Personal Movie Tracker application.
"""

def ShowOptions():
	print("Select the option from following: ")
	option = int(input("1. Add a new movie.\n2. View all movies.\n3. Search movies by title or genre.\n4. Exit\n"))
	

def main():
	print("======== Personal Movie Tracker ========")
	ShowOptions()

if __name__ == "__main__":
	main()