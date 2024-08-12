from fastapi import FastAPI
from fastapi.testclient import TestClient
from testcontainers.compose.compose import DockerCompose
from main import app
import httpx
import pytest
import redis
import os
# from testcontainers.redis import RedisContainer
from testcontainers.compose import DockerCompose

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

@pytest.fixture()
def redis_db():
    if not os.environ.get("SKIP_CONTAINERS"):
        with DockerCompose(".", compose_file_name="docker-compose.yml") as dc:
            db = redis.Redis(host='localhost', port=6379, db=0)
            # init
            yield db
            # teardown
            db.flushdb()
    else:
        yield None
        db = redis.Redis(host='localhost', port=6379, db=0)
        db.flushdb()

@pytest.mark.vcr()
def test_mint_nft(redis_db):
    # clear redis db
    r3 = client.get("/1")
    assert r3.status_code == 404

    r = client.post("/add/1")
    assert r.status_code == 200

    r1 = client.get("/1")
    assert r1.status_code == 200
    assert r1.json()["text"] == "Normal body temperature for a cat is 102 degrees F."
    # compose.


@pytest.mark.vcr()
def test_iana():
    response = httpx.get('http://www.iana.org/domains/reserved')
    assert response.status_code == 200
    
def test_redis(redis_db):
    # set value in redis, running in localhost
    # key is key, value is 123
    # use python client
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('key', '123')
