from pydantic import BaseModel
from typing import List, Dict

class WebResearchQuery(BaseModel):
    query: str
    target_domains: List[str] = ["github.com", "arxiv.org", "erhatechnologies.com"]

class SourceComparison(BaseModel):
    source_a: str
    source_b: str
    consensus_points: List[str]
    divergence_points: List[str]

class WebDossier(BaseModel):
    query: str
    comparison: SourceComparison
    executive_summary: str
    credibility_rating: str
