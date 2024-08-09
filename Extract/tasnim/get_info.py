from bs4 import BeautifulSoup
import requests

def get_info(url: str) -> dict:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return {}

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.title.string if soup.title else 'No title found'
    text = soup.get_text(strip=True)

    return {
        'title': title,
        'text': text
    }


