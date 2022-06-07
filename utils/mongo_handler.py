from pymongo import mongo_client

class MongoHandler:
    uri = "mongodb://localhost:27017"

    def __init__(self):
        self.connection = self.create_connection()
        self.db_name = "movie_meta"
        self.col_name = "movies"

    def create_connection(self):
        return mongo_client.MongoClient(self.uri)

    def create_db_object(self):
        return self.connection[self.db_name]

    def create_col_object(self):
        return self.create_db_object()[self.col_name]

    def insert(self, doc):
        return self.create_col_object().insert_one(doc).inserted_id

    def delete_doc(self, filter_statement):
        if not isinstance(filter_statement, dict):
            return False, "Not valid mongo filter"

        return self.create_col_object().delete_one(filter_statement).deleted_count

    def get_meta_data(self, filter_statement={}):
        return self.create_col_object().find(filter_statement)


if __name__ == '__main__':
    mongo = MongoHandler()

    mongo.db_name = 'test'
    mongo.col_name = 'only_test'

    for item in mongo.create_col_object().find({}):
        print(item)