import requests
from bs4 import BeautifulSoup

def get_links(url_root  = "https://www.hamshahrionline.ir/") -> list:
    response = requests.get(url_root)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = [link['href'] for link in links]

        urls = [url for url  in urls  if "news" in url]
        urls = [url_root + url for url  in urls]

        return urls


    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []
