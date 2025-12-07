from flask import Flask, render_template, request, redirect, url_for
import uuid
import json
import os

app = Flask(__name__)

DATA_FILE = "bouquets.json"

# ----------------------- LOAD / SAVE ----------------------- #
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        postcards = json.load(f)
else:
    postcards = {}


def save_postcards():
    with open(DATA_FILE, "w") as f:
        json.dump(postcards, f, indent=4)


# ----------------------- HOME ---------------------------- #
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------- GLOBE SELECT -------------------- #
@app.route("/globes")
def globes():
    globe_ids = ["globe1", "globe2", "globe3", "globe4"]
    return render_template("globes.html", globes=globe_ids)


# ----------------------- WRITE MESSAGE -------------------- #
@app.route("/write", methods=["POST"])
def write():
    globe = request.form.get("globe")
    if not globe:
        return redirect(url_for("globes"))
    return render_template("write.html", globe=globe)


# ----------------------- PREVIEW PAGE --------------------- #
@app.route("/preview", methods=["POST"])
def preview():
    globe = request.form.get("globe")
    to_name = request.form.get("to_name")
    from_name = request.form.get("from_name")
    message = request.form.get("message")

    return render_template(
        "preview.html",
        globe=globe,
        to_name=to_name,
        from_name=from_name,
        message=message,
    )
# ---------------- HISTORY PAGE ---------------- #
@app.route("/history")
def history():
    return render_template("history.html", postcards=postcards)


# ----------------------- FINAL SEND ----------------------- #
@app.route("/final", methods=["POST"])
def final():
    globe = request.form.get("globe")
    to_name = request.form.get("to_name")
    from_name = request.form.get("from_name")
    message = request.form.get("message")

    postcard_id = str(uuid.uuid4())[:6]

    postcards[postcard_id] = {
        "globe": globe,
        "to": to_name,
        "from": from_name,
        "message": message
    }

    save_postcards()

    # Sender gets the sharing page
    return render_template(
        "final.html",
        postcard_id=postcard_id,
        globe=globe,
        to_name=to_name,
        from_name=from_name,
        message=message
    )


# ----------------------- RECEIVER LANDING ----------------------- #
@app.route("/reveal/<postcard_id>")
def reveal(postcard_id):
    """
    First page receiver sees.
    Only shows a message + button "View your bloom"
    """
    if postcard_id not in postcards:
        return "This winter whisper has melted away...", 404

    return render_template(
        "reveal.html",
        postcard_id=postcard_id
    )


# ----------------------- RECEIVER BLOOM PAGE ----------------------- #
@app.route("/bloom/<postcard_id>")
def bloom(postcard_id):
    """
    Final bloom page — shows globe + message
    """
    card = postcards.get(postcard_id)
    if not card:
        return "This winter whisper has melted away...", 404

    return render_template(
        "bloom.html",
        globe=card["globe"],
        to_name=card["to"],
        from_name=card["from"],
        message=card["message"]
    )


# ----------------------- RUN ----------------------- #
if __name__ == "__main__":
    app.run(debug=True)
