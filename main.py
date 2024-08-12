from fastapi import FastAPI, HTTPException
import httpx
import redis

app = FastAPI()



@app.get("/{id}")
def get_nft(id: str):
    db = redis.Redis(host='localhost', port=6379, db=0)
    r = db.get(id)
    if not r:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"text": r}


def get_cat_fact():
    r = httpx.get("https://catfact.ninja/fact")
    return r.json()["fact"]


@app.post("/add/{item_id}")
def mint_nft(item_id: str):
    db = redis.Redis(host='localhost', port=6379, db=0)
    db.set(item_id, get_cat_fact())
