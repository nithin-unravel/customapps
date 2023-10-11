import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the target endpoint where you want to send the response
target_endpoint = "https://unraveldata.xmatters.com/api/integration/1/functions/9010ef5f-8d9e-4873-8f67-1f7bf838cbe7/triggers?apiKey=d6a4c761-367f-47d4-9fd6-fdaf09c2fb65&recipients=nkollu"

@app.route('/json-endpoint', methods=['POST'])
def json_endpoint():
    # Get the JSON data from the request
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400

    # Extract relevant values from the incoming JSON data
    policy_url = data.get("policy_url", "")
    trigger_condition = data.get("trigger_condition", "")
    recent_violations = data.get("recent_violations", "")
    subject = data.get("subject", "")

    # Create the new JSON response
    response = {
        "recipients": "nkollu",
        "summary": f"An alert was triggered with Policy URL: {policy_url}, Trigger Condition: {trigger_condition}, Recent Violations: {recent_violations}",
        "description": subject,
        "priority": "MEDIUM"
    }

    # Send the response to the target endpoint
    response_to_target = requests.post(target_endpoint, json=response)

    if response_to_target.status_code == 200:
        return jsonify({'message': 'Response sent successfully to the target endpoint'})
    else:
        return jsonify({'error': 'Failed to send the response to the target endpoint'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

