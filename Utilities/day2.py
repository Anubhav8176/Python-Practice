

def save_bio(content):
	try:
		with open("bio.txt", "w", encoding="utf-8") as file:
			file.write(content)
	except:
		raise Exception("Unable to add content")

name = input("Enter your name: ")
profession = input("Enter your profession: ")
goal = input("What are your goals in life? ")
fav_emoji = input("Enter your favorite emoji: ")
url_link = input("Enter your website url or handle: ")

if not fav_emoji.strip():
	fav_emoji = "\U0001F600"

print(f"{fav_emoji} {name} | {profession}")
print(f"💡 {goal}")
print(f"🔗 {url_link}")

# Bonus Part of the code.
# Asking user that they want to store this into the .txt file

print("\n")
print("\n")
print("\n")

save_it = input("You want to save this bio in a .txt file? (y/n)")

if save_it=="y":
	content_to_save = f"{fav_emoji} {name} | {profession} \n 💡 {goal} \n 🔗 {url_link}"
	save_bio(content_to_save)