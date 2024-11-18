from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloIndex():
    return 'Tek Lyon > Tek Nancy'

app.run(host='0.0.0.0', port=8180)
