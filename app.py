from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to TrueThread!</h1><p>Social media for the people.</p>"

if __name__ == '__main__':
    app.run(debug=True)
