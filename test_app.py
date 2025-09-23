import unittest
import json
from app import app, downloader

class TikTokDownloaderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test que la página principal carga correctamente"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TikTok Downloader', response.data)

    def test_health_endpoint(self):
        """Test del endpoint de salud"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'OK')

    def test_preview_without_url(self):
        """Test de vista previa sin URL"""
        response = self.app.post('/preview', 
                                json={})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_preview_invalid_url(self):
        """Test de vista previa con URL inválida"""
        response = self.app.post('/preview', 
                                json={'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('error', data)
        self.assertIn('TikTok', data['error'])

    def test_download_without_url(self):
        """Test de descarga sin URL"""
        response = self.app.post('/download_direct', 
                                json={})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_download_invalid_url(self):
        """Test de descarga con URL inválida"""
        response = self.app.post('/download_direct', 
                                json={'url': 'https://example.com'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('error', data)

    def test_delete_nonexistent_file(self):
        """Test de eliminación de archivo inexistente"""
        response = self.app.get('/delete_file/nonexistent.mp4')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()