import sys
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import argparse

def get_social_links(domain):
    try:
        # Make a GET request to the URL
        response = requests.get(domain, timeout=args.timeout)

        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the anchor tags in the HTML
        links = soup.find_all('a')

        # Print the URL
        print("\nURL: " + domain)

        for link in links:
            href = link.get('href')
            if href and 'facebook' in href:
                print(href)
            elif href and 'instagram' in href:
                print(href)
            elif href and 'twitter' in href:
                print(href)
            elif href and 'linkedin' in href:
                print(href)
            elif href and 'youtube' in href:
                print(href)

    except KeyboardInterrupt:
        exit(0)
    except:
        pass

def main(threads):
    domains = [line.strip() for line in sys.stdin.readlines()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(get_social_links, domain) for domain in domains]
        concurrent.futures.wait(futures)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threads', type=int, default=50, help='number of threads to use (default 50)')
    parser.add_argument('--timeout', type=int, default=5, help='timeout in seconds (default 5)')
    args = parser.parse_args()
    main(args.threads)