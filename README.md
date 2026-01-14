# 🎵 TikTok Downloader

Una aplicación web moderna y elegante para descargar videos de TikTok en calidad máxima. Construida con Flask y yt-dlp.

![TikTok Downloader](https://img.shields.io/badge/TikTok-Downloader-ff6b6b)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Características

- 🎬 **Descarga directa** - Videos se descargan inmediatamente al navegador
- 💾 **Almacenamiento temporal** - Guarda videos en el servidor para descarga posterior  
- 👁️ **Vista previa** - Muestra información del video antes de descargar
- 📱 **Responsive** - Compatible con móviles y escritorio
- 🚀 **Sin límites** - Descarga todos los videos que quieras
- 🎯 **Calidad máxima** - Utiliza yt-dlp para obtener la mejor calidad disponible
- 🔒 **Privado y seguro** - No almacena datos personales
- ⚡ **Rápido y eficiente** - Procesamiento optimizado

## 🚀 Demo en Vivo

🔗 **[Probar ahora](https://tu-tiktok-downloader.herokuapp.com)**

## 📷 Capturas de Pantalla

*[Próximamente - Agrega capturas de pantalla de tu aplicación]*

## 🛠️ Instalación Local

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/tiktok-downloader.git
   cd tiktok-downloader
   ```

2. **Crea un entorno virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecuta la aplicación**
   ```bash
   python app.py
   ```

5. **Abre tu navegador**
   ```
   http://localhost:5000
   ```

## 🌐 Despliegue en la Nube

### ✅ Pre-Verificación de Despliegue

Antes de desplegar, verifica que no haya cambios sin confirmar:

```bash
# Linux/Mac
./check_deployment.sh

# Windows
check_deployment.bat

# Python (cualquier plataforma)
python check_deployment.py
```

### Heroku (Recomendado)

1. **Crea una cuenta en [Heroku](https://heroku.com)**

2. **Instala Heroku CLI**

3. **Despliega tu aplicación**
   ```bash
   # Verificar pre-despliegue
   python check_deployment.py
   
   # Desplegar
   heroku create tu-tiktok-downloader
   heroku config:set SECRET_KEY=tu_clave_secreta_aqui
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### Railway

1. **Ve a [Railway](https://railway.app)**
2. **Conecta tu repositorio de GitHub**
3. **Despliega automáticamente**

### Render

1. **Ve a [Render](https://render.com)**
2. **Conecta tu repositorio**
3. **Configura el servicio web con:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## 🔧 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Descarga**: yt-dlp (fork mejorado de youtube-dl)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Servidor**: Gunicorn
- **Hosting**: Heroku, Railway, Render

## 📝 API Endpoints

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | Página principal |
| `/preview` | POST | Vista previa del video |
| `/download_direct` | POST | Descarga directa del video |
| `/download_local` | POST | Guardar video en servidor |
| `/download_file/<filename>` | GET | Descargar archivo guardado |
| `/delete_file/<filename>` | DELETE | Eliminar archivo del servidor |
| `/health` | GET | Estado de la aplicación |

## 🎯 Uso de la API

### Vista previa de video
```javascript
fetch('/preview', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: 'https://www.tiktok.com/@user/video/123' })
})
```

### Descarga directa
```javascript
fetch('/download_direct', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url: 'https://www.tiktok.com/@user/video/123' })
})
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. **Abre** un Pull Request

### Reportar Bugs

Si encuentras un bug, por favor:
1. Verifica que no esté ya reportado
2. Crea un issue con detalles del problema
3. Incluye pasos para reproducir el bug

## 🐛 Solución de Problemas

### Error: "yt-dlp no encontrado"
```bash
pip install --upgrade yt-dlp
```

### Error: "Puerto en uso"
Cambia el puerto en `app.py`:
```python
app.run(port=8000)  # Cambiar puerto
```

### Videos no se descargan
- Verifica que la URL de TikTok sea válida
- Algunos videos privados no se pueden descargar
- Actualiza yt-dlp: `pip install --upgrade yt-dlp`

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## ⚠️ Disclaimer

Esta herramienta es solo para uso educativo y personal. Los usuarios son responsables de:

- Respetar los términos de servicio de TikTok
- Respetar los derechos de autor de los creadores de contenido
- No usar la herramienta para propósitos comerciales sin permiso
- Cumplir con las leyes locales sobre derechos de autor

## 🙏 Agradecimientos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Por la increíble librería de descarga
- [Flask](https://flask.palletsprojects.com/) - Por el framework web ligero y potente
- Comunidad de código abierto - Por las contribuciones y feedback

## 📊 Estadísticas del Proyecto

![GitHub stars](https://img.shields.io/github/stars/tu-usuario/tiktok-downloader)
![GitHub forks](https://img.shields.io/github/forks/tu-usuario/tiktok-downloader)
![GitHub issues](https://img.shields.io/github/issues/tu-usuario/tiktok-downloader)

## 📞 Contacto

- **GitHub**: [@tu-usuario](https://github.com/tu-usuario)
- **Email**: tu-email@ejemplo.com
- **Website**: [tu-sitio-web.com](https://tu-sitio-web.com)

## 🔄 Roadmap

- [ ] Soporte para más plataformas (Instagram, YouTube Shorts)
- [ ] API REST completa
- [ ] Sistema de colas para descargas masivas
- [ ] Interfaz de administración
- [ ] Soporte para subtítulos
- [ ] Compresión de videos
- [ ] Conversión de formatos

---

⭐ **¡No olvides darle una estrella al proyecto si te gustó!**

---

**🎉 ¡Gracias por usar TikTok Downloader!**