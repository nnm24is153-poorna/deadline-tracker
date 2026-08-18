from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

deadlines = []
next_id = 1

@app.route('/deadlines', methods=['GET'])
def get_deadlines():
    return jsonify(deadlines)

@app.route('/deadlines', methods=['POST'])
def add_deadline():
    global next_id
    data = request.get_json()
    new_deadline = {
        "id": next_id,
        "title": data.get("title"),
        "due_date": data.get("due_date"),
        "status": "pending"
    }
    deadlines.append(new_deadline)
    next_id += 1
    return jsonify(new_deadline), 201

@app.route('/deadlines/<int:deadline_id>', methods=['PUT'])
def update_deadline(deadline_id):
    for d in deadlines:
        if d["id"] == deadline_id:
            d["status"] = "done"
            return jsonify(d)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)