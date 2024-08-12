from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import httpx
import pytest

client = TestClient(app)

# def test_is_server_real():
#     url = "http://testserver/"
#     r = httpx.get(url)
#     assert r == 1


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization", "host"],
        "ignore_localhost": True,
        "ignore_hosts": ["testserver"],
        # "record_mode": "once",
    }


@pytest.mark.vcr()
def test_mint_nft():
    r3 = client.get("/1")
    assert r3.status_code == 404

    r = client.post("/add/1")
    assert r.status_code == 200

    r1 = client.get("/1")
    assert r1.status_code == 200
    assert r1.json()["text"] == "Normal body temperature for a cat is 102 degrees F."


@pytest.mark.vcr()
def test_iana():
    response = httpx.get('http://www.iana.org/domains/reserved')
    assert response.status_code == 200
