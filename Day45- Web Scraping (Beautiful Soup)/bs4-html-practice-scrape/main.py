# Name of package and BeautifulSoup is the class
from bs4 import BeautifulSoup
# Import lxml

# encoding for the emoji
with open("website.html", encoding="utf-8") as file:
    data = file.read()

# instantiating class and passing in data, soup is object
# specify language of parser for file, sometimes use lxml parser
soup = BeautifulSoup(data, "html.parser")

# # using soup object to get content within html tag
# print(soup.title)
# # give you name of tag
# print(soup.title.name)
# # gives you text within html tag
# print(soup.title.string)
# # prints anchor tag
# print(soup.a)
#
# # Prints all HTML code well spaced out
# print(soup.prettify())

#Give us all the a tags
# all_anchor_tags = soup.find_all(name="a")
#
# # Loops through all tags
# for tag in all_anchor_tags:
    ## Gets text
    # print(tag.getText())

    # # prints all the links
    # print(tag.get("href"))

# You can search by tag or/and attribute name (id,class)
# heading = soup.find(name="h1", id="name")
# print(heading)

# # select_one gives us first matching item and select all of them
# # using css selector
# name = soup.select_one(selector="#name")
# print(name)

# This will select all elements that have class of heading, it yields a list
headings = soup.select(".heading")
print(headings)


