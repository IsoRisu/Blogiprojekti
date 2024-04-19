from flask import Flask
from os import geten

app = Flask(__name__)

import routes

app.secret_key = getenv("SECRET_KEY")

