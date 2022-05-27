import pprint
import tmdbsimple as tmdb
from urllib.request import urlopen

tmdb.API_KEY = "454b6ca4172e455fe7a7d8395c10d6d9"

image_path_string = 'https://image.tmdb.org/t/p/original/bk9GVjN4kxmGekswNigaa5YIdr5.jpg'

search = tmdb.Search()

movie_data = search.movie(query="The")

pprint.pprint(movie_data['results'], indent=4)

# temp = urlopen(image_path_string).read()

# print(temp)

# with open('alien.jpg', "wb") as poster:
#     poster.write(urlopen(image_path_string).read())