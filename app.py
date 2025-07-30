from flask import Flask, jsonify  # Flask is used to create the web server, jsonify formats JSON responses
import json  # For reading and parsing the config_data.json file

# Create a Flask web application instance
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
    """
    GET endpoint to retrieve configuration data from config_data.json.
    Returns:
        - 200 OK with JSON data if file exists and is readable
        - 404 Not Found if the file is missing
        - 500 Internal Server Error for any unexpected error
    """
    try:
        # Open and load the JSON data from the file
        with open("config_data.json", "r") as f:
            data = json.load(f)
        
        # Return the data as a JSON response with HTTP 200 status
        return jsonify(data), 200

    except FileNotFoundError:
        # Handle missing file scenario
        return jsonify({"error": "Config JSON file not found"}), 404

    except Exception as e:
        # Handle any other unexpected error
        return jsonify({"error": str(e)}), 500

# Entry point of the script to run the Flask development server
if __name__ == "__main__":
    # Run the Flask app in debug mode (useful for development)
    app.run(debug=True)
