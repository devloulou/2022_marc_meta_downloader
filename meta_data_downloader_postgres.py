import os

from utils.file_handler import FileHandler
from utils.search_wrapper import SearchWrapper
from utils.parameters import (movie_data,
                                poster_path,
                                meta_table,
                                select_movie_titles, 
                                insert_meta_table,
                                select_data_for_deletion,
                                delete_movie)
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
    sql = PostgreDB()
    movie_list = [item.split('.')[0].upper() for item in file_handler.get_movies()]

    meta_data = { item[0] : item[1:]  for item in sql.run_sql(select_data_for_deletion)}
    
    need_to_delete = [item for item in meta_data.keys() if item not in movie_list]

    for item in need_to_delete:        
        data = meta_data[item]
        os.remove(data[1])
        sql.run_sql(delete_movie.format(id=data[0]))

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
    delete_unnecessary_meta(file_handler)
    loader(file_handler)


if __name__ == '__main__':
    main()
