from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import httpx

client = TestClient(app)

# def test_is_server_real():
#     url = "http://testserver/"
#     r = httpx.get(url)
#     assert r == 1


def test_mint_nft():
    r = client.post("/add/1")
    assert r.status_code == 200
    r1 = client.get("/1")

    assert r1.status_code == 200
    assert r1.json()["text"] == "foo"

