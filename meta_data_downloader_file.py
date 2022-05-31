import os
from utils.file_handler import FileHandler
from utils.search_wrapper import SearchWrapper
from utils.parameters import movie_data, poster_path

def loader(file_handler):    
    search = SearchWrapper()

    movie_list = [item.split('.')[0] for item in file_handler.get_movies()]
    meta_data = [item.split('.')[0] for item in file_handler.get_files_from_folder(movie_data)]

    need_to_download = [item for item in movie_list if item not in meta_data]

    for item in need_to_download:
        movie_name = item
        meta_data = search.get_movie_data(movie_name)

        image_link = search.get_image_object()
        image_path = os.path.join(poster_path, f"{movie_name}.jpeg")

        json_path = os.path.join(movie_data, f"{movie_name}.json")

        file_handler.write_json(json_path, meta_data)
        file_handler.write_image(image_path, image_link)


def delete_unnecessary_meta(file_handler):
    movie_list = [item.split('.')[0] for item in file_handler.get_movies()]

    meta_data = [item.split('.')[0] for item in file_handler.get_files_from_folder(movie_data)]

    need_to_delete = [item for item in meta_data if item not in movie_list]

    for item in need_to_delete:        
        image_path = os.path.join(poster_path, f"{item}.jpeg")
        meta_path = os.path.join(movie_data, f"{item}.json")

        os.remove(image_path)
        os.remove(meta_path)


def main():
    file_handler = FileHandler()

    delete_unnecessary_meta(file_handler)
    loader(file_handler)


if __name__ == '__main__':
    main()
