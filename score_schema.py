from pydantic import BaseModel
from typing import List

class MatchScore(BaseModel):
    match: str
    teams: str
    score: str

class ScoreResponse(BaseModel):
    matches: List[MatchScore]
