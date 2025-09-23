# advanced_build_config.py
# Configuración avanzada para evitar falsos positivos de antivirus

import os
import hashlib
import time

def create_advanced_spec():
    """Crear .spec avanzado con técnicas anti-falsos positivos"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
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
    ['Youtube.py'],
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
    name='Apayku Medios',
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
'''
    
    with open('media_downloader_advanced.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Spec avanzado creado: media_downloader_advanced.spec")

def create_digital_signature_info():
    """Crear información para firma digital simulada"""
    signature_info = '''# Información de firma digital para Windows
# Esto ayuda a que el ejecutable parezca más legítimo

[Certificate Info]
Subject: CN=Media Tools Software, O=Media Tools, C=US
Issuer: CN=Media Tools CA, O=Media Tools, C=US
Valid From: 2024-01-01
Valid To: 2026-12-31
Thumbprint: A1B2C3D4E5F6789012345678901234567890ABCD

[Publisher Info]
Company: Media Tools
Description: Multimedia Content Downloader
Product: Media Downloader
Version: 1.0.0
Copyright: © 2025 Media Tools
'''
    
    with open('signature_info.txt', 'w') as f:
        f.write(signature_info)
    
    print("✅ Info de firma creada: signature_info.txt")

def create_whitelist_submission_info():
    """Crear información para envío a whitelist de antivirus"""
    whitelist_info = '''# Media Downloader - Información para Whitelist de Antivirus

## Información del Software
- Nombre: Media Downloader
- Versión: 1.0.0
- Desarrollador: Media Tools
- Propósito: Descarga legítima de contenido multimedia público
- Tipo: Herramienta de utilidad GUI

## Funcionalidades Principales
1. Descarga de videos/audio de plataformas públicas
2. Interfaz gráfica amigable con Tkinter
3. Selección de formatos de descarga
4. Progreso visual de descarga
5. Configuración de carpeta de destino

## Librerías Utilizadas
- yt-dlp: Librería legal para descarga de medios
- tkinter: GUI estándar de Python
- PIL: Procesamiento de imágenes
- threading: Manejo de hilos
- urllib3: Comunicación HTTP estándar

## Hash del Ejecutable
[Se generará automáticamente después de la compilación]

## Razones de Falsos Positivos
1. PyInstaller empaqueta Python, puede ser detectado como "packed"
2. yt-dlp descarga contenido de internet (red)
3. El ejecutable modifica archivos (guarda descargas)
4. Uso de threading puede parecer sospechoso

## Mitigaciones Implementadas
1. Información de versión completa
2. Icono profesional personalizado
3. Sin ofuscación de código
4. Exclusión de módulos innecesarios
5. UPX optimizado selectivamente
6. Console=False para mejor UX

## URLs de Contacto (simuladas)
- Website: https://mediatools-software.example.com
- Support: support@mediatools-software.example.com
- GitHub: https://github.com/mediatools/downloader

## Certificados de Antivirus Recomendados
Para envío a whitelist:
1. Windows Defender - Microsoft
2. VirusTotal - Google
3. Malwarebytes
4. Avast
5. AVG
'''
    
    with open('whitelist_submission.md', 'w', encoding='utf-8') as f:
        f.write(whitelist_info)
    
    print("✅ Info whitelist creada: whitelist_submission.md")

def create_build_optimized():
    """Crear script de construcción optimizado"""
    build_script = '''@echo off
title Media Downloader - Builder Optimizado
color 0A

echo.
echo  ███╗   ███╗███████╗██████╗ ██╗ █████╗     ██████╗ ██╗     
echo  ████╗ ████║██╔════╝██╔══██╗██║██╔══██╗    ██╔══██╗██║     
echo  ██╔████╔██║█████╗  ██║  ██║██║███████║    ██║  ██║██║     
echo  ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║    ██║  ██║██║     
echo  ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║    ██████╔╝███████╗
echo  ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝
echo.
echo  🚀 CONSTRUCTOR OPTIMIZADO - v1.0
echo  ═══════════════════════════════════════════════════════════
echo.

echo [1/7] 📦 Verificando e instalando dependencias...
pip install --upgrade pyinstaller pillow yt-dlp --quiet
if errorlevel 1 (
    echo ❌ Error instalando dependencias
    pause
    exit /b 1
)

echo [2/7] 🎨 Generando icono personalizado...
python setup_executable.py create_icon
if not exist "media_downloader_icon.ico" (
    echo ⚠️  Usando icono por defecto
)

echo [3/7] 🧹 Limpiando builds anteriores...
if exist "dist" rmdir /s /q "dist"
if exist "build" rmdir /s /q "build"
if exist "__pycache__" rmdir /s /q "__pycache__"

echo [4/7] 📋 Preparando configuración avanzada...
python advanced_build_config.py

echo [5/7] 🔧 Construyendo ejecutable (esto puede tomar varios minutos)...
pyinstaller --clean --noconfirm media_downloader_advanced.spec

echo [6/7] 🔍 Verificando construcción...
if exist "dist\\MediaDownloader.exe" (
    echo ✅ Ejecutable creado exitosamente
    
    echo [7/7] 📊 Generando información del build...
    echo Build completado: %date% %time% > build_info.txt
    for %%i in ("dist\\MediaDownloader.exe") do echo Tamaño del ejecutable: %%~zi bytes >> build_info.txt
    
    echo.
    echo ═══════════════════════════════════════════════════════════
    echo ✅ ¡BUILD COMPLETADO EXITOSAMENTE!
    echo.
    echo 📁 Ubicación: dist\\MediaDownloader.exe
    for %%i in ("dist\\MediaDownloader.exe") do echo 📏 Tamaño: %%~zi bytes
    echo 🛡️  Optimizado para evitar falsos positivos
    echo.
    echo 💡 TIPS PARA EVITAR DETECCIÓN DE ANTIVIRUS:
    echo    • Escanea con VirusTotal antes de distribuir
    echo    • Considera firmar digitalmente el ejecutable
    echo    • Envía a whitelist de antivirus principales
    echo    • Documenta el propósito legítimo del software
    echo.
    
    set /p open="¿Abrir carpeta del ejecutable? (s/n): "
    if /i "%open%"=="s" explorer "dist"
    
) else (
    echo ❌ Error: No se pudo crear el ejecutable
    echo 📋 Revisa los logs arriba para más detalles
    pause
    exit /b 1
)

echo.
pause
'''
    
    with open('build_optimized.bat', 'w', encoding='utf-8') as f:
        f.write(build_script)
    
    print("✅ Builder optimizado creado: build_optimized.bat")

def create_antivirus_bypass_tips():
    """Crear guía para evitar detecciones"""
    tips_content = '''# 🛡️ Guía: Evitar Falsos Positivos de Antivirus

## 🎯 Estrategias Implementadas

### 1. **Información Profesional del Ejecutable**
- ✅ Versión completa (1.0.0.0)
- ✅ Información de compañía
- ✅ Descripción detallada
- ✅ Copyright información

### 2. **Optimizaciones de PyInstaller**
- ✅ `--console=False` (sin ventana DOS)
- ✅ UPX selectivo (evita over-compression)
- ✅ Exclusión de módulos sospechosos
- ✅ Hiddenimports específicos

### 3. **Icono Personalizado**
- ✅ ICO multi-resolución (16px a 256px)
- ✅ Diseño profesional
- ✅ Relacionado con funcionalidad

### 4. **Código Limpio**
- ✅ Sin ofuscación
- ✅ Imports explícitos
- ✅ Comentarios claros
- ✅ Nombres descriptivos

## 🔧 Pasos Post-Compilación

### 1. **Verificar con VirusTotal**
```bash
# Subir MediaDownloader.exe a:
# https://www.virustotal.com/gui/
```

### 2. **Firma Digital (Opcional)**
```bash
# Si tienes certificado de código:
signtool sign /f certificate.pfx /p password /t http://timestamp.digicert.com MediaDownloader.exe
```

### 3. **Envío a Whitelist**
Enviar a fabricantes principales:
- Microsoft Defender
- Malwarebytes
- Avast/AVG
- Bitdefender

### 4. **Distribución Responsable**
- Hospedar en GitHub Releases
- Incluir código fuente
- Documentar propósito
- Proveer checksums

## 📊 Técnicas Específicas Implementadas

### A. **PyInstaller Hooks Personalizados**
```python
hiddenimports=[
    'yt_dlp.extractor.youtube',  # Específico vs genérico
    'urllib3.util.retry',        # Dependencias explícitas
    'certifi',                   # SSL certificates
]
```

### B. **Exclusiones Inteligentes**
```python
excludes=[
    'matplotlib',  # Librería pesada
    'numpy',       # No necesaria
    'test',        # Módulos de testing
]
```

### C. **UPX Optimizado**
```python
upx=True,
upx_exclude=[
    'vcruntime140.dll',  # Críticos del sistema
    'api-ms-win*.dll'    # Windows APIs
]
```

## ⚠️ Señales de Alerta para Antivirus

### **Comportamientos que Triggean Detección:**
1. **Red**: Descargar archivos de internet
2. **Archivos**: Escribir en system paths
3. **Proceso**: Múltiples threads
4. **Empaquetado**: PyInstaller signatures

### **Nuestras Mitigaciones:**
1. ✅ Descarga solo a carpetas especificadas por usuario
2. ✅ No modifica registro ni system paths
3. ✅ Threading limitado y documentado
4. ✅ Información completa de versión

## 🎯 Checklist Final

- [ ] Ejecutable compilado sin errores
- [ ] Icono visible correctamente
- [ ] Información de versión completa
- [ ] Tamaño razonable (< 50MB)
- [ ] Funciona en Windows limpio
- [ ] Escaneado en VirusTotal
- [ ] Documentación incluida
- [ ] Código fuente disponible

## 📞 Si Hay Falsos Positivos

### **Reporte a Fabricante:**
1. **Windows Defender**: 
   - https://www.microsoft.com/wdsi/filesubmission
2. **Malwarebytes**:
   - https://forums.malwarebytes.com/forum/122-false-positives/
3. **VirusTotal**:
   - Comentar en el análisis

### **Información a Incluir:**
- Hash del archivo
- Propósito legítimo
- Código fuente
- Información de contacto
- Documentación técnica

---

**💡 Recuerda**: Los falsos positivos son comunes con PyInstaller. La clave es ser transparente, profesional y proactivo en la comunicación con los fabricantes de antivirus.
'''
    
    with open('antivirus_bypass_guide.md', 'w', encoding='utf-8') as f:
        f.write(tips_content)
    
    print("✅ Guía anti-falsos positivos: antivirus_bypass_guide.md")

def main():
    print("🛡️ Configurando build avanzado anti-detección...")
    print("=" * 60)
    
    create_advanced_spec()
    create_digital_signature_info()
    create_whitelist_submission_info()
    create_build_optimized()
    create_antivirus_bypass_tips()
    
    print("\n" + "=" * 60)
    print("✅ ¡Configuración avanzada completada!")
    print("\n🚀 Para construir el ejecutable optimizado:")
    print("   👉 Ejecuta: build_optimized.bat")
    print("\n📚 Archivos creados:")
    print("   • media_downloader_advanced.spec (configuración)")
    print("   • build_optimized.bat (constructor)")
    print("   • antivirus_bypass_guide.md (guía)")
    print("   • whitelist_submission.md (para antivirus)")
    print("\n🛡️ Técnicas anti-falsos positivos implementadas:")
    print("   ✅ Información de versión profesional")
    print("   ✅ Icono personalizado multi-resolución")
    print("   ✅ UPX optimizado selectivamente")
    print("   ✅ Exclusiones inteligentes")
    print("   ✅ Imports explícitos")
    print("   ✅ Sin console window")

if __name__ == "__main__":
    main()