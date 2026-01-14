#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para empaquetar la aplicación con PyInstaller
Genera múltiples archivos en lugar de un solo ejecutable (más rápido y eficiente)
"""

import os
import sys
import subprocess
import shutil


def create_optimized_spec():
    """Crear .spec optimizado para empaquetado en múltiples archivos"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
# Configuración optimizada para empaquetado multi-archivo

block_cipher = None

a = Analysis(
    ['Youtube.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        # yt-dlp esenciales
        'yt_dlp',
        'yt_dlp.extractor',
        'yt_dlp.extractor.youtube',
        'yt_dlp.extractor.tiktok',
        'yt_dlp.extractor.instagram',
        'yt_dlp.extractor.facebook',
        'yt_dlp.downloader',
        'yt_dlp.downloader.http',
        'yt_dlp.postprocessor',
        
        # Tkinter
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        '_tkinter',
        
        # Red
        'urllib3',
        'urllib3.util',
        'urllib3.util.retry',
        'certifi',
        'ssl',
        'http.client',
        
        # Sistema
        'threading',
        'tempfile',
        'shutil',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'numpy', 'scipy', 'pandas',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'django', 'flask', 'tornado',
        'IPython', 'jupyter',
        'test', 'unittest', 'pytest',
        'PIL',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Separar en múltiples archivos (más eficiente)
exe = EXE(
    pyz,
    a.scripts,
    [],  # NO incluir a.binaries, a.zipfiles, a.datas aquí
    exclude_binaries=True,  # ESTO ES CLAVE para múltiples archivos
    name='ApayKuMedias',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # SIN VENTANA DE CONSOLA
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='media_downloader_icon.ico' if os.path.exists('media_downloader_icon.ico') else None,
)

# COLLECT crea el directorio con múltiples archivos
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[
        'vcruntime*.dll',
        'python*.dll',
        '_tkinter.pyd',
    ],
    name='ApayKuMedias',
)
'''
    
    with open('Youtube_multifile.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Archivo .spec multi-archivo creado: Youtube_multifile.spec")
    return 'Youtube_multifile.spec'


def clean_build_dirs():
    """Limpiar directorios de builds anteriores"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Limpiando: {dir_name}")
            try:
                shutil.rmtree(dir_name)
            except Exception as e:
                print(f"⚠️  No se pudo limpiar {dir_name}: {e}")


def check_dependencies():
    """Verificar que las dependencias estén instaladas"""
    print("📦 Verificando dependencias...")
    
    dependencies = ['pyinstaller', 'yt_dlp']
    missing = []
    
    for dep in dependencies:
        try:
            __import__(dep.replace('-', '_'))
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} - FALTANTE")
            missing.append(dep)
    
    if missing:
        print(f"\n⚠️  Faltan dependencias: {', '.join(missing)}")
        print("💡 Instalar con: pip install " + " ".join(missing))
        return False
    
    return True


def build_executable(spec_file):
    """Construir el ejecutable usando PyInstaller"""
    print(f"\n🔧 Construyendo ejecutable con {spec_file}...")
    print("⏱️  Esto puede tomar varios minutos...\n")
    
    try:
        # Ejecutar PyInstaller
        cmd = ['pyinstaller', '--clean', '--noconfirm', spec_file]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        print("✅ Build completado exitosamente!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante el build:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False


def show_results():
    """Mostrar resultados del build"""
    dist_dir = 'dist/ApayKuMedias'
    
    if not os.path.exists(dist_dir):
        print("❌ No se encontró el directorio de distribución")
        return
    
    print("\n" + "="*60)
    print("✅ ¡BUILD COMPLETADO EXITOSAMENTE!")
    print("="*60)
    
    # Listar archivos
    print(f"\n📁 Archivos generados en: {dist_dir}/")
    
    total_size = 0
    file_count = 0
    
    for item in sorted(os.listdir(dist_dir)):
        item_path = os.path.join(dist_dir, item)
        if os.path.isfile(item_path):
            size = os.path.getsize(item_path)
            total_size += size
            file_count += 1
            
            # Mostrar solo archivos importantes
            if item.endswith('.exe') or item.endswith('.dll') or size > 1024*1024:
                size_mb = size / (1024*1024)
                print(f"  {'📌' if item.endswith('.exe') else '📄'} {item:<40} {size_mb:>8.2f} MB")
    
    print(f"\n📊 Total: {file_count} archivos, {total_size/(1024*1024):.2f} MB")
    print(f"\n🚀 Ejecutar: {dist_dir}/ApayKuMedias.exe")
    print("\n💡 Distribución:")
    print(f"   • Copiar toda la carpeta '{os.path.basename(dist_dir)}' completa")
    print("   • Los usuarios ejecutan ApayKuMedias.exe")
    print("   • Todos los archivos .dll y .pyd son necesarios")
    

def main():
    """Función principal"""
    print("╔" + "="*58 + "╗")
    print("║  🚀 EMPAQUETADOR PyInstaller - Múltiples Archivos      ║")
    print("║  📦 Optimizado para mejor rendimiento                   ║")
    print("║  🚫 Sin ventana de consola                              ║")
    print("╚" + "="*58 + "╝\n")
    
    # Verificar dependencias
    if not check_dependencies():
        sys.exit(1)
    
    # Limpiar builds anteriores
    clean_build_dirs()
    
    # Crear spec file optimizado
    spec_file = create_optimized_spec()
    
    # Construir
    if build_executable(spec_file):
        show_results()
    else:
        print("\n❌ El build falló. Revisa los errores arriba.")
        sys.exit(1)


if __name__ == '__main__':
    main()
