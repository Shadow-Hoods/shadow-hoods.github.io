#/bin/python3

import flask, requests

app = flask.Flask(__name__, template_folder="./")
token = "ODIzOTgxMjQ0NDk2MzQ3MTY3.YFouVQ.iZJKCHAaRhXDKy7DR6NeNqMaVDE"  # ce token est celui de mon bot, vous pouvez le changer.

@app.route("/")
def main():
    everyone = requests.get('https://canary.discord.com/api/v10/guilds/751580453634310284/members?limit=1000', headers={'Content-Type': 'application/json', 'Authorization': f'Bot {token}'}).json()
    return flask.render_template("index.html", everyone=len(everyone), members=len([l for l in everyone if 'bot' not in list(l['user'].keys())]), bots=len([l for l in everyone if 'bot' in list(l['user'].keys())]))

@app.route("/<path:file>")
def upload(file):
    return flask.send_file(file)

app.run(host='0.0.0.0', port=8080)