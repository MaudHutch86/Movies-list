import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")

movies_list = []
title_list = soup.find_all(name="h3", class_="title")
for title in title_list:
    movie = title.getText()
    movies_list.append(movie)

for n in range(1, len(movies_list)):
    movies = movies_list[::-1]


with open("movies.text", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")