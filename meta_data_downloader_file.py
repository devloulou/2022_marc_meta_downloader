import os
from utils.file_handler import FileHandler
from utils.search_wrapper import SearchWrapper
from utils.parameters import movie_data, poster_path

def loader():
    file_handler = FileHandler()
    search = SearchWrapper()

    movie_list = file_handler.get_file_list()

    for item in movie_list:
        movie_name = item.split('.')[0]
        meta_data = search.get_movie_data(movie_name)

        image_link = search.get_image_object()
        image_path = os.path.join(poster_path, f"{movie_name}.jpeg")

        json_path = os.path.join(movie_data, f"{movie_name}.json")

        file_handler.write_json(json_path, meta_data)
        file_handler.write_image(image_path, image_link)

if __name__ == '__main__':
    loader()
