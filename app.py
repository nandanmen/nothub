from flask import Flask, request
from flask_cors import CORS, cross_origin

from modules.action import Action, parse
from modules.util import validate_signature
from modules.client import board
import modules.tickets as tickets

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def hello():
    return "Hello from notion integration!"


@app.route('/ticket', methods=['POST'])
def main():
    if not validate_signature():
        return ("SHA didn't match", 401)

    action, ticket_number = parse()

    if action == Action.AddTicket:
        tickets.add_ticket(request.json["issue"])
    elif action in [Action.InProgress, Action.Review, Action.Close]:
        tickets.update_ticket(ticket_number, action)

    return ("", 204)


@app.route('/feedback', methods=['POST'])
@cross_origin()
def addFeedback():
    feedback = board.collection.add_row()
    body = request.json
    feedback.title = body["name"]
    feedback.message = body["message"]

    return ("", 201)
