import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
text = response.text
soup = BeautifulSoup(text, "html.parser")

questions = soup.select(".s-post-summary")

for question in questions:
    title = question.select_one(".s-link").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    print(f"{user} - Title: {title}")
