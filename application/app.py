from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, Flask!'

# Run the application if the script is executed directly
if __name__ == '__main__':
    # Set the debug mode to True for development
    app.run(debug=True)
