from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(): return {"message": "hello gnuvil"}

@app.get("/search")
def search(q: str, limit: int=10): return {"query": q, "limit": limit}