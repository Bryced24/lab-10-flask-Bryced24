import os

import psycopg2
from flask import Flask

DATABASE_URL = os.environ.get('DATABASE_URL')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Bryce Davis in 3308'
