import os, json


FILENAME = "vault.txt"

def load_data():
	try:
		with open("vault.txt", "r", encoding="utf-8") as file:
			content = json.load(file)
		return content
	except Exception as e:
		return {}

def add_data(website_name, username, password):

	new_data = {
		website_name: {
			"username": username,
			"password": password
		}
	}

	if os.path.exists(FILENAME) and os.path.getsize(filename=FILENAME)>0:
		with open("vault.txt", "r", encoding="utf-8") as file:
			existing_data = json.load(file)
	else:
		existing_data = {}

	existing_data.update(new_data)

	with open("vault.txt", "w", encoding="utf-8") as file:
		json.dump(existing_data, file, indent=4)

def check_password(password: str):
	suggestion_to_improve = []
	has_small = False
	has_capital = False
	has_number = False
	has_special_character = False
	if len(password) > 8:
		for a in password:
			if a.isupper():
				has_capital = True
			elif a.islower():
				has_small = True
			elif a.isdigit():
				has_number = True
			elif not a.isalnum() or a.isspace():
				has_special_character = True
	else:
		suggestion_to_improve.append("Password length should greater than 8!")

	if has_small and has_capital and has_number and has_special_character:
		return "strong"
	elif sum([has_small, has_capital, has_number, has_special_character])==3:
		return "medium"
	else:
		return "weak"


def add_new_password():
	while True:
		website_name = input("Enter the name of the website: ")
		username = input("Enter the username used there: ")
		password = input("Enter the password: ")
		password_strength = check_password(password=password)
		if password_strength == "strong":
			decision = input("Password is strong, wanna save it?: (y/n)").strip().lower()
			if decision == "y":
				add_data(website_name=website_name, username=username, password=password)
				break
		elif password_strength == "medium":
			decision = input("Password is not so strong, still want to save it? (y/n): ").strip().lower()
			if decision == "y":
				add_data(website_name=website_name, username=username, password=password)
				break
		else:
			decision = input("Password is weak, might consider making a strong one. Still want to go ahead? (y/n): ").strip().lower()
			if decision == "y":
				add_data(website_name=website_name, username=username, password=password)
				break


def list_the_vault():
	content = load_data()
	for website, data in content.items():
		print(f"Website: {website}")
		print(f"	Username: {data["username"]}")
		print(f"	Password: {data["password"]}")

	print("\n")

def update_an_entry():
	content = load_data()

	website_name = input("Enter the name of the website: ")
	password = input("Enter the new password: ")

	found = False

	for key, item in content.items():
		if key == website_name:
			item["password"] = password
			found = True
			break

	if found:
		with open("vault.txt", "w", encoding="utf-8") as file:
			json.dump(content, file, indent=4)
	else:
		print(f"Website with name {website_name} does not found!")

def main():
	print("====Offline Credential Manager====")

	while True:
		operation = int(input("Select an option from below: \n1. Add new password.\n2. List the vault.\n3. Update an entry.\n4. Quit\n"))
		print()
		if operation == 1:
			add_new_password()
		elif operation == 2:
			list_the_vault()
		elif operation == 3:
			update_an_entry()
		elif operation == 4:
			break
		else:
			print("Enter a valid operation i.e 1, 2, 3 or 4")

if __name__ == "__main__":
	main()