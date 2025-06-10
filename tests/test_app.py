import json
from app import create_app


def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.get('/health')
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data['status'] == 'ok'


def test_hello_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello World' in resp.data
