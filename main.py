from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

nfts = {}


@app.get("/{id}")
def get_nft(id: str):
    global nfts
    r = nfts.get(id)
    if not r:
        raise HTTPException(status_code=404, detail="Item not found")
    return r


def get_cat_fact():
    r = httpx.get("https://catfact.ninja/fact")
    return r.json()["fact"]


@app.post("/add/{item_id}")
def mint_nft(item_id: str):
    global nfts
    nfts[item_id] = {"text": get_cat_fact()}
