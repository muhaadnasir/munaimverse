from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.routes import main_bp
    from app.projects.routes import projects_bp
    from .blogs.routes import blogs_bp
    from .myArts.routes import my_arts_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)
    app.register_blueprint(blogs_bp)
    app.register_blueprint(my_arts_bp)
    return app