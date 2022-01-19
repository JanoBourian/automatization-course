from flask import Flask 

app = Flask(__name__)

app.config.from_pyfile("settings.py")

@app.route("/")
def home():
    return '<h1> Flask is most better than Django </h1>'

if __name__ == '__main__':
    host = '192.168.0.20'
    port = '8080'
    debug = True
    app.run(host=host, port= port, debug=debug)