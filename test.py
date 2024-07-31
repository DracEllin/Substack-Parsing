# from bs4 import BeautifulSoup as BS
# import requests
# file = open("index.html", "r", encoding="utf-8")
# html = file.read()
# soup = BS(html, "html.parser")
# main = soup.find("div", class_="main-container")
# navigations = main.find("div", class_="navigations")
# titles = navigations.find_all("h1", class_="nav")
# # for title in titles:
# #     print(title.text)

# content = main.find("div", class_="content-container")
# posts = content.find_all("div", class_="posts")
# # for post in posts:
# #     title = post.find("h2", class_="title")
# #     print(title.text)
# footer = main.find("div", class_="footer-box")
# boxex = footer.find_all("div", "box")
# for box in boxex:
#     p = box.find("p", class_="title")
#     print(p.text.strip())

def to_jaden_case(string):
    words = string.split(' ')
    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    new_string = ''
    i = 0
    while i != len(new_words):
        if i == len(new_words) - 1:
            new_string += new_words[i]
        else:
            new_string += new_words[i] + ' '
    return new_string
string = input("Введите текст: ")
print(to_jaden_case(string))