folder_path = r"C:\WORK\prooktatas\oop_project\movies"
movie_data = r"C:\WORK\prooktatas\oop_project\movie_data"
poster_path = r"C:\WORK\prooktatas\oop_project\posters"

meta_table = """
create table if not exists meta_data (
    id serial primary key,
    adult bool,
    backdrop_path text,
    original_language text,
    original_title text,
    overview text,
    popularity numeric,
    poster_path text,
    release_date text,
    title text,
    video bool,
    vote_average numeric,
    vote_count int,
    image_location text
)
"""

insert_meta_table = """
insert into meta_data (adult, backdrop_path, original_language, original_title,
overview, popularity, poster_path, release_date, title, video, vote_average,
vote_count, image_location) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

"""

select_movie_titles = """
    select upper(original_title) as title from meta_data t
"""

select_data_for_deletion = """
select
upper(original_title) as title,
t.id,
t.image_location
from meta_data t
"""

delete_movie = """
delete from meta_data where id = {id}
"""