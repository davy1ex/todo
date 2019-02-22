import os
from flask import Flask


app = Flask()
app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run()
