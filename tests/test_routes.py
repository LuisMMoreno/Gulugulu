import os
import unittest
from app import app

class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home_page_visuals_and_icons(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        html = res.data.decode('utf-8')
        
        # Header text and font
        self.assertIn('Gulugulu', html)
        self.assertIn('suez-one.css', html)
        self.assertNotIn('/static/images/icono.png" alt="Gulu"', html)
        
        # Lucide iconography
        self.assertIn('data-lucide', html)
        self.assertNotIn('material-symbols-outlined', html)

    def test_results_page(self):
        res = self.client.get('/results?q=matematicas')
        self.assertEqual(res.status_code, 200)
        html = res.data.decode('utf-8')
        self.assertIn('Gulugulu', html)
        self.assertIn('suez-one.css', html)
        self.assertIn('data-lucide', html)
        self.assertNotIn('material-symbols-outlined', html)

    def test_minijuegos_page(self):
        res = self.client.get('/minijuegos')
        self.assertEqual(res.status_code, 200)
        html = res.data.decode('utf-8')
        self.assertIn('Gulugulu', html)
        self.assertIn('suez-one.css', html)
        self.assertIn('data-lucide', html)
        self.assertNotIn('material-symbols-outlined', html)

    def test_games_pages(self):
        for grado in [1, 2, 3, 4, 5]:
            res = self.client.get(f'/juego/{grado}/1')
            self.assertEqual(res.status_code, 200)
            html = res.data.decode('utf-8')
            self.assertIn('Gulugulu', html)
            self.assertIn('suez-one.css', html)
            self.assertIn('data-lucide', html)
            self.assertNotIn('material-symbols-outlined', html)

    def test_admin_login_page(self):
        res = self.client.get('/admin')
        self.assertEqual(res.status_code, 200)
        html = res.data.decode('utf-8')
        self.assertIn('Gulugulu', html)
        self.assertIn('data-lucide', html)
        self.assertNotIn('material-symbols-outlined', html)

    def test_search_api(self):
        res = self.client.get('/search?q=matematicas')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.is_json)

    def test_autocomplete_api(self):
        res = self.client.get('/autocomplete?q=cuaderno')
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.is_json)

    def test_security_directory_traversal(self):
        # Attempt to access files above directory
        res = self.client.get('/files/../../etc/passwd')
        self.assertIn(res.status_code, [400, 403, 404])
        res2 = self.client.get('/files/..%2F..%2Fapp.py')
        self.assertIn(res2.status_code, [400, 403, 404])

    def test_custom_404_handler(self):
        # API 404 should return JSON
        res_api = self.client.get('/api/v2/non_existent_endpoint')
        self.assertEqual(res_api.status_code, 404)
        self.assertTrue(res_api.is_json)

        # Web 404 should render template
        res_web = self.client.get('/ruta_inexistente_12345')
        self.assertEqual(res_web.status_code, 404)

if __name__ == '__main__':
    unittest.main()

