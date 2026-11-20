import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "book_data.json"
TARGET_COUNT = 70

def scrape_books(current_url):
    try:
        response = requests.get(current_url)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Failed to fetch the data")
        return [], None

    print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()

        books.append({"title": title, "price": price})

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(current_url, next_link.get("href")) if next_link else None

    return books, next_url

def main():
    collected = []
    current_url = urljoin(BASE_URL, START_PAGE)

    while len(collected) < TARGET_COUNT and current_url:
        print(f"Scraping: {current_url}")
        book, next_url = scrape_books(current_url)
        collected.extend(book)
        current_url = next_url

    collected = collected[:TARGET_COUNT]
    print(f"Scraped {TARGET_COUNT} books")

    with open(OUTPUT_PAGE, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=4)

    print(f"Data save to {OUTPUT_PAGE}")


if __name__ == "__main__":
    main()