import os
from .user import get_user
from notion.client import NotionClient
from dotenv import load_dotenv
load_dotenv()


client = NotionClient(token_v2=os.getenv("TOKEN_V2"))


def add_ticket(issue):
    db = client.get_collection_view(os.getenv("COLLECTION"))
    title = issue["title"]
    number = issue["number"]

    ticket = db.collection.add_row()
    ticket.assign = list(map(lambda assignee: get_user(
        client, assignee["login"]), issue["assignees"]))

    if (len(ticket.assign) > 0):
        ticket.status = 'Not started'
    else:
        ticket.status = 'Backlog'
    ticket.title = f"#{number} {title}"
