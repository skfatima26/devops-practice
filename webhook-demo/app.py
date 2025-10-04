from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print(request.json)
    return "Webhook received", 200

if __name__ == "__main__":
    app.run(port=5000)
