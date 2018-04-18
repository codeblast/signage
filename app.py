from flask import Flask, send_from_directory

from api.checkin import checkin

app = Flask(__name__)
app.register_blueprint(checkin)


@app.route('/')
def hello():
    # TODO(glombard): figure out how to deal with this 8080 vs 80 port split
    return ('<a href="/admin/checkin.html">Activate check-in</a> '
    	    'or <a href="http://localhost/pages/checkin.html">view FIDS page</a>?')


@app.route('/admin/<path:path>')
def send_admin(path):
    return send_from_directory('admin', path)


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
