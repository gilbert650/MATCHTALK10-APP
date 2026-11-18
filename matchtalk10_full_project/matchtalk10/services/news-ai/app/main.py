from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from .recommender import rank_articles
app=FastAPI(title="MatchTalk10 News Intelligence",version="1.0.0")
SAMPLES=[
 {"id":"a1","title":"Modern football pressing systems","summary":"Tactical analysis and transitions","sport":"football","teams":["Arsenal"],"players":[],"topics":["tactics"],"url":""},
 {"id":"a2","title":"Basketball defensive analytics","summary":"Metrics behind elite defence","sport":"basketball","teams":[],"players":[],"topics":["statistics"],"url":""},
 {"id":"a3","title":"Understanding tennis rankings","summary":"Tournament points and consistency","sport":"tennis","teams":[],"players":[],"topics":["rankings"],"url":""}
]
class Request(BaseModel):
 user_id:str
 followed_sports:List[str]=Field(default_factory=list)
 followed_teams:List[str]=Field(default_factory=list)
 followed_players:List[str]=Field(default_factory=list)
 previously_read_article_ids:List[str]=Field(default_factory=list)
 articles:List[dict]=Field(default_factory=list)
@app.get("/health")
def health(): return {"status":"ok","service":"matchtalk10-news-ai"}
@app.get("/recommendations")
def demo(user_id:str="anonymous"):
 return {"user_id":user_id,"mode":"demo-rule-based","items":rank_articles(SAMPLES,sports=["football"]),"notice":"Sample corpus only"}
@app.post("/recommendations/rank")
def rank(req:Request):
 if not req.articles: raise HTTPException(400,"Provide candidate articles")
 return {"user_id":req.user_id,"mode":"hybrid-baseline","items":rank_articles(req.articles,req.followed_sports,req.followed_teams,req.followed_players,req.previously_read_article_ids)}
