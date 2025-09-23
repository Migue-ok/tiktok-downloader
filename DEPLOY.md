# 🚀 Guía de Despliegue - TikTok Downloader

Esta guía te ayudará a desplegar tu TikTok Downloader en diferentes plataformas de hosting gratuito.

## 📋 Preparación

Antes de desplegar, asegúrate de tener:
- [ ] Código subido a GitHub
- [ ] Archivos de configuración creados
- [ ] Tests funcionando localmente

## 🌟 Heroku (Recomendado)

### Pasos para Heroku:

1. **Crear cuenta en Heroku**
   - Ve a [heroku.com](https://heroku.com)
   - Crea una cuenta gratuita

2. **Instalar Heroku CLI**
   ```bash
   # Windows (usando Chocolatey)
   choco install heroku-cli
   
   # O descarga desde: https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Login y crear aplicación**
   ```bash
   heroku login
   heroku create tu-tiktok-downloader
   ```

4. **Configurar variables de entorno**
   ```bash
   heroku config:set SECRET_KEY=tu_clave_secreta_aqui
   heroku config:set DEBUG=False
   ```

5. **Desplegar**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Abrir aplicación**
   ```bash
   heroku open
   ```

### Archivos necesarios para Heroku:
- ✅ `Procfile` - Comando de inicio
- ✅ `requirements.txt` - Dependencias
- ✅ `runtime.txt` - Versión de Python

## 🚄 Railway

### Pasos para Railway:

1. **Ir a Railway**
   - Ve a [railway.app](https://railway.app)
   - Regístrate con GitHub

2. **Conectar repositorio**
   - Haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Elige tu repositorio

3. **Configurar variables**
   - Ve a Variables
   - Agrega `SECRET_KEY=tu_clave_secreta`
   - Agrega `DEBUG=False`

4. **Desplegar**
   - Railway detecta automáticamente Flask
   - El deploy se hace automáticamente

### Archivos necesarios para Railway:
- ✅ `railway.json` - Configuración
- ✅ `requirements.txt` - Dependencias

## 🎨 Render

### Pasos para Render:

1. **Ir a Render**
   - Ve a [render.com](https://render.com)
   - Regístrate con GitHub

2. **Crear Web Service**
   - Haz clic en "New Web Service"
   - Conecta tu repositorio

3. **Configurar servicio**
   - Name: `tiktok-downloader`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

4. **Variables de entorno**
   - Agrega `SECRET_KEY`
   - Agrega `DEBUG=False`

5. **Desplegar**
   - Haz clic en "Create Web Service"

## 🐳 Docker (Opcional)

### Para usar Docker:

1. **Construir imagen**
   ```bash
   docker build -t tiktok-downloader .
   ```

2. **Ejecutar contenedor**
   ```bash
   docker run -p 5000:5000 -e SECRET_KEY=tu_clave tiktok-downloader
   ```

## ⚙️ Variables de Entorno Importantes

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `SECRET_KEY` | Clave secreta de Flask | `tiktok_downloader_secret_key_2025` |
| `DEBUG` | Modo debug | `False` |
| `PORT` | Puerto del servidor | `5000` |

## 🔧 Configuración Post-Despliegue

### 1. Verificar funcionamiento
- [ ] Página principal carga
- [ ] Vista previa funciona
- [ ] Descarga directa funciona
- [ ] Endpoint `/health` responde

### 2. Configurar dominio personalizado (opcional)
- Heroku: Settings → Domains
- Railway: Settings → Custom Domain
- Render: Settings → Custom Domains

### 3. Configurar HTTPS
- Heroku: Automático
- Railway: Automático
- Render: Automático

## 📊 Monitoreo

### Logs en vivo:
```bash
# Heroku
heroku logs --tail

# Railway - Ver en dashboard
# Render - Ver en dashboard
```

### Métricas de rendimiento:
- Heroku: Heroku Metrics
- Railway: Analytics tab
- Render: Metrics tab

## 🚨 Solución de Problemas

### Error: "Application failed to start"
1. Verificar que `Procfile` existe
2. Revisar `requirements.txt`
3. Verificar logs del deploy

### Error: "R10 (Boot timeout)"
1. Aumentar timeout en Heroku
2. Optimizar tiempo de inicio de la app

### Error: "yt-dlp not working"
1. Verificar que yt-dlp está en requirements.txt
2. Actualizar a última versión

## 🔄 Actualización y Mantenimiento

### Para actualizar la aplicación:
```bash
git add .
git commit -m "Update: descripción de cambios"
git push origin main

# Para Heroku específicamente:
git push heroku main
```

### Tareas de mantenimiento:
- [ ] Actualizar yt-dlp mensualmente
- [ ] Revisar logs de errores
- [ ] Monitorear uso de recursos
- [ ] Hacer backup de configuración

## 📈 Optimización

### Para mejor rendimiento:
1. **Usar CDN** para archivos estáticos
2. **Implementar cache** para vistas previas
3. **Optimizar imágenes** en el frontend
4. **Comprimir respuestas** con gzip

### Límites de plataformas gratuitas:
- **Heroku**: 550 horas/mes, duerme tras 30min inactividad
- **Railway**: $5 crédito mensual, sin sleep
- **Render**: 750 horas/mes, duerme tras 15min inactividad

## 🎉 ¡Listo!

Tu TikTok Downloader ahora está desplegado y listo para usar. 

**URLs de ejemplo:**
- Heroku: `https://tu-tiktok-downloader.herokuapp.com`
- Railway: `https://tu-proyecto.up.railway.app`
- Render: `https://tu-servicio.onrender.com`

---

**💡 Consejo**: Guarda estas URLs y compártelas con tus usuarios para que puedan acceder a tu TikTok Downloader desde cualquier lugar.