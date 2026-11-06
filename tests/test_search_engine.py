import os
import unittest
from search_engine import SearchEngine

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.bd_path = os.path.join(os.getcwd(), 'BD')
        self.engine = SearchEngine(self.bd_path)

    def test_file_type_detection(self):
        self.assertEqual(self.engine.get_file_type('foto.jpg'), 'image')
        self.assertEqual(self.engine.get_file_type('foto.jpeg'), 'image')
        self.assertEqual(self.engine.get_file_type('dibujo.png'), 'image')
        self.assertEqual(self.engine.get_file_type('clip.mp4'), 'video')
        self.assertEqual(self.engine.get_file_type('cancion.mp3'), 'audio')
        self.assertEqual(self.engine.get_file_type('guia.pdf'), 'pdf')
        self.assertEqual(self.engine.get_file_type('trabajo.docx'), 'word')
        self.assertEqual(self.engine.get_file_type('notas.txt'), 'text')

    def test_format_size(self):
        self.assertEqual(self.engine.format_size(500), '500 B')
        self.assertEqual(self.engine.format_size(2048), '2 KB')
        self.assertEqual(self.engine.format_size(1024 * 1024 * 5), '5.0 MB')

    def test_synonyms_loaded(self):
        self.assertIsInstance(self.engine.synonyms, dict)
        if os.path.exists('synonyms.json'):
            self.assertGreater(len(self.engine.synonyms), 0)

    def test_search_empty_query(self):
        results = self.engine.search('')
        self.assertEqual(results, [])
        results_spaces = self.engine.search('   ')
        self.assertEqual(results_spaces, [])

    def test_search_indexing(self):
        self.assertIsInstance(self.engine.index, list)
        self.assertGreaterEqual(len(self.engine.index), 0)

if __name__ == '__main__':
    unittest.main()

