from flask import Flask

def create_app():
    app = Flask(
        __name__,
    static_folder="../static",
    )
   # app.config['SECRET_KEY'] = 'jlkw1232k45kerw3425rj'
   

    return app
