@echo off
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
if exist "dist\MediaDownloader.exe" (
    echo ✅ Ejecutable creado exitosamente
    
    echo [7/7] 📊 Generando información del build...
    echo Build completado: %date% %time% > build_info.txt
    for %%i in ("dist\MediaDownloader.exe") do echo Tamaño del ejecutable: %%~zi bytes >> build_info.txt
    
    echo.
    echo ═══════════════════════════════════════════════════════════
    echo ✅ ¡BUILD COMPLETADO EXITOSAMENTE!
    echo.
    echo 📁 Ubicación: dist\MediaDownloader.exe
    for %%i in ("dist\MediaDownloader.exe") do echo 📏 Tamaño: %%~zi bytes
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
