# setup_executable.py
# Script para crear ejecutable y generar icono

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import subprocess

def create_icon():
    """Crear icono personalizado con gato y símbolo de descarga"""
    # Crear imagen de 256x256 para el icono
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Fondo circular gradiente
    for i in range(size//2):
        alpha = int(255 * (1 - i/(size//2)))
        color = (108, 92, 231, alpha)  # Color púrpura con transparencia
        draw.ellipse([i, i, size-i, size-i], fill=color)
    
    # Fondo sólido circular
    draw.ellipse([20, 20, size-20, size-20], fill=(108, 92, 231, 255))
    draw.ellipse([25, 25, size-25, size-25], fill=(255, 255, 255, 255))
    
    try:
        # Intentar usar una fuente del sistema
        font_large = ImageFont.truetype("seguiemj.ttf", 80)  # Emoji font
        font_medium = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        try:
            # Fuente alternativa
            font_large = ImageFont.truetype("arial.ttf", 60)
            font_medium = ImageFont.truetype("arial.ttf", 30)
            font_small = ImageFont.truetype("arial.ttf", 18)
        except:
            # Fuente por defecto
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
    
    # Dibujar gato en el centro
    cat_emoji = "🐱"
    try:
        # Intentar dibujar emoji
        draw.text((size//2, size//2-20), cat_emoji, font=font_large, 
                 fill=(108, 92, 231, 255), anchor="mm")
    except:
        # Si no funciona el emoji, usar texto
        draw.text((size//2, size//2-20), "CAT", font=font_medium, 
                 fill=(108, 92, 231, 255), anchor="mm")
    
    # Símbolo de descarga (flecha hacia abajo)
    arrow_points = [
        (size//2-15, size//2+40),
        (size//2+15, size//2+40),
        (size//2+15, size//2+25),
        (size//2+25, size//2+35),
        (size//2, size//2+55),
        (size//2-25, size//2+35),
        (size//2-15, size//2+25)
    ]
    draw.polygon(arrow_points, fill=(0, 184, 148, 255))
    
    # Texto "DL" (Download)
    try:
        draw.text((size//2, size//2+75), "DL", font=font_small, 
                 fill=(108, 92, 231, 255), anchor="mm")
    except:
        pass
    
    # Guardar en diferentes tamaños para Windows
    sizes = [16, 32, 48, 64, 128, 256]
    icon_path = "media_downloader_icon.ico"
    
    # Crear archivo ICO con múltiples tamaños
    img.save(icon_path, format='ICO', sizes=[(s, s) for s in sizes])
    print(f"✅ Icono creado: {icon_path}")
    
    return icon_path

def create_spec_file(icon_path):
    """Crear archivo .spec personalizado para PyInstaller"""
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['compact_media_downloader.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'yt_dlp',
        'yt_dlp.extractor',
        'yt_dlp.downloader',
        'yt_dlp.postprocessor',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'threading',
        'urllib3',
        'certifi',
        'websockets'
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

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
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin ventana de consola
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='{icon_path}',
    version='version_info.txt'
)
'''
    
    with open('media_downloader.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Archivo .spec creado: media_downloader.spec")

def create_version_info():
    """Crear archivo de información de versión"""
    version_content = '''# UTF-8
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Media Tools'),
        StringStruct(u'FileDescription', u'Descargador de Medios - Herramienta para descargar contenido multimedia'),
        StringStruct(u'FileVersion', u'1.0.0.0'),
        StringStruct(u'InternalName', u'MediaDownloader'),
        StringStruct(u'LegalCopyright', u'© 2025 Media Tools. Herramienta gratuita.'),
        StringStruct(u'OriginalFilename', u'MediaDownloader.exe'),
        StringStruct(u'ProductName', u'Media Downloader'),
        StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_content)
    
    print("✅ Información de versión creada: version_info.txt")

def create_build_script():
    """Crear script de construcción"""
    build_script = '''@echo off
echo 🚀 Construyendo ejecutable de Media Downloader...
echo.

echo 📦 Instalando dependencias necesarias...
pip install pyinstaller pillow yt-dlp

echo.
echo 🎨 Creando icono personalizado...
python setup_executable.py create_icon

echo.
echo 🔧 Construyendo ejecutable...
pyinstaller --clean media_downloader.spec

echo.
echo ✅ ¡Construcción completada!
echo 📁 El ejecutable está en: dist/MediaDownloader.exe
echo.
pause
'''
    
    with open('build.bat', 'w', encoding='utf-8') as f:
        f.write(build_script)
    
    print("✅ Script de construcción creado: build.bat")

def create_requirements():
    """Crear archivo requirements.txt"""
    requirements = '''yt-dlp>=2023.12.30
Pillow>=10.0.0
pyinstaller>=6.0.0
'''
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print("✅ Requirements creado: requirements.txt")

def main():
    """Función principal"""
    print("🎯 Configurando Media Downloader para ejecutable...")
    print("=" * 50)
    
    # Crear icono
    icon_path = create_icon()
    
    # Crear archivos necesarios
    create_spec_file(icon_path)
    create_version_info()
    create_build_script()
    create_requirements()
    
    print("\n" + "=" * 50)
    print("✅ ¡Configuración completada!")
    print("\n📋 Para crear el ejecutable:")
    print("1️⃣  Ejecuta: build.bat")
    print("2️⃣  O manualmente: pyinstaller --clean media_downloader.spec")
    print("\n📁 El ejecutable estará en: dist/MediaDownloader.exe")
    print("\n🛡️  El ejecutable incluye:")
    print("   • Información de versión profesional")
    print("   • Icono personalizado")
    print("   • Sin ventana de consola")
    print("   • Optimizado para evitar falsos positivos")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "create_icon":
        create_icon()
    else:
        main()
