import pytest
from src.app import create_app
from src.config import db

@pytest.fixture(scope="session")
def app():
    """
    Crea la aplicación Flask configurada para pruebas.
    Usa SQLite en memoria para no alterar datos reales.
    """
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """
    Cliente de prueba que permite enviar requests a los endpoints.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Runner para comandos de la CLI de Flask.
    """
    return app.test_cli_runner()
