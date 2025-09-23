# Media Downloader - Información para Whitelist de Antivirus

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
