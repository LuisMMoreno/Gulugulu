import unittest
from app import app, get_db_connection

class TestAuth(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_dashboard_requires_login(self):
        res = self.client.get('/admin/dashboard')
        self.assertEqual(res.status_code, 302)
        self.assertIn('/admin', res.headers.get('Location', ''))

    def test_login_invalid_credentials(self):
        res = self.client.post('/admin/login', data={
            'username': 'fake_user_xyz',
            'password': 'wrong_password_123'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        html = res.data.decode('utf-8')
        self.assertIn('Usuario o contraseña incorrectos', html)

    def test_login_valid_admin(self):
        with self.client:
            res = self.client.post('/admin/login', data={
                'username': 'admin',
                'password': 'admon123*'
            }, follow_redirects=False)
            self.assertEqual(res.status_code, 302)
            self.assertIn('/admin/dashboard', res.headers.get('Location', ''))

            # Check dashboard renders for authenticated admin
            dash_res = self.client.get('/admin/dashboard')
            self.assertEqual(dash_res.status_code, 200)
            dash_html = dash_res.data.decode('utf-8')
            self.assertIn('Gulugulu', dash_html)
            self.assertIn('data-lucide', dash_html)
            self.assertNotIn('material-symbols-outlined', dash_html)

            # Test logout
            logout_res = self.client.get('/logout')
            self.assertEqual(logout_res.status_code, 302)

            # Dashboard should redirect again
            dash_after = self.client.get('/admin/dashboard')
            self.assertEqual(dash_after.status_code, 302)

    def test_unauthorized_admin_actions(self):
        # Without login, POST actions must be rejected
        res = self.client.post('/admin/create_user', data={
            'cedula': '99999',
            'name': 'Test',
            'username': 'test',
            'password': '123'
        })
        self.assertIn(res.status_code, [401, 302])

        res_backup = self.client.post('/admin/backup/create')
        self.assertIn(res_backup.status_code, [401, 302])

if __name__ == '__main__':
    unittest.main()

