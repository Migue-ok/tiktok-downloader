# -*- mode: python ; coding: utf-8 -*-
# MediaDownloader - Configuración avanzada PyInstaller

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# Datos adicionales para yt-dlp
yt_dlp_datas = collect_data_files('yt_dlp')

# Módulos ocultos completos
hidden_imports = [
    # Core yt-dlp
    'yt_dlp',
    'yt_dlp.extractor',
    'yt_dlp.extractor.common',
    'yt_dlp.extractor.youtube',
    'yt_dlp.extractor.tiktok',
    'yt_dlp.extractor.instagram',
    'yt_dlp.extractor.facebook',
    'yt_dlp.downloader',
    'yt_dlp.downloader.http',
    'yt_dlp.postprocessor',
    'yt_dlp.postprocessor.ffmpeg',
    
    # Tkinter completo
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'tkinter.filedialog',
    'tkinter.font',
    
    # Dependencias de red
    'urllib3',
    'urllib3.util',
    'urllib3.util.retry',
    'urllib3.exceptions',
    'certifi',
    'ssl',
    'socket',
    'http.client',
    'http.cookiejar',
    
    # JSON y codificación
    'json',
    'base64',
    'hashlib',
    'hmac',
    
    # Sistema
    'threading',
    'subprocess',
    'tempfile',
    'shutil',
    
    # Imagen
    'PIL',
    'PIL.Image',
    'PIL.ImageTk',
    'PIL.ImageDraw',
    'PIL.ImageFont',
]

a = Analysis(
    ['compact_media_downloader.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=yt_dlp_datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Excluir librerías pesadas innecesarias
        'matplotlib', 'numpy', 'scipy', 'pandas',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'django', 'flask', 'tornado',
        'IPython', 'jupyter',
        'test', 'unittest', 'pytest',
        'pdb', 'pydoc',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Filtrar archivos innecesarios
def filter_binaries(binaries):
    filtered = []
    exclude_patterns = [
        'api-ms-win', 'ucrtbase', 'msvcp', 'vcruntime',
        'Qt5', 'Qt6', '_testcapi', 'tcl85', 'tk85'
    ]
    
    for binary in binaries:
        name = binary[0].lower()
        if not any(pattern in name for pattern in exclude_patterns):
            filtered.append(binary)
    
    return filtered

a.binaries = filter_binaries(a.binaries)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MediaDownloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[
        'vcruntime140.dll',
        'msvcp140.dll',
        'api-ms-win*.dll'
    ],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='media_downloader_icon.ico',
    version='version_info.txt'
)

# Post-procesamiento para limpiar archivos
import shutil
if os.path.exists('build'):
    shutil.rmtree('build')
