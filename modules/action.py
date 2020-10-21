from flask import request
from enum import Enum
import re


class Action(Enum):
    AddTicket = "add_ticket"
    InProgress = "in_progress"
    Review = "review"
    Close = "close"
    Unknown = "unknown"


class GitHubEvent(Enum):
    Issues = "issues"
    PullRequest = "pull_request"
    Create = "create"


def parse():
    event = request.headers.get('X-GitHub-Event')
    body = request.json

    action = Action.Unknown

    if event == GitHubEvent.Issues and body.get("action") == "opened":
        return (Action.AddTicket, None)
    elif event == GitHubEvent.Create and body.get("ref_type") == "branch":
        branch_name = body.get("ref")
        action = Action.InProgress
    elif event == GitHubEvent.PullRequest:
        pr_action = body.get("action")
        pr = body.get("pull_request")
        branch_name = pr.get("head").get("ref")
        if pr_action == "closed":
            action = Action.Close if pr.get("merged") else Action.InProgress
        elif pr_action == "review_requested":
            action = Action.Review
    else:
        return (Action.Unknown, None)

    name = re.search(r"#\d+", branch_name)
    return (action, name.group()[1:]) if name else (Action.Unknown, None)
