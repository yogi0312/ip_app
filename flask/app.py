from flask import Flask
import socket

# Create Flask application
app = Flask(__name__)

# Define Route for home page
@app.route("/")
def get_ip():

    # Get hostname
    hostname = socket.gethostname()

    # Get IP address
    ip_address = socket.gethostbyname(hostname)

    # Return IP address
    return f"The IP address is: {ip_address}"

# Define Route for greeting page
@app.route("/greet")
def say_hello():

    # Return greeting message
    return "Hi how are you"

# Main entry point
if __name__ == "__main__":

    # Run Flask application
    app.run(host="0.0.0.0", port=5000)