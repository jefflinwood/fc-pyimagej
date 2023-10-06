from flask import Flask
import imagej

app = Flask(__name__)

@app.route('/')
def index():
    ij = imagej.init("2.5.0")
    print(ij.getVersion())
    return "Hello World!"

@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
