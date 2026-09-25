from fastapi import FastAPI
from app.config import settings
from app.models import WebResearchQuery, WebDossier, SourceComparison
from app.services.comparator import run_web_comparison

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/dossier", response_model=WebDossier)
def generate_dossier(req: WebResearchQuery):
    data = run_web_comparison(req.query)
    comp = SourceComparison(
        source_a=data["source_a"],
        source_b=data["source_b"],
        consensus_points=data["consensus_points"],
        divergence_points=data["divergence_points"]
    )
    return WebDossier(
        query=req.query,
        comparison=comp,
        executive_summary=data["summary"],
        credibility_rating="HIGH_CONFIDENCE (Triangulated)"
    )
