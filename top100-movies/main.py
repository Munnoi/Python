import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
all_movies = soup.select(selector='span h2 strong')
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movie_titles = movie_titles[::-1]

with open("top100-movies/movies.txt", mode='w') as file:
  for movie in movie_titles:
    file.write(f"{movie}\n")