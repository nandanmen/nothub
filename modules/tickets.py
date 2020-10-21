from flask import request
from .action import Action
from .client import board
from .user import get_user
import re


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


def update_ticket(ticket_number, action):
    ticket = get_ticket(ticket_number)
    if ticket:
        if action == Action.InProgress:
            ticket.status = "In progress"
        elif action == Action.Review:
            ticket.status = "Review"
        elif action == Action.Close:
            ticket.status = "Completed"


def get_ticket(ticket_number):
    rows = board.collection.get_rows()
    for row in rows:
        if row.title.startswith(f"#{ticket_number}"):
            return row


def get_ticket_number(action):
    body = request.json
    if action == Action.InProgress:
        branch_name = body.get("ref")
    elif action in [Action.Close, Action.Review]:
        pr = body.get("pull_request")
        branch_name = pr.get("head").get("ref")
    else:
        return None

    name = re.search(r"#\d+", branch_name)
    if name:
        return name.group()[1:]
