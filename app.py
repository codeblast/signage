from flask import Flask

from api.checkin import checkin

app = Flask(__name__)
app.register_blueprint(checkin)


@app.route('/')
def hello():
    # TODO(glombard): figure out how to deal with this 8080 vs 80 port split
    # so we don't have to hardcode the localhost here...
    return ('<a href="http://localhost:8081/admin/checkin.html">Activate check-in</a> '
    	    'or <a href="http://localhost/pages/checkin.html">view FIDS page</a>?')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
