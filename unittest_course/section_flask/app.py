from flask import Flask, jsonify
from config.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({'message': 'Hello world'})

if __name__ == '__main__':
    app.run()