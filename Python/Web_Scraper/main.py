import requests
from bs4 import BeautifulSoup

def scrape_data(url, container_tag, container_class, fields):
    """
    Scrape data from a webpage.

    Arguments:
    - url: The web address to scrape from.
    - container_tag: The HTML tag that holds each item (e.g., 'div').
    - container_class: The class name of the container tag (e.g., 'book-info').
    - fields: A dictionary with field names as keys, and (tag, class) tuples as values.
              These describe where to find each piece of data inside the container.

    Returns:
    - A list of dictionaries with the scraped information.
    """

    # Get the webpage content
    response = requests.get(url)

    # Check if the page was retrieved successfully
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return None

    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all item containers
    containers = soup.find_all(container_tag, class_=container_class)

    # List to store all scraped data
    all_data = []

    # Loop through each container and extract the data fields
    for container in containers:
        item_data = {}
        for field, (tag, cls) in fields.items():
            element = container.find(tag, class_=cls)
            if element:
                item_data[field] = element.get_text(strip=True)
            else:
                item_data[field] = f"No {field}"
        all_data.append(item_data)

    return all_data

# Example usage:

url = "https://example.com/books"  # Change this to the real URL

# Define the container and fields to scrape
container_tag = "div"
container_class = "book-info"
fields = {
    "Title": ("h2", "book-title"),
    "Author": ("p", "author"),
    "Price": ("span", "price"),
}

# Call the function to scrape data
scraped_data = scrape_data(url, container_tag, container_class, fields)

# Print the results if any data was scraped
if scraped_data:
    for item in scraped_data:
        for key, value in item.items():
            print(f"{key}: {value}")
        print()  # Blank line between items
else:
    print("No data scraped.")
