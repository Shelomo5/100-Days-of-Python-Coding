import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

# get hold of data from particular url
response = requests.get(URL)
# raw text
movies_page = response.text

# instantiating class and passing in data, soup is object
# specify language of parser for file, sometimes use lxml parser
soup = BeautifulSoup(movies_page, "html.parser")

# find movie titles using elements organized in a list
movie_titles = soup.find_all(name="h3", class_="title")
# reverses in place the list order
movie_titles.reverse()

# Open text file
with open("movies.txt", "w", encoding="utf-8") as file:
    # iterate through each title and get the string only and place in text file
    for title in movie_titles:
        title_string = title.getText()
        file.write(f"{title_string}\n")



