from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route to handle uppercase conversion
@app.route('/uppercase/<n>', methods=['GET'])
def convert_to_uppercase(n):
    # Convert the word to uppercase
   n= int(n)
   return f"{2**n}"

@app.route('/',methods=['GEt'])
def index():
    return "<h1>Server is Running</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

