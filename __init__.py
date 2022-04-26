from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    
    from views import dog_bp
    app.register_blueprint(dog_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)