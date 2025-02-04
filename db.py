from pymongo import MongoClient


# if 'db' not in g:
def get_db():

    client = MongoClient(
        "mongodb+srv://rohanchaudhary:<db_password>@cluster0.artvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    return client["Fitness2DA_database"]
