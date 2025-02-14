import requests 
from bs4 import BeautifulSoup

def get_user_input():
    """Get URL Input From the user"""
    return input("Please Input a Full URL: ")

def web_scraper(get_url):
    """Web Scraping Function"""
    try:
        #Make a GET request to the URL
        response = requests.get(get_url)

        #Check For HTTP Errors
        response.raise_for_status()

        #Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        #Extract text from selected HTML elements
        elements = soup.find_all(['h1', 'h2', 'h3', 'p', 'td', 'tr', 'div'])
        clean_text = '\n\n'.join([element.get_text(strip=True) for element in elements])

        #Print the cleaned text from the webpage 
        print(f"Content from {get_url}")
        print("="*50) #visual separator
        print(clean_text)

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error Code: {err}")
    except Exception as e:
        print(f"Error occurred while parsing HTML: {e}")

#Check if this file is being run directly
if __name__ == "__main__":
    get_url = get_user_input()
    if not get_url:
        print("Error: URL cannot be empty!")
    else:
        web_scraper(get_url)