import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, 'html.parser')

titles = soup.find_all(name="h3", class_="title")
title_list = [title.getText() for title in titles][::-1]

for title in title_list:
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        file.write(f"{title}\n")
