from fastapi import FastAPI
from fetch_scores import fetch_live_score

app = FastAPI()

# Updated endpoint to return live scores
@app.get("/live-scores")
def get_live_scores():
    return fetch_live_score()

# New route: homepage
@app.get("/")
def read_root():
    return {"message": "Welcome to the Cricket Score API"}

# New route: alias or info
@app.get("/live-score")
def single_score():
    return {"message": "Try using /live-scores instead"}

# New route: basic view
@app.get("/view")
def view_scores():
    return {"message": "This would be a UI page in the future."}
