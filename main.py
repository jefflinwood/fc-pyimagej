from flask import Flask
import imagej

app = Flask(__name__)

@app.route('/')
def index():
    ij = imagej.init("2.5.0")
    version = ij.getVersion()
    return f'Hello World! ImageJ version: {version}'

@app.route('/health')
def health():
    return "OK"

def test_ij():
    ij = imagej.init("2.5.0")
    try:
        imp = ij.IJ.openImage("https://s3.amazonaws.com/soiling-test-bucket/test-folder/test-image.jpg")
        ij.py.from_java(imp.getDimensions())
        imp.close()
        return True
    except:
        return False

@app.route('/imageopen')
def imageopen():
   test_ij()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
