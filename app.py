from flask import Flask, request
import modules.tickets as tickets

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def hello():
    return "Hello from the Notion integration!"


@app.route('/ticket', methods=['POST'])
def handleTicket():
    if request.json["action"] == "opened":
        tickets.add_ticket(request.json["issue"])

    return ("", 204)
