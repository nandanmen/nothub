import json

with open("../users.json") as file:
    users = json.load(file)


def get_user(client, login):
    return client.get_user(users[login])
