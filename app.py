from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
import yt_dlp
import os
import tempfile
import time
from datetime import datetime
import uuid
import shutil
import json
import socket

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'tiktok_downloader_secret_key_2025')

# Configuración para producción
PORT = int(os.environ.get('PORT', 5000))
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Directorio para descargas temporales (en producción será temporal)
DOWNLOADS_DIR = os.path.join(tempfile.gettempdir(), 'tiktok_downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# Directorio temporal para descargas directas
TEMP_DIR = tempfile.mkdtemp()

class TikTokDownloader:
    def __init__(self):
        self.ydl_opts_direct = {
            'format': 'best[ext=mp4]/best',  # Mejor calidad disponible
            'outtmpl': os.path.join(TEMP_DIR, '%(id)s_%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'extractaudio': False,
            'audioformat': 'mp3',
            'embed_subs': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
        }
        
        self.ydl_opts_local = {
            'format': 'best[ext=mp4]/best',  # Mejor calidad disponible
            'outtmpl': os.path.join(DOWNLOADS_DIR, '%(uploader)s_%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'extractaudio': False,
            'audioformat': 'mp3',
            'embed_subs': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
        }
    
    def get_video_info(self, url):
        """Obtiene información del video sin descargarlo"""
        try:
            with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'Sin título')[:100],  # Limitar título
                    'uploader': info.get('uploader', 'Desconocido')[:50],
                    'duration': info.get('duration', 0),
                    'view_count': info.get('view_count', 0),
                    'like_count': info.get('like_count', 0),
                    'thumbnail': info.get('thumbnail', ''),
                    'formats': len(info.get('formats', [])),
                    'id': info.get('id', 'unknown')
                }
        except Exception as e:
            print(f"Error obteniendo info: {str(e)}")
            return None
    
    def download_for_direct(self, url):
        """Descarga el video para envío directo"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts_direct) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Buscar el archivo descargado
                video_id = info.get('id', 'unknown')
                title = info.get('title', 'video')
                
                # Buscar archivos que coincidan con el patrón
                for file in os.listdir(TEMP_DIR):
                    if video_id in file:
                        file_path = os.path.join(TEMP_DIR, file)
                        if os.path.exists(file_path):
                            return file_path, title[:50]  # Limitar nombre
                
                return None, None
        except Exception as e:
            print(f"Error en descarga directa: {str(e)}")
            return None, None
    
    def download_to_local(self, url):
        """Descarga el video a la carpeta temporal (simulando local en web)"""
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts_local) as ydl:
                info = ydl.extract_info(url, download=True)
                
                uploader = info.get('uploader', 'unknown')
                title = info.get('title', 'video')
                video_id = info.get('id', 'unknown')
                
                # Buscar archivos que coincidan
                for file in os.listdir(DOWNLOADS_DIR):
                    if video_id in file or (uploader in file and title[:20] in file):
                        file_path = os.path.join(DOWNLOADS_DIR, file)
                        if os.path.exists(file_path):
                            return file_path, title[:50]
                
                return None, None
        except Exception as e:
            print(f"Error en descarga local: {str(e)}")
            return None, None

downloader = TikTokDownloader()

@app.route('/')
def index():
    # Obtener lista de archivos "locales" (temporales en web)
    local_files = []
    if os.path.exists(DOWNLOADS_DIR):
        for file in os.listdir(DOWNLOADS_DIR):
            if file.endswith(('.mp4', '.webm', '.mkv', '.mov')):
                try:
                    file_path = os.path.join(DOWNLOADS_DIR, file)
                    file_size = os.path.getsize(file_path)
                    file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
                    local_files.append({
                        'name': file,
                        'size': f"{file_size / (1024*1024):.1f} MB",
                        'modified': file_modified.strftime("%Y-%m-%d %H:%M")
                    })
                except:
                    continue
    
    local_files.sort(key=lambda x: x['modified'], reverse=True)
    # Limitar a 20 archivos para evitar sobrecarga
    local_files = local_files[:20]
    
    return render_template('index.html', local_files=local_files)

@app.route('/preview', methods=['POST'])
def preview():
    try:
        data = request.get_json() if request.is_json else request.form
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL requerida'})
        
        if 'tiktok.com' not in url:
            return jsonify({'error': 'Solo se admiten URLs de TikTok'})
        
        info = downloader.get_video_info(url)
        if info:
            return jsonify({'success': True, 'info': info})
        else:
            return jsonify({'error': 'No se pudo obtener información del video'})
    except Exception as e:
        return jsonify({'error': f'Error del servidor: {str(e)}'})

@app.route('/download_direct', methods=['POST'])
def download_direct():
    try:
        data = request.get_json() if request.is_json else request.form
        url = data.get('url', '').strip()
        
        if not url or 'tiktok.com' not in url:
            return jsonify({'error': 'URL de TikTok válida requerida'})
        
        file_path, title = downloader.download_for_direct(url)
        
        if file_path and os.path.exists(file_path):
            def remove_file_after_send(response):
                try:
                    os.remove(file_path)
                except:
                    pass
                return response
            
            return send_file(
                file_path,
                as_attachment=True,
                download_name=f"{title}.mp4",
                mimetype='video/mp4'
            )
        else:
            return jsonify({'error': 'Error al descargar el video'})
    except Exception as e:
        return jsonify({'error': f'Error del servidor: {str(e)}'})

@app.route('/download_local', methods=['POST'])
def download_local():
    try:
        data = request.get_json() if request.is_json else request.form
        url = data.get('url', '').strip()
        
        if not url or 'tiktok.com' not in url:
            return jsonify({'error': 'URL de TikTok válida requerida'})
        
        file_path, title = downloader.download_to_local(url)
        
        if file_path and os.path.exists(file_path):
            return jsonify({'success': True, 'message': f'Video descargado: {title}'})
        else:
            return jsonify({'error': 'Error al descargar el video'})
    except Exception as e:
        return jsonify({'error': f'Error del servidor: {str(e)}'})

@app.route('/download_file/<filename>')
def download_file(filename):
    """Descarga un archivo de la carpeta temporal"""
    file_path = os.path.join(DOWNLOADS_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'Archivo no encontrado'}), 404

@app.route('/delete_file/<filename>')
def delete_file(filename):
    """Elimina un archivo de la carpeta temporal"""
    file_path = os.path.join(DOWNLOADS_DIR, filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return jsonify({'success': True, 'message': f'Archivo eliminado: {filename}'})
        except Exception as e:
            return jsonify({'error': f'Error al eliminar: {str(e)}'})
    else:
        return jsonify({'error': 'Archivo no encontrado'}), 404

@app.route('/health')
def health():
    """Endpoint de salud para monitoreo"""
    return jsonify({'status': 'OK', 'timestamp': datetime.now().isoformat()})

# Limpieza automática de archivos temporales
@app.teardown_appcontext
def cleanup_temp_files(error):
    """Limpia archivos temporales antiguos"""
    try:
        current_time = time.time()
        
        # Limpiar directorio temporal
        for file in os.listdir(TEMP_DIR):
            file_path = os.path.join(TEMP_DIR, file)
            if os.path.isfile(file_path):
                if current_time - os.path.getmtime(file_path) > 1800:  # 30 minutos
                    os.remove(file_path)
        
        # Limpiar directorio de descargas
        for file in os.listdir(DOWNLOADS_DIR):
            file_path = os.path.join(DOWNLOADS_DIR, file)
            if os.path.isfile(file_path):
                if current_time - os.path.getmtime(file_path) > 3600:  # 1 hora
                    os.remove(file_path)
    except:
        pass

if __name__ == '__main__':
    print("🚀 Iniciando TikTok Downloader...")
    print(f"📁 Directorio temporal: {DOWNLOADS_DIR}")
    print(f"🌐 Puerto: {PORT}")
    print(f"🔧 Debug: {DEBUG}")
    
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)