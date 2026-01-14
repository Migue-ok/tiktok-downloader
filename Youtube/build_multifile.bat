@echo off
chcp 65001 >nul
title Empaquetador PyInstaller - Múltiples Archivos
color 0A

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║  🚀 EMPAQUETADOR PyInstaller - Múltiples Archivos         ║
echo ║  📦 Optimizado para mejor rendimiento                      ║
echo ║  🚫 Sin ventana de consola                                 ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

echo [1/4] 📦 Instalando/Actualizando dependencias...
pip install --upgrade pyinstaller yt-dlp --quiet
if errorlevel 1 (
    echo ❌ Error instalando dependencias
    pause
    exit /b 1
)
echo ✅ Dependencias instaladas

echo.
echo [2/4] 🧹 Limpiando builds anteriores...
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
if exist "__pycache__" rmdir /s /q "__pycache__" 2>nul
echo ✅ Limpieza completada

echo.
echo [3/4] 🔧 Ejecutando build (esto puede tomar varios minutos)...
python build_multifile.py

echo.
echo [4/4] ✅ Proceso completado
echo.
echo 💡 Presiona cualquier tecla para abrir la carpeta de distribución...
pause >nul

if exist "dist\ApayKuMedias" (
    explorer "dist\ApayKuMedias"
) else (
    echo ⚠️  No se encontró la carpeta de distribución
)
