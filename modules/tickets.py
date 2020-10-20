import os
from .user import get_user
from .client import client


def add_ticket(issue):
    db = client.get_collection_view(os.environ.get("COLLECTION"))
    title = issue["title"]
    number = issue["number"]

    ticket = db.collection.add_row()

    assigned = []
    for assignee in issue["assignees"]:
        user = get_user(assignee["login"])
        if user:
            assigned.append(user)

    ticket.assign = assigned

    if (len(ticket.assign) > 0):
        ticket.status = 'Not started'
    else:
        ticket.status = 'Backlog'
    ticket.title = f"#{number} {title}"
