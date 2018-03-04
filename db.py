import json

def get_msg():
    with open("./database/data.json","r") as f:
        myjson = json.load(f)
    return myjson
