from datetime import datetime

def save_content_to_file(content_to_add):
	try:
		with open("learning_journal.txt", "a", encoding="utf-8") as file:
			file.write("\n"+content_to_add)
	except:
		raise Exception("Encountered an error while adding the content to the file!")

def read_content_from_file():
	try:
		with open("learning_journal.txt", "r", encoding="utf-8") as file:
			content = file.read()
			print(f"Your journal is: \n {content}")
			
	except:
		raise Exception("Encountered an error while adding the content to the file!")

def raw_data_to_content(content: str, rating: float):
	if not 0<=rating<=5:
		raise Exception("Rating should be a number and between 0-5.")

	current_datetime = datetime.now()

	date = current_datetime.strftime("%Y-%m-%d - %I:%M %p")	

	content_to_return = f"📅 {date} {content}! Productivity Rating: {rating}/5.0"

	return content_to_return

def main():
	print("Welcome to the Learning journal system!")
	content = input("Hey there! What have you learnt today? ")
	rating = float(input("Give yourself a productive rating out of 5 for today: "))

	formatted_content = raw_data_to_content(content=content, rating=rating)

	save_content_to_file(formatted_content)

	read_content  = input("Do you want to read the content from the journal? (y/n) ")

	if read_content.lower() == 'y':
		read_content_from_file()
	elif read_content.lower == 'n':
		print("Good Bye! Have a great day ahead.")

if __name__ == "__main__":
	main()