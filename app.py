from flask import Flask, send_from_directory

from api.checkin import checkin

app = Flask(__name__)
app.register_blueprint(checkin)


@app.route('/')
def hello():
    return ('<a href="/admin/checkin.html">Activate check-in</a> '
    	    'or <a href="/pages/checkin.html">view FIDS page</a>?')


@app.route('/pages/<path:path>')
def send_pages(path):
    return send_from_directory('pages', path)


@app.route('/admin/<path:path>')
def send_admin(path):
    return send_from_directory('admin', path)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
