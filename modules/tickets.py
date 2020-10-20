from .user import get_user
from .client import board


def add_ticket(issue):
    title = issue["title"]
    number = issue["number"]

    ticket = board.collection.add_row()

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
