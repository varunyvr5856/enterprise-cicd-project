
import app.main as main

def test_health():
    client = main.app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
