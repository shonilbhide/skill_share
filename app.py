from flask import Flask
from Routes.user_routes import user_blueprint
import DB

app = Flask(__name__)
DB.get_db()
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
