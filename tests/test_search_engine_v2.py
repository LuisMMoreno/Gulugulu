import os
import unittest
from core.search.search_engine import SearchEngineV2
from core.knowledge.graph_engine import KnowledgeGraphEngine, RecommendationEngine

class TestSearchEngineV2(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.getcwd(), 'database.db')
        self.engine = SearchEngineV2(self.db_path)
        self.graph = KnowledgeGraphEngine(self.db_path)
        self.recommender = RecommendationEngine(self.db_path)

    def test_tokenize(self):
        tokens = self.engine.expander.expand("Matemáticas grado 1 sumas")
        self.assertIn("matemáticas", tokens)
        self.assertIn("grado", tokens)
        self.assertIn("1", tokens)
        self.assertIn("sumas", tokens)

    def test_autocomplete(self):
        res = self.engine.autocomplete("mat")
        self.assertIsInstance(res, list)

    def test_search_v2_structure(self):
        results = self.engine.search("ciencias")
        self.assertIsInstance(results, list)
        if results:
            first = results[0]
            self.assertIn('title', first)
            self.assertIn('pedagogical_id', first)
            self.assertIn('subject_name', first)
            self.assertIn('grade_name', first)

    def test_graph_and_recommendations(self):
        # Test engine initializes and queries without unhandled exception
        related = self.graph.get_related(1)
        self.assertIsInstance(related, list)
        recs = self.recommender.recommend_for_lo(1, limit=3)
        self.assertIsInstance(recs, list)

if __name__ == '__main__':
    unittest.main()
