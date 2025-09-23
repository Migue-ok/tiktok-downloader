@echo off
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
