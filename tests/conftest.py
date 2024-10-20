from pytest import fixture
from starlette.testclient import TestClient
from app.main import app


@fixture(scope='function')
def api_client():
    client = TestClient(app=app)
    yield client
    client.close()


