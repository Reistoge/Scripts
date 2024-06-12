import re
import requests

def collect_phone_numbers(url):
    # Fetch the HTML content of the page
    page = requests.get(url)
    html_content = page.text
  
    # Use a regular expression pattern to search for phone numbers
    phone_number_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    phone_numbers = re.findall(phone_number_pattern, html_content)
  
    return phone_numbers

# Example usage
url = "https://www.zipmec.eu/en/cards.html"
phone_numbers = collect_phone_numbers(url)
print("Phone numbers found:", phone_numbers)
