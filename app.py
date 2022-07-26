from flask import Flask

from blueprints.loader.loader import loader_bp
from blueprints.main.main import main_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(loader_bp)

if __name__ == '__main__':
    app.run(host='127.0.0.3', port=7000, debug=True)
