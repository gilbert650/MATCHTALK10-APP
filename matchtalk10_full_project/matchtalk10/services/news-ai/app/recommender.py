import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_articles(articles, sports=None, teams=None, players=None, exclude=None, limit=10):
    sports={x.lower() for x in (sports or [])}; teams={x.lower() for x in (teams or [])}
    players={x.lower() for x in (players or [])}; exclude=set(exclude or [])
    rows=[a for a in articles if a["id"] not in exclude]
    if not rows: return []
    df=pd.DataFrame(rows)
    df["text"]=(df["title"].fillna("")+" "+df["summary"].fillna("")+" "+df["sport"].fillna("")+" "+df["topics"].apply(lambda x:" ".join(x))+" "+df["teams"].apply(lambda x:" ".join(x))+" "+df["players"].apply(lambda x:" ".join(x))).str.lower()
    try:
        matrix=TfidfVectorizer(stop_words="english").fit_transform(df["text"])
        sim=cosine_similarity(matrix).mean(axis=1)
    except ValueError: sim=[0.0]*len(df)
    out=[]
    for i,row in df.iterrows():
        score=float(sim[i])*.15; reasons=[]
        if row["sport"].lower() in sports: score+=3; reasons.append("followed sport")
        mt=teams.intersection(x.lower() for x in row["teams"])
        if mt: score+=5*len(mt); reasons.append("followed team")
        mp=players.intersection(x.lower() for x in row["players"])
        if mp: score+=4*len(mp); reasons.append("followed player")
        out.append({"article_id":row["id"],"title":row["title"],"url":row.get("url",""),"score":round(score,4),"reasons":reasons or ["general relevance"]})
    return sorted(out,key=lambda x:x["score"],reverse=True)[:limit]
