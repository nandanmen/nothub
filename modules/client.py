import os
from notion.client import NotionClient

client = NotionClient(token_v2=os.environ.get("TOKEN_V2"))
