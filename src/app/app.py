from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    code = request.args.get('code')

    return f'Authorization code: {code}', 200

@app.route('/home')
def home():
    pass

app.run(port=3000)