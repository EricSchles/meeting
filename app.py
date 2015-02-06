from flask import Flask, redirect, jsonify

app = Flask(__name__)

@app.route("/<login>")
def log_on(login):
    if login == "palantir":
        return redirect(url_for("palantir"))
    else:
        return "Nothing to see here"

@app.route("/palantir")
def palantir():
    return jsonify({
    "test":"true"
})

if __name__ == "__main__":
    app.run(debug=True)
