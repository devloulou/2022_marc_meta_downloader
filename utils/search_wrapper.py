from urllib.request import urlopen
import tmdbsimple as tmdb

class SearchWrapper:
    tmdb.API_KEY = "454b6ca4172e455fe7a7d8395c10d6d9"

    def __init__(self):
        self.image_api = 'https://image.tmdb.org/t/p/original'
        self.search = tmdb.Search()
        self.jpg_path = None

    def get_movie_data(self, movie):
        data = self.search.movie(query=movie)['results'][0]
        self.jpg_path = data['poster_path']
        return data

    def get_image_object(self, jpg_path=None):
        # if jpg_path is None:
        #     url = self.image_api + self.jpg_path
        # else:
        #     url = self.image_api + jpg_path
        
        # return urlopen(url)

        url = self.image_api + self.jpg_path if jpg_path is None \
                else self.image_api + jpg_path

        return urlopen(url)

if __name__ == '__main__':
    my_search = SearchWrapper()
    data = my_search.get_movie_data('Alien')
    image_link = my_search.get_image_object()

    with open('alien.jpg', "wb") as poster:
        poster.write(image_link.read())