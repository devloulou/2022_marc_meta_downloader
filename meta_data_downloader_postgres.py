import os
from bson import ObjectId

from utils.file_handler import FileHandler
from utils.search_wrapper import SearchWrapper
from utils.parameters import (movie_data,
                                poster_path,
                                meta_table,
                                select_movie_titles, 
                                insert_meta_table)
from utils.mongo_handler import MongoHandler
from utils.db_handler import PostgreDB


def loader(file_handler):    
    search = SearchWrapper()
    sql = PostgreDB()

    movie_list = [item.split('.')[0].upper() for item in file_handler.get_movies()]
    meta_data = [item[0] for item in sql.run_sql(select_movie_titles)]

    need_to_download = [item for item in movie_list if item not in meta_data]

    for item in need_to_download:
        movie_name = item
        meta_data = search.get_movie_data(movie_name)

        image_link = search.get_image_object()
        image_path = os.path.join(poster_path, f"{meta_data['original_title']}.jpeg")

        meta_data['image_location'] = image_path
        
        meta_data.pop("id")
        meta_data.pop("genre_ids")
        data = []
        
        for item in meta_data.values():
            data.append(item)

        sql.insert_data(insert_meta_table, tuple(data))

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

def initialize_postgres_objects():
    sql = PostgreDB()
    is_it_ok = sql.run_sql(meta_table)
    # if is_it_ok != True:
    #     raise ValueError(f'{is_it_ok[1]}')

    if isinstance(is_it_ok, tuple):
        raise ValueError(f'{is_it_ok[1]}')
    return True

def main():
    file_handler = FileHandler()

    initialize_postgres_objects()
    #delete_unnecessary_meta(file_handler)
    loader(file_handler)


if __name__ == '__main__':
    main()
