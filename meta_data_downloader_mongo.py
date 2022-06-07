import os
from bson import ObjectId

from utils.file_handler import FileHandler
from utils.search_wrapper import SearchWrapper
from utils.parameters import movie_data, poster_path
from utils.mongo_handler import MongoHandler

def loader(file_handler):    
    search = SearchWrapper()
    mongo = MongoHandler()

    movie_list = [item.split('.')[0].upper() for item in file_handler.get_movies()]
    # itt le kell kérni minden adatot mongodb-ből
    meta_data = [doc['original_title'].upper() for doc in mongo.get_meta_data()]

    need_to_download = [item for item in movie_list if item not in meta_data]

    for item in need_to_download:
        movie_name = item
        meta_data = search.get_movie_data(movie_name)

        image_link = search.get_image_object()
        image_path = os.path.join(poster_path, f"{meta_data['original_title']}.jpeg")

        meta_data['image_location'] = image_path
        meta_data['upper_movie_name'] = meta_data['original_title'].upper()
        mongo.insert(meta_data)

        file_handler.write_image(image_path, image_link)


def delete_unnecessary_meta(file_handler):
    mongo = MongoHandler()
    movie_list = [item.split('.')[0].upper() for item in file_handler.get_movies()]
    meta_data = [doc['original_title'].upper() for doc in mongo.get_meta_data()]
    need_to_delete = [item for item in meta_data if item not in movie_list]
    filter_statement = {"upper_movie_name": {"$in": need_to_delete }}
    need_to_delete = [doc for doc in mongo.get_meta_data(filter_statement)]

    for item in need_to_delete:        
        image_path = item['image_location']
        os.remove(image_path)
        delete_statement = {'_id': ObjectId(item['_id'])}

        mongo.delete_doc(delete_statement)


def main():
    file_handler = FileHandler()

    delete_unnecessary_meta(file_handler)
    loader(file_handler)


if __name__ == '__main__':
    file_handler = FileHandler()
    #main()
    #loader(file_handler)

    delete_unnecessary_meta(file_handler)
