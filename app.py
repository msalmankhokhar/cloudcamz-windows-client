from flask import Flask

app = Flask(__name__)

# importing routes
from routes.index import *
from routes.errors import *

host = '0.0.0.0'
port = 80

if __name__ == '__main__':
    app.run(host, port, debug=True)