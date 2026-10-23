import requests
from bs4 import BeautifulSoup

def get_h2_headers(url):
	headers = {
        "User-Agent": "MyH2Scraper/1.0 (https://example.com; you@example.com)"
    }
	try:
		response = requests.get(url=url, headers=headers, timeout=10)
		response.raise_for_status()
	except requests.RequestException as e:
		print(f"Failed to load the information: \n{e}")

	beautiful_soup = BeautifulSoup(response.text, "html.parser")
	all_h2 = beautiful_soup.find_all("h2")
	header_tag_h2 = []

	for tag in all_h2:
		header_tag_h2.append(tag.get_text(strip=True))

def main():
	URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
	get_h2_headers(URL)

if __name__ == "__main__":
	main()