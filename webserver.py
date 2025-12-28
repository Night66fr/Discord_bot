from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return 'discord bot is fine'

def run():
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get("PORT", 3000))
    )

def keep_alive():
    Thread(target=run).start()
