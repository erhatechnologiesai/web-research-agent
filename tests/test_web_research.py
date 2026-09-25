import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestWebResearchAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_dossier_endpoint(self):
        res = self.client.post("/dossier", json={"query": "Multi-agent coordination protocols"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["credibility_rating"], "HIGH_CONFIDENCE (Triangulated)")
        self.assertGreater(len(data["comparison"]["consensus_points"]), 0)

if __name__ == "__main__":
    unittest.main()
