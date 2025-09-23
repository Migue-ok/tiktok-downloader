@echo off
title TikTok Downloader - Servidor Web
color 0A

echo.
echo ==========================================
echo    TikTok Downloader - Servidor Web
echo ==========================================
echo.

echo [INFO] Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado o no esta en el PATH
    echo [INFO] Descarga Python desde: https://python.org
    pause
    exit /b 1
)

echo [INFO] Instalando dependencias...
pip install -r requirements.txt

echo [INFO] Ejecutando tests...
python test_app.py

if %errorlevel% neq 0 (
    echo [WARNING] Algunos tests fallaron, pero el servidor puede ejecutarse
)

echo.
echo [INFO] Iniciando servidor web...
echo [INFO] La aplicacion estara disponible en: http://localhost:5000
echo [INFO] Presiona Ctrl+C para detener el servidor
echo.

python app.py

echo.
echo [INFO] Servidor detenido. Presiona cualquier tecla para salir...
pause >nul