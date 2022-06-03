from pymongo import mongo_client

# 1. kapcsolatat létrehozása
# 2. database object
# 3. collection object
# 4. minden utasítás a collection-objecten keresztül fog történni
#######################################

#1.
uri = "mongodb://localhost:27017"
connection = mongo_client.MongoClient(uri)

#2.
database = connection['test']

#3.
col = database['only_test']

# 4.
# test adat
my_dict = {
    "auto": "BMW",
    "color": "white",
    "motor_type": "benzin"
}

my_dict2 = {
    "auto": "Volvo",
    "color": "white",
    "motor_type": "benzin"
}

my_dict3 = {
    "auto": "BMW",
    "color": "black",
    "motor_type": "benzin"
}

many_doc = (my_dict, my_dict2, my_dict3)

# insert to mongodb

#col.insert_one(my_dict)
result = col.insert_many(many_doc, ordered=False)


# delete:

#result = col.delete_one({'auto': {"$in": ['Volvo']} })
#result = col.delete_many({'auto': {"$in": ['Volvo']} })

# print(result.raw_result)
# print(result.deleted_count)

# update:

filter_st = {"auto": "Opel"}
update_statement = {'$set': {"auto": "Opel", "color": "yellow"}}

#col.update_one(filter=filter_st, update=update_statement, upsert=True)

# select vagy read

for item in col.find({'auto': 'BMW'}):
    print(item)