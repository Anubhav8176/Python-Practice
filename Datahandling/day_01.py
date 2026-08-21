import csv
import os

# Task needed to build CLI Contact Book (CSV-Powered)
# Task 1: Give user the options to select from to perform some operation. Done
# Task 2: Make the functions for 1. Adding new contact, 2. View contacts, 3. Search contact from the file (CSV).
# Take 3: Complete all the function and handle the CSV files.

FILENAME = "contacts.csv"

# If file exist open that file
if not os.path.exists(FILENAME):
	with open(FILENAME, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["Name", "Phone", "Email"])
	

def add_contacts():
	name = input("Enter the name: ")
	phone = input("Enter the number here: ")
	email = input("Enter the email here: ")

	with open(FILENAME, "r", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			if row["Name"].lower() == name.lower():
				print("Contact already exists")
				return

	with open(FILENAME, "a", encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow([name, phone, email])
		print("Contact added succesfully")

def view_all_contacts():
	with open(FILENAME, 'r', encoding="utf-8") as file:
		file_data = csv.reader(file)
		rows = list(file_data)

		if len(rows)<1:
			print("No contacts found!!")
			return
		for contact in rows[1:]:
			print(f"{contact[0]} | {contact[1]} | {contact[2]} | ")
		print()

def search_contact():
	query = input("Enter the contact you want to search for: ").strip().lower()
	found = False
	with open(FILENAME, "r", encoding="utf-8") as file:
		reader = csv.DictReader(file)
		for row in reader:
			if query in row['Name'].lower():
				print(f"{row['Name']} | {row['Phone']} | {row['Email']} | ")
				found = True

		if not found:
			print("No matching contact found!")	
		print()

def main():
	while True:
		print("=====Contact Book=====")
		print("1. Add a new contact")
		print("2. View all contacts")
		print("3. Search a contact")
		print("4. Exit")
		option = int(input("Please select one the following options(Enter the number you want to choose):"))

		print("\n=======================================\n")

		match option:
			case 1:
				add_contacts()
			case 2:
				view_all_contacts()
			case 3:
				search_contact()
			case 4:
				break
			case _:
				print("Please enter a valid number!!")


if __name__ == "__main__":
	main()
