from fastapi import FastAPI

app = FastAPI()


@app.get("/{id}")
def get_nft(id):
    return {"text": "foo"}
    # return {"Hello": "World!!!!"}


@app.post("/add/{item_id}")
def mint_nft(item_id: int):
    return {"item_id": item_id}
