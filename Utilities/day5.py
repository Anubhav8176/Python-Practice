emoji_map_fun = {
    "love": "❤️",
    "happy": "😊",
    "code": "💻",
    "tea": "🍵",
    "music": "🎵",
    "food": "🍕",
}

raw_message = input("Enter the message you want to enhance:\n")
message_list = raw_message.split()
updated_raw_message = []
for message in message_list:
	updated_message = message.lower().strip(".,!?")
	if message in emoji_map_fun:
		updated_message = f"{message} {emoji_map_fun.get(message, "")} "
		updated_raw_message.append(updated_message)
	else:
		updated_raw_message.append(message)

print("\n Enhanced message: \n")
print(" ".join(updated_raw_message))