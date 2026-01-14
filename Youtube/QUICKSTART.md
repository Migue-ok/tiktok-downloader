# 🚀 Inicio Rápido - Empaquetado con PyInstaller

## 📦 Guía de 3 Pasos

### Paso 1: Instalar Dependencias

```bash
pip install pyinstaller yt-dlp
```

### Paso 2: Ejecutar el Empaquetador

#### Windows:
```batch
build_multifile.bat
```

#### Linux/Mac:
```bash
python build_multifile.py
```

### Paso 3: Distribuir

Tu aplicación estará en: `dist/ApayKuMedias/`

Comprime la carpeta completa y comparte el ZIP.

---

## ✨ Características del Empaquetado

- ✅ **Sin ventana de consola** - Interfaz limpia
- ✅ **Múltiples archivos** - Carga más rápida
- ✅ **Optimizado** - Solo 60-80 MB
- ✅ **Compatible** - Windows 7/8/10/11

---

## 📚 Documentación Completa

Ver [README_BUILD.md](README_BUILD.md) para guía detallada.

---

## ⚡ Comandos Útiles

### Limpiar builds anteriores:
```bash
# Windows
rmdir /s /q build dist __pycache__

# Linux/Mac
rm -rf build dist __pycache__
```

### Build manual:
```bash
pyinstaller --clean --noconfirm Youtube_multifile.spec
```

### Ver archivos generados:
```bash
# Windows
dir dist\ApayKuMedias

# Linux/Mac
ls -lh dist/ApayKuMedias/
```

---

## 🛠️ Solución Rápida de Problemas

### Error: "No module named 'pyinstaller'"
```bash
pip install pyinstaller
```

### Error: "No module named 'yt_dlp'"
```bash
pip install yt-dlp
```

### El ejecutable no inicia
- Verifica que todos los archivos de `dist/ApayKuMedias/` estén presentes
- No muevas solo el .exe, debe ir con todos sus archivos

### Antivirus bloquea el ejecutable
- Es un falso positivo común con PyInstaller
- Agrega una excepción en tu antivirus
- O reporta el falso positivo al fabricante

---

## 💡 Tips

1. **No separar archivos**: Distribuir la carpeta completa
2. **FFmpeg para MP3**: Opcional, solo si necesitas descargar audio
3. **Tamaño normal**: 60-80 MB es normal para aplicaciones PyInstaller
4. **Primera ejecución**: Puede ser más lenta, luego será rápida

---

## 📞 ¿Necesitas Ayuda?

- 📖 Lee la [Guía Completa](README_BUILD.md)
- 🐛 Reporta bugs en GitHub Issues
- 💬 Pregunta en GitHub Discussions

---

**¡Listo para empaquetar!** 🎉
