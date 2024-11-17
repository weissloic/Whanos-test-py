from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Tek Nancy > Tek Lyon...'

app.run(host='0.0.0.0', port=8180)
