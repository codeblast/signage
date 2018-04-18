from flask import Flask, redirect

from checkin import checkin

app = Flask(__name__)
app.register_blueprint(checkin)


@app.route('/')
def hello():
    return redirect('http://localhost:8081/admin/index.html')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
