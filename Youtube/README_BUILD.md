# 📦 Guía de Empaquetado con PyInstaller

Esta guía te ayudará a empaquetar la aplicación usando PyInstaller para crear un ejecutable distribuible.

## 🎯 Características de este Empaquetado

- ✅ **Múltiples archivos**: Más rápido de cargar y ejecutar
- ✅ **Sin ventana de consola**: Aplicación limpia y profesional
- ✅ **Optimizado**: Solo incluye dependencias necesarias
- ✅ **Menor tamaño**: Excluye librerías innecesarias
- ✅ **Compatibilidad**: Windows 7/8/10/11

## 📋 Requisitos Previos

### 1. Python Instalado
```bash
python --version
# Debe ser Python 3.7 o superior
```

### 2. Instalar Dependencias
```bash
pip install pyinstaller yt-dlp
```

### 3. FFmpeg (Opcional, solo para MP3)
Si deseas descargar audio en formato MP3, necesitas FFmpeg:
- Descargar de: https://ffmpeg.org/download.html
- Agregar a PATH del sistema

## 🚀 Métodos de Empaquetado

### Método 1: Usar el Script Automático (Recomendado)

#### En Windows:
```batch
# Opción A: Doble clic en el archivo
build_multifile.bat

# Opción B: Desde CMD/PowerShell
.\build_multifile.bat
```

#### En Linux/Mac:
```bash
python build_multifile.py
```

### Método 2: PyInstaller Directo

```bash
# Generar el archivo .spec
python build_multifile.py  # Esto crea Youtube_multifile.spec

# Construir manualmente
pyinstaller --clean --noconfirm Youtube_multifile.spec
```

### Método 3: Construcción Avanzada

Para optimización adicional:
```bash
python advanced_build_config.py
pyinstaller --clean --noconfirm media_downloader_advanced.spec
```

## 📁 Estructura de Salida

Después del empaquetado, encontrarás:

```
dist/
└── ApayKuMedias/
    ├── ApayKuMedias.exe          ← Ejecutable principal
    ├── python*.dll               ← DLLs necesarias
    ├── _tkinter.pyd
    ├── yt_dlp/                   ← Módulos de Python
    └── ... (otros archivos)
```

## 🎯 Distribución

### Para Distribuir tu Aplicación:

1. **Comprimir la carpeta completa**
   ```
   dist/ApayKuMedias/ → ApayKuMedias.zip
   ```

2. **Compartir el ZIP** con usuarios

3. **Instrucciones para usuarios finales:**
   - Descomprimir el ZIP
   - Ejecutar `ApayKuMedias.exe`
   - ¡Listo!

### ⚠️ Importante
- NO distribuir solo el .exe, debe ir con todos los archivos
- La carpeta completa debe permanecer junta
- Tamaño aproximado: 60-80 MB

## 🛠️ Solución de Problemas

### Error: "No module named 'yt_dlp'"
```bash
pip install yt-dlp
```

### Error: "No module named 'tkinter'"
- En Windows: Ya viene con Python
- En Linux: `sudo apt-get install python3-tk`

### El ejecutable es muy grande
- Normal para PyInstaller (60-80 MB)
- Incluye Python completo + dependencias
- Opción: Usar `upx` para comprimir más

### Antivirus detecta el ejecutable
- Falso positivo común con PyInstaller
- Soluciones:
  1. Agregar excepción en el antivirus
  2. Reportar falso positivo al fabricante
  3. Firmar digitalmente el ejecutable (requiere certificado)

### El programa no inicia
1. Verificar que todos los archivos estén presentes
2. Ejecutar desde CMD para ver errores:
   ```batch
   cd dist\ApayKuMedias
   ApayKuMedias.exe
   ```

## 🔧 Personalización

### Cambiar el Ícono
1. Reemplazar `media_downloader_icon.ico`
2. Ejecutar el build nuevamente

### Cambiar el Nombre
Editar `build_multifile.py`, línea:
```python
name='ApayKuMedias',  # ← Cambiar aquí
```

### Incluir Archivos Adicionales
Editar el .spec, sección `datas`:
```python
datas=[
    ('mi_archivo.txt', '.'),
    ('carpeta_imagenes', 'imagenes'),
],
```

## 📊 Comparación: Archivo Único vs Múltiples Archivos

### Un Solo Archivo (--onefile)
- ✅ Ventaja: Un solo .exe
- ❌ Desventaja: Más lento al iniciar
- ❌ Desventaja: Extrae archivos temporalmente
- Tamaño: ~65 MB

### Múltiples Archivos (--onedir) - **RECOMENDADO**
- ✅ Ventaja: Inicia más rápido
- ✅ Ventaja: No usa archivos temporales
- ✅ Ventaja: Más fácil de debuggear
- ❌ Desventaja: Múltiples archivos
- Tamaño total: ~70 MB

## 📝 Notas Adicionales

### Optimizaciones Incluidas
- Excluye NumPy, Pandas, Matplotlib
- Excluye PyQt5/6
- Solo incluye extractores necesarios de yt-dlp
- UPX compression activado
- console=False (sin ventana CMD)

### Seguridad
- El código fuente NO está incluido en el ejecutable
- Solo se incluye bytecode de Python
- Para mayor seguridad, considerar:
  - Firma digital con certificado
  - Ofuscación de código (opcional)

### Actualizaciones
Para actualizar la aplicación:
1. Modificar el código fuente
2. Ejecutar el build nuevamente
3. Redistribuir la nueva carpeta

## 🆘 Soporte

### Recursos Útiles
- PyInstaller Docs: https://pyinstaller.org/
- yt-dlp Docs: https://github.com/yt-dlp/yt-dlp
- FFmpeg: https://ffmpeg.org/

### Logs de Errores
Si hay problemas, revisar:
- `build/ApayKuMedias/warn-ApayKuMedias.txt`
- Salida de consola durante el build

## 📜 Licencia

Este script de empaquetado es parte del proyecto TikTok Downloader.
Asegúrate de cumplir con las licencias de todas las dependencias.

---

**¿Necesitas ayuda?** Abre un issue en el repositorio de GitHub.
