from flask import request
from enum import Enum


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


def get_action():
    event = request.headers.get('X-GitHub-Event')
    body = request.json

    if event == GitHubEvent.Issues and body["action"] == "opened":
        return Action.AddTicket
    elif event == GitHubEvent.Create and body["ref_type"] == "branch":
        return Action.InProgress

    return Action.Unknown
