import pprint
import tmdbsimple as tmdb

tmdb.API_KEY = "454b6ca4172e455fe7a7d8395c10d6d9"

image_path_string = 'https://image.tmdb.org/t/p/original/bk9GVjN4kxmGekswNigaa5YIdr5.jpg'

search = tmdb.Search()

movie_data = search.movie(query="Alien")

pprint.pprint(movie_data['results'][0], indent=4)
