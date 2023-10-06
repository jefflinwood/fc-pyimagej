from flask import Flask
import imagej

app = Flask(__name__)

@app.route('/')
def index():
    ij = imagej.init("2.14.0")
    print(ij.getVersion())
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
