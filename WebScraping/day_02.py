import requests
import csv
import os
from bs4 import BeautifulSoup


FILENAME = "hn_top20.csv"

if os.path.exists(FILENAME):
	with open(FILENAME, "w", newline="", encoding="utf-8") as file:
		writer = csv.writer(file)
		writer.writerow(["Title", "Content"])

def save_to_csv(content):
	try:
		with open(FILENAME, "a", encoding="utf-8") as file:
			writer = csv.writer(file)
			for data in content:
				writer.writerow([data["title"], data["content"]])
	except Exception as e:
		print(f"Failed to save data: {e}")

def extract_titles(url):
	try:
		response = requests.get(url=url, timeout=10)
		response.raise_for_status()
	except requests.RequestException as e:
		print(f"Failed to get the page: {e}")

	beautiful_soup = BeautifulSoup(response.text, "html.parser")
	link = beautiful_soup.select("span.titleline > a")
	titles = []

	for tags in link:
		content = {
			"title": tags.text,
			"content": tags["href"]
		}
		titles.append(content)

	save_to_csv(titles)


def main():
	URL = "https://news.ycombinator.com/"
	extract_titles(url=URL)

if __name__ == "__main__":
	main()
