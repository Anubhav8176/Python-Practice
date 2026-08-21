
def main():
	number_of_people = int(input("Enter the number of people: "))
	all_people = []
	for people in range(number_of_people):
		temp = input(f"Enter the name of {people+1} person: ")
		all_people.append(temp)

	total_amount = int(input("Enter the total amount to split: "))

	each_person_ows = round(total_amount/number_of_people, 2)

	for people_owe in all_people:
		print(f"{people_owe} owes {each_person_ows}")


if __name__ == "__main__":
	main() 