# setup_executable.py
# Script para configurar empaquetado con PyInstaller (simplificado)

import os
import sys

def create_icon():
    """Crear icono simple sin dependencias de PIL"""
    # Por ahora, no crear icono si PIL no está disponible
    # El usuario puede proporcionar su propio .ico
    icon_path = "media_downloader_icon.ico"
    
    if os.path.exists(icon_path):
        print(f"✅ Icono existente encontrado: {icon_path}")
        return icon_path
    else:
        print(f"⚠️  No se encontró icono. Puedes:")
        print(f"   1. Crear tu propio {icon_path}")
        print(f"   2. O continuar sin icono personalizado")
        return None

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
