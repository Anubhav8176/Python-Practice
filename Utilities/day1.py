import datetime

name = input("Please enter your name ")
age = int(input("Please enter your current age "))
city = input("Please enter your city name ")
profession = input("Please enter your profession ")
fav_hobby = input("Please enter your favorite hobby ")

intro_message = (
    f"Hello! my name is {name}, I'm {age} years old and live in {city}. "
    f"I work as a {profession} and I absolutely enjoy {fav_hobby} in my free time. "
    f"Nice to meet you!\n"
)


current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"


border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)