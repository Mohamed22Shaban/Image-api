from flask import Flask
from flask import bp as actionsbp

# 1)
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

# 3)
app.register_blueprint(actionsbp)