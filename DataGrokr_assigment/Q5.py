"""5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
the web, and prints it after stripping HTML tags."""
import sys
import requests
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Usage: python anti_html.py <URL>")
        return
    
    url = sys.argv[1]
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()

    # Step 4: Print clean text
    print(text)

if __name__ == "__main__":
    main()
