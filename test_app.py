from app import app

def test_home():
    r = app.test_client().get("/")
    assert r.status_code == 200
    assert b"Bye" in r.data

def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_metrics():
    r = app.test_client().get("/metrics")
    assert r.status_code == 200
    assert b"app_requests_total" in r.data
