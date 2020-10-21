from flask import Flask, request

from modules.action import Action, get_action
import modules.tickets as tickets
from modules.util import validate_signature

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hello():
    return "Hello from notion integration!"


@app.route('/ticket', methods=['POST'])
def main():
    if not validate_signature():
        return ("SHA didn't match", 401)

    action = get_action()

    if action == Action.AddTicket:
        tickets.add_ticket(request.json["issue"])
    elif action in [Action.InProgress, Action.Review, Action.Close]:
        ticket_number = tickets.get_ticket_number(action)
        if ticket_number is not None:
            tickets.update_ticket(ticket_number, action)

    return ("", 204)
