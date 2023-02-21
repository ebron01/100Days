import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name='h3', class_='title')

movie_titles = [film.getText() for film in all_movies]
movies = movie_titles[::-1]

with open("/home/beast/100Days/100movies/movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")
