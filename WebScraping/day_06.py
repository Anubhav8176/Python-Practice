import requests, os, textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def main():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch the url {BASE_URL}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    raw_quotes = soup.select("div.quote")[:5]
    quotes = []

    for quote_body in raw_quotes:
        quote = quote_body.select_one(".text").get_text(strip=True)
        author = quote_body.select_one(".author").get_text(strip=True)
        quotes.append({"quote": quote, "author": author})

    print(quotes)


def create_image(quote, author, index):
    width, height = 800, 400
    backgroud_color = "#f8d77f"
    text_color = "#262626"
    
    image = Image.new("RGB", (width, height), backgroud_color)
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.load_default()
    author_font = ImageFont.load_default()
    
    wrapped = textwrap.fill(quote, width=60)
    author_text = f"- {author}"
    
    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)
    y_text += wrapped.count('\n') * 15 + 40
    draw.text((500, y_text), author_text, font=font, fill=text_color)
    
    # save image
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filename)
    print(f"✅ saved: {filename}")

    

if __name__ == "__main__":
    main()