from flask import Flask, send_from_directory

 
app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World!'


@app.route('/pages/<path:path>')
def send_pages(path):
    return send_from_directory('pages', path)


if __name__ == '__main__':
  app.run(port=8080, host='0.0.0.0')
