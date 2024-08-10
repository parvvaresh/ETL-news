import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from get_links import get_links
from get_info import get_info

def extract_tasnim() -> pd.DataFrame:
    links = get_links()

    df = pd.DataFrame(columns=['url', 'title', 'text'])

    def process_link(link):
        try:
            result = get_info(link)
            print(result)
            return {
                'url': link,
                'title': result.get('title', 'No title found'),
                'text': result.get('text', 'No text found')
            }
        except Exception as e:
            print(f"Error processing {link}: {e}")
            return {
                'url': link,
                'title': 'Error',
                'text': 'Error'
            }

    with ThreadPoolExecutor(max_workers=16) as executor:
        future_to_link = {executor.submit(process_link, link): link for link in links}

        for future in as_completed(future_to_link):
            result = future.result()
            df = df.append(result, ignore_index=True)

    return df



extract_tasnim()