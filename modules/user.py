""" import json

with open("users.json") as file:
    users = json.load(file) """

users = {
    "narendrasss": "b7a8d519-63fb-4cbb-bb68-b37360b6d70b"
}


def get_user(client, login):
    return client.get_user(users[login])
