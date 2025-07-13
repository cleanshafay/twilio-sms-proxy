from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth
import os

app = Flask(__name__)

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")

@app.route("/send-sms", methods=["POST"])
def send_sms():
    data = request.get_json()

    payload = {
        "To": data.get("To"),
        "From": data.get("From"),
        "Body": data.get("Body")
    }

    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"
    response = requests.post(
        url,
        data=payload,
        auth=HTTPBasicAuth(TWILIO_SID, TWILIO_AUTH)
    )

    return jsonify({
        "status": response.status_code,
        "twilio_response": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
