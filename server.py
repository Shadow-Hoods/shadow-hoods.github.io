import flask

app = flask.Flask(__name__, template_folder="./")

@app.route("/")
def main():
    return flask.render_template("index.html")

app.run(host='0.0.0.0', port=8080)
