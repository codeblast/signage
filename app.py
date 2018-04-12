from flask import Flask, send_from_directory

from api.checkin import checkin

app = Flask(__name__)
app.register_blueprint(checkin)


@app.route('/')
def hello():
    return 'Try <a href="/pages/checkin.html">checkin.html</a>'


@app.route('/pages/<path:path>')
def send_pages(path):
    return send_from_directory('pages', path)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
