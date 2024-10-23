from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from sms_manager import manage_sessions, get_metrics, add_country_operator, remove_country_operator
from alerts import send_telegram_alert

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Sample login for authentication
@app.route('/login', methods=['POST'])
def login():
    if request.json.get("username") == "admin" and request.json.get("password") == "admin":
        token = create_access_token(identity="admin")
        return jsonify(access_token=token), 200
    return jsonify({"msg": "Bad credentials"}), 401

# Manage SMS sessions
@app.route('/sms/manage/<action>', methods=['POST'])
def manage_sms_sessions(action):
    if action in ['start', 'stop', 'restart']:
        country_operator = request.json.get("country_operator")
        manage_sessions(action, country_operator)
        return jsonify({"msg": f"Session {action}ed"}), 200
    return jsonify({"msg": "Invalid action"}), 400

# Get real-time metrics
@app.route('/sms/metrics', methods=['GET'])
def get_sms_metrics():
    return jsonify(get_metrics()), 200

# Add or remove country-operator pairs
@app.route('/country-operator', methods=['POST', 'DELETE'])
def modify_country_operator():
    if request.method == 'POST':
        data = request.json
        add_country_operator(data)
    else:
        country_operator = request.json.get("country_operator")
        remove_country_operator(country_operator)
    return jsonify({"msg": "Operation successful"}), 200

# Alerts (Example for Telegram notifications)
@app.route('/alerts', methods=['POST'])
def alert():
    message = request.json.get("message")
    send_telegram_alert(message)
    return jsonify({"msg": "Alert sent"}), 200

if __name__ == "__main__":
    app.run(debug=True)
