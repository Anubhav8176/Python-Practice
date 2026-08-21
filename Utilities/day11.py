

# Friendship Compatibility Calculator
# 
# Task 1: As usual take the user input i.e; names of the two people to check
# Task 2: Make constants/list for vowels and character positions
# Task 3: Compare them to get the score
# Task 4: Use this score to say the verdict or result.

def get_the_score(name: str, friend: str) -> int:
	name, friend = name.lower(), friend.lower()
	score = 0
	shared_letters = set(name) & set(friend)
	vowels = set('aeiou')

	score += len(shared_letters)*5
	score += len(vowels & shared_letters)*10

	return min(score, 100)


def main():
	name = input("Enter your name here: ")
	friend = input("Enter your friend's name here: ")

	score = get_the_score(name, friend)

	print(f"Your friendship score is: {score}")

if __name__ == "__main__":
	main()