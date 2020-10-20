""" import json

with open("users.json") as file:
    users = json.load(file) """

import os
from .client import client


users = {
    "narendrasss": "b7a8d519-63fb-4cbb-bb68-b37360b6d70b",
    "kx-chen": "d03eff2d-1b3a-47bf-a3c6-84cb5a6f6032",
    "jackyzha0": "fa67aa9a-3aa7-4416-8693-7b6eb83faef4",
    "xanhlaok": "382e1fcd-494d-44d4-a70c-828de5534200",
    "francismacapobre": "ac56b8e8-586c-45ab-b135-ad5f14461b98",
    "michelleykim": "220fedd8-c1de-47d4-80e1-ffeb62e57e4c",
    "jmengo": "f396bd97-d814-4de3-b6d7-a92e8568e259",
    "tiffanywu0313": "3f5adc90-0717-4310-b805-01db92d5107a",
    "gokcedilek": "00abae75-7e1a-4044-bea9-da23f78abc8a",
    "baojill": "bf2cd194-9c6c-45d9-bdf4-ed0c1de325c0",
    "HenryY0518": "47db1698-fede-43a5-b7ef-49579062eaaf"
}


def get_user(login):
    if login in users:
        return client.get_user(users[login])


def get_users():
    db = client.get_collection_view(os.environ.get("COLLECTION"))
    result = db.default_query().execute()

    users = {}
    for row in result:
        props = row.get_all_properties()
        for user in props["assign"]:
            if user.full_name not in users:
                users[user.full_name] = {
                    "email": user.email,
                    "id": user.full_name
                }

    return users
