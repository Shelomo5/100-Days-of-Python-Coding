from bs4 import BeautifulSoup
import requests


# get hold of data/text from particular url
response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# use find_all to locate attribute and get all the articles in list
articles = soup.find_all(class_="titleline")
#lists created to store texts and links
article_texts = []
article_links = []
for article in articles:
    # This just gets strings
    text = article.getText()
    article_texts.append(text)

    # This gets links
    link = article.find(name="a").get("href")
    article_links.append(link)

# List comprehension where we make a list of upvotes in text form
# score is split and we keep first item and convert to int
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# gets largest upvotes and its index
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
