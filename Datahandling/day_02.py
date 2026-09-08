
def get_student_data():
	students = {}

	while True:
		name = input("Enter the name of the student or done if you want to exit: ").strip()
		if name.lower() == "done":
			break

		if name in students:
			print("Student already exists")
			continue

		marks = input("Enter the marks of the student: ").strip()

		try:
			int_marks = int(marks)
			students[name] = int_marks
		except ValueError:
			print("Marks should be in integer")

	return students


def display_report(students):
    if not students:
        print("No student data ❌")
        return
    
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score ]
    bottomer = [name for name, score in students.items() if score == min_score ]

    print("\n Students marks report 🗓️")
    print("-" * 30)
    print(f"Total students: {len(students)}")
    print(f"average marks for students: {average:.2f}")
    print(f"Highest marks : {max_score} by {', '.join(topper)}")
    print(f"lowest marks : {min_score} by {', '.join(bottomer)}")

    print("-" * 30)
    print("Detailed Marks 🗓️")
    for name, score in students.items():
        print(f" - {name}: {score}")
		  

def main():
	print("======== Welcome to the student marks analyzer ========")
	students = get_student_data()
	display_report(students=students)

if __name__ == "__main__":
	main()