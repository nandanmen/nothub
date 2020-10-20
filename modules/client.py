import os
from notion.client import NotionClient

client = NotionClient(token_v2=os.environ.get("TOKEN_V2"))

board = client.get_collection_view(os.environ.get("COLLECTION"))
