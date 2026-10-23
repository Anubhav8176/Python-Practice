# Step: 1=> Read the data from the file named api_data.json
# Step: 2=> Convert this data into a dictionary
# Step: 3=> Get the fields from the dictionary
# Step: 4=> Set the data into the converted_data.json file


import os, json, csv

def load_json_data(file_name):
	if not os.path.exists(file_name):
		print("File doesnot exists")
		return []

	with open(file_name, "r", encoding="utf-8") as file:
		try:
			return json.load(file)
		except:
			print("Invalid JSON format!!")

def extract_the_data(data, filename):	
	if not data:
		print("No data was found!")
		return

	field_name = list(data[0].keys())

	with open(filename, "w", newline="", encoding="utf-8") as file:
		writer = csv.DictWriter(file, fieldnames=field_name)
		writer.writeheader()

		for record in data:
			writer.writerow(record)

	print(f"Conversion is successfull!")

def main():
	data_arr = load_json_data("api_data.json")
	extract_the_data(data=data_arr, filename="converted_data.csv")
	

if __name__ == "__main__":
	main()