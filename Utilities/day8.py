import getpass
import string
import random

def check_password(password: str):
	issues = []
	if len(password)>=8:
		if not any(c.islower() for c in password):
			issues.append("Password must has a lower case letter")
		if not any(c.isupper() for c in password):
			issues.append("Password must has a upper case letter")
		if not any(c.isdigit() for c in password):
			issues.append("Password must has a digit")
		if not any(c in string.punctuation for c in password):
			issues.append("Password must contain a special character")		
	else:
		issues.append("Password must contain at least 8 characters!")

	return issues


def suggest_strong_password():
	length = random.randint(8, 20)
	password_options = string.ascii_letters + string.digits + string.punctuation

	return "".join(random.choice(password_options) for _ in range(length))
		

def main():
	password = getpass.getpass("Enter your password here: ")
	issues = check_password(password=password)

	if len(issues)>0:
		print("Your password has following issue(s): \n")
		for issue in issues:
			print(issue)

		suggested_strong_password = suggest_strong_password()
		print(f"Here is a strong password: {suggested_strong_password}")
	else:
		print("Password is strong you can continue with it! Have a great day.")

if __name__ == "__main__":
	main()