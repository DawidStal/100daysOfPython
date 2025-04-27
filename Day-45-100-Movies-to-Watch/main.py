import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

soup = BeautifulSoup(response.text,"html.parser")
# print(soup.prettify())
movies = soup.find_all(name="h3", class_="title")
movie_ranking = []
for movie in reversed(movies):
    text = movie.getText()
    if ")" in text:
        text = text.split(")")
    if ":" in text:
        text = text.split(":")
    number = int(text[0])
    title = text[1][1:]
    movie_ranking.append((number, title))

print(movie_ranking)
with open("Day-45-100-Movies-to-Watch//movies.txt", "w",  encoding="utf-8") as file:
    for movie in movie_ranking:
        file.write(f"{movie[0]}, {movie[1]} \n")

