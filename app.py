from flask import Flask, request
import requests

app = Flask("Cisco")


@app.route("/ping", methods=("POST",))
def ping():
    try:
        response = requests.get(request.json["url"], verify=False)
        payload = response.content
    except Exception as exception:
        payload = {"message": f"Bad request: {exception}"}
    return payload


@app.route("/info")
def info():
    return {"Receiver": "Cisco is the best!"}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
