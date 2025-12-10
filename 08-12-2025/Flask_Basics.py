from flask import Flask
app = Flask(__name__)

@app.route("/get-item", methods=["GET"])
def get_item():
    return "Get Executed"
@app.route("/create-item", methods=["POST"])
def create_item():
    return "Post Executed"
@app.route("/update-item", methods=["PUT"])
def update_item():
    return "Put Executed"
@app.route("/delete-item", methods=["DELETE"])
def delete_item():
    return "Delete Executed"
if __name__ == "__main__":
    app.run()