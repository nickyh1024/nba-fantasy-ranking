from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Define a route (URL endpoint) for the root of the site
@app.route('/')
def index():
    # Return a JSON response
    return jsonify({"message": "Welcome to NBA Fantasy Rankings API!"})

# Run the app when this file is executed
if __name__ == '__main__':
    app.run(debug=True)
