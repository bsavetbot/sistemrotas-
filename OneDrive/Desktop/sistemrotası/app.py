from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Sistem Rotası çalışıyor!"

if __name__ == '_ _main_ _':
    app.run()