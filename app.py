""" Module that Create and host an endpoint,
    The endpoint take two GET request query parameters
    return specific information in JSON format.
"""

from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api_json():
    """ Module Method that Create and host the endpoint;
        take two GET request query parameters
        return specific information in JSON format.
    """

    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.now().strftime('%A')

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.utcnow()
    utc_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Include GitHub file URL and repository URL
    github_file_url = "https://github.com/Mubarak1A/HNGx-Stage1/app.py"
    github_repo_url = "https://github.com/Mubarak1A/HNGx-Stage1"

    # Validate the UTC time within +/-2 minutes
    utc_time_validation = datetime.timedelta(minutes=2)
    time_diff = current_time - datetime.datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%SZ')
    if abs(time_diff) > utc_time_validation:
        return jsonify({"error": "Invalid UTC time"}), 400

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
