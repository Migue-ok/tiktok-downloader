import yt_dlp
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time

class CompactMediaDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title(" ")
        self.root.geometry("450x380")
        self.root.minsize(420, 360)
        self.root.resizable(True, True)
        
        # Paleta de colores minimalista
        self.colors = {
            'bg': '#f8f9fa',
            'card': '#ffffff',
            'accent': '#e9ecef',
            'primary': '#6c5ce7',
            'primary_hover': '#5f3dc4',
            'secondary': '#fd79a8',
            'success': '#00b894',
            'text': '#2d3436',
            'text_light': '#636e72',
            'border': '#ddd',
            'selected': '#6c5ce7',
            'hover': '#f1f2f6'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Variables
        self.download_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        self.url_var = tk.StringVar()
        self.format_var = tk.StringVar(value="1080p Video")
        self.selected_platform = tk.StringVar(value="YouTube")
        self.downloading = False
        
        # Logos compactos de plataformas
        self.platform_logos = {
            'YouTube': {'text': '▶', 'bg': '#FF0000', 'fg': 'white'},
            'TikTok': {'text': '♪', 'bg': '#000000', 'fg': 'white'},
            'Instagram': {'text': '📷', 'bg': '#E4405F', 'fg': 'white'},
            'Facebook': {'text': 'f', 'bg': '#1877F2', 'fg': 'white'}
        }
        
        self.create_compact_widgets()
        
    def create_platform_button(self, parent, platform, row, col):
        """Crear botón de plataforma compacto"""
        logo_info = self.platform_logos[platform]
        
        frame = tk.Frame(parent, bg=self.colors['card'])
        frame.grid(row=row, column=col, padx=8, pady=5, sticky='nsew')
        
        # Botón más pequeño
        btn = tk.Button(frame,
                       text=logo_info['text'],
                       font=('Arial Black', 12) if platform != 'Instagram' else ('Segoe UI Emoji', 12),
                       bg=logo_info['bg'],
                       fg=logo_info['fg'],
                       relief='flat',
                       bd=0,
                       width=3,
                       height=1,
                       cursor='hand2',
                       command=lambda: self.select_platform(platform))
        btn.pack()
        
        # Etiqueta más pequeña
        label = tk.Label(frame,
                        text=platform,
                        bg=self.colors['card'],
                        fg=self.colors['text_light'],
                        font=('Segoe UI', 8, 'bold'))
        label.pack(pady=(3, 0))
        
        # Efectos hover
        def on_enter(e):
            if self.selected_platform.get() != platform:
                btn.config(relief='raised', bd=1)
        
        def on_leave(e):
            if self.selected_platform.get() != platform:
                btn.config(relief='flat', bd=0)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        setattr(self, f"{platform.lower()}_btn", btn)
        setattr(self, f"{platform.lower()}_frame", frame)
        
        return btn
    
    def select_platform(self, platform):
        """Seleccionar plataforma"""
        self.selected_platform.set(platform)
        
        for p in self.platform_logos.keys():
            btn = getattr(self, f"{p.lower()}_btn", None)
            frame = getattr(self, f"{p.lower()}_frame", None)
            if btn and frame:
                if p == platform:
                    frame.config(relief='solid', bd=2, highlightbackground=self.colors['selected'])
                    btn.config(relief='raised', bd=1)
                else:
                    frame.config(relief='flat', bd=0)
                    btn.config(relief='flat', bd=0)
        
        self.update_status(f"{platform} seleccionado")
    
    def create_compact_button(self, parent, text, command, bg_color, hover_color, **kwargs):
        """Crear botón compacto"""
        btn = tk.Button(parent,
                       text=text,
                       command=command,
                       bg=bg_color,
                       fg='white',
                       font=('Segoe UI', 9, 'bold'),
                       relief='flat',
                       bd=0,
                       padx=15,
                       pady=8,
                       cursor='hand2',
                       **kwargs)
        
        def on_enter(e):
            btn.config(bg=hover_color)
        
        def on_leave(e):
            btn.config(bg=bg_color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        
        return btn
    
    def create_progress_bar(self, parent):
        """Crear barra de progreso compacta"""
        progress_frame = tk.Frame(parent, bg=self.colors['card'])
        progress_frame.pack(fill='x', pady=(10, 5))
        
        # Canvas más pequeño
        self.progress_canvas = tk.Canvas(progress_frame,
                                        height=25,
                                        bg=self.colors['card'],
                                        highlightthickness=0)
        self.progress_canvas.pack(fill='x', padx=10)
        
        # Estado inicial
        self.update_progress_animation(0, "Listo para descargar")
    
    def update_progress_animation(self, progress, message):
        """Actualizar progreso compacto"""
        self.progress_canvas.delete("all")
        
        canvas_width = self.progress_canvas.winfo_width()
        if canvas_width <= 1:
            canvas_width = 400
        
        # Barra de fondo
        self.progress_canvas.create_rectangle(
            10, 8, canvas_width - 10, 15,
            fill=self.colors['accent'],
            outline=self.colors['border'],
            width=1
        )
        
        if progress > 0:
            # Barra de progreso
            bar_width = (progress / 100) * (canvas_width - 20)
            self.progress_canvas.create_rectangle(
                10, 8, 10 + bar_width, 15,
                fill=self.colors['success'],
                outline=""
            )
            
            # Gato pequeño
            cat_x = 15 + (progress / 100) * (canvas_width - 30)
            cat_emoji = "🐈" if int(time.time() * 2) % 2 else "🐱"
            self.progress_canvas.create_text(
                cat_x, 11,
                text=cat_emoji,
                font=('Segoe UI Emoji', 10)
            )
        else:
            # Gato inicial
            self.progress_canvas.create_text(
                20, 11,
                text="🐱",
                font=('Segoe UI Emoji', 10)
            )
        
        # Texto de estado más pequeño
        self.progress_canvas.create_text(
            canvas_width // 2, 20,
            text=message,
            fill=self.colors['text'],
            font=('Segoe UI', 8)
        )
        
        self.root.update()
    
    def update_status(self, message):
        """Actualizar solo el mensaje de estado"""
        self.update_progress_animation(0, message)
    
    def paste_from_clipboard(self):
        """Pegar desde portapapeles"""
        try:
            clipboard_content = self.root.clipboard_get()
            self.url_var.set(clipboard_content)
            self.update_status("URL pegada")
        except:
            messagebox.showwarning("Advertencia", "No hay contenido en el portapapeles")
    
    def create_compact_widgets(self):
        # Frame principal compacto
        main_frame = tk.Frame(self.root, bg=self.colors['card'], relief='solid', bd=1)
        main_frame.pack(fill='both', expand=True, padx=8, pady=8)
        
        # Título compacto
        title_frame = tk.Frame(main_frame, bg=self.colors['card'])
        title_frame.pack(fill='x', pady=(10, 5))
        
        title_label = tk.Label(title_frame,
                              text="🚀 Apayku Medios",
                              bg=self.colors['card'],
                              fg=self.colors['text'],
                              font=('Segoe UI', 14, 'bold'))
        title_label.pack()
        
        # Plataformas compactas
        platform_frame = tk.Frame(main_frame, bg=self.colors['card'])
        platform_frame.pack(fill='x', pady=5)
        
        platform_label = tk.Label(platform_frame,
                                 text="Plataforma:",
                                 bg=self.colors['card'],
                                 fg=self.colors['text'],
                                 font=('Segoe UI', 9, 'bold'))
        platform_label.pack(pady=(0, 5))
        
        # Grid compacto de plataformas
        platforms_grid = tk.Frame(platform_frame, bg=self.colors['card'])
        platforms_grid.pack()
        
        for i in range(4):
            platforms_grid.columnconfigure(i, weight=1)
        
        self.create_platform_button(platforms_grid, "YouTube", 0, 0)
        self.create_platform_button(platforms_grid, "TikTok", 0, 1)
        self.create_platform_button(platforms_grid, "Instagram", 0, 2)
        self.create_platform_button(platforms_grid, "Facebook", 0, 3)
        
        # URL compacta
        url_frame = tk.Frame(main_frame, bg=self.colors['card'])
        url_frame.pack(fill='x', padx=15, pady=8)
        
        url_label = tk.Label(url_frame,
                            text="URL:",
                            bg=self.colors['card'],
                            fg=self.colors['text'],
                            font=('Segoe UI', 9, 'bold'))
        url_label.pack(anchor='w', pady=(0, 3))
        
        url_input_frame = tk.Frame(url_frame, bg=self.colors['card'])
        url_input_frame.pack(fill='x')
        
        self.url_entry = tk.Entry(url_input_frame,
                                 textvariable=self.url_var,
                                 font=('Segoe UI', 9),
                                 bg='white',
                                 fg=self.colors['text'],
                                 relief='solid',
                                 bd=1)
        self.url_entry.pack(side='left', fill='x', expand=True, ipady=5)
        
        paste_btn = tk.Button(url_input_frame,
                             text="📋",
                             command=self.paste_from_clipboard,
                             bg=self.colors['secondary'],
                             fg='white',
                             font=('Segoe UI', 8),
                             relief='flat',
                             bd=0,
                             padx=8,
                             cursor='hand2')
        paste_btn.pack(side='right', padx=(5, 0), ipady=5)
        
        # Opciones compactas en una fila
        options_frame = tk.Frame(main_frame, bg=self.colors['card'])
        options_frame.pack(fill='x', padx=15, pady=5)
        
        # Formato
        format_frame = tk.Frame(options_frame, bg=self.colors['card'])
        format_frame.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        format_label = tk.Label(format_frame,
                               text="Formato:",
                               bg=self.colors['card'],
                               fg=self.colors['text'],
                               font=('Segoe UI', 9, 'bold'))
        format_label.pack(anchor='w', pady=(0, 2))
        
        self.format_combo = ttk.Combobox(format_frame,
                                        textvariable=self.format_var,
                                        values=["🎵 MP3", "🎬 1080p", "🎬 720p", "🎬 480p", "⭐ Mejor"],
                                        state="readonly",
                                        font=('Segoe UI', 8),
                                        width=12)
        self.format_combo.pack(fill='x', ipady=3)
        
        # Carpeta
        folder_frame = tk.Frame(options_frame, bg=self.colors['card'])
        folder_frame.pack(side='right', fill='x', expand=True, padx=(5, 0))
        
        folder_label = tk.Label(folder_frame,
                               text="Carpeta:",
                               bg=self.colors['card'],
                               fg=self.colors['text'],
                               font=('Segoe UI', 9, 'bold'))
        folder_label.pack(anchor='w', pady=(0, 2))
        
        folder_input_frame = tk.Frame(folder_frame, bg=self.colors['card'])
        folder_input_frame.pack(fill='x')
        
        self.folder_entry = tk.Entry(folder_input_frame,
                                    textvariable=self.download_path,
                                    font=('Segoe UI', 8),
                                    bg=self.colors['accent'],
                                    fg=self.colors['text'],
                                    relief='solid',
                                    bd=1,
                                    state='readonly')
        self.folder_entry.pack(side='left', fill='x', expand=True, ipady=3)
        
        browse_btn = tk.Button(folder_input_frame,
                              text="📁",
                              command=self.browse_folder,
                              bg=self.colors['primary'],
                              fg='white',
                              font=('Segoe UI', 8),
                              relief='flat',
                              bd=0,
                              padx=8,
                              cursor='hand2')
        browse_btn.pack(side='right', padx=(3, 0), ipady=3)
        
        # Progreso compacto
        self.create_progress_bar(main_frame)
        
        # Botones compactos
        buttons_frame = tk.Frame(main_frame, bg=self.colors['card'])
        buttons_frame.pack(fill='x', padx=15, pady=(5, 10))
        
        self.download_btn = self.create_compact_button(buttons_frame,
                                                      "🚀 DESCARGAR",
                                                      self.start_download,
                                                      self.colors['success'],
                                                      '#27ae60')
        self.download_btn.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        clear_btn = self.create_compact_button(buttons_frame,
                                              "🗑️ LIMPIAR",
                                              self.clear_fields,
                                              self.colors['secondary'],
                                              '#e84393')
        clear_btn.pack(side='right')
        
        # Seleccionar YouTube por defecto
        self.root.after(100, lambda: self.select_platform("YouTube"))
    
    def browse_folder(self):
        """Seleccionar carpeta"""
        folder = filedialog.askdirectory(title="Seleccionar carpeta")
        if folder:
            self.download_path.set(folder)
            self.update_status(f"Carpeta: {os.path.basename(folder)}")
    
    def clear_fields(self):
        """Limpiar campos"""
        self.url_var.set("")
        self.update_status("Campos limpiados")
    
    def get_ydl_opts(self):
        """Configurar opciones de yt-dlp"""
        format_choice = self.format_var.get()
        
        opts = {
            'outtmpl': os.path.join(self.download_path.get(), '%(title)s.%(ext)s'),
            'writeinfojson': False,
            'writesubtitles': False,
            'writeautomaticsub': False,
            'verbose': False,  # Reducir mensajes de debug
        }
        
        if "MP3" in format_choice:
            # FFmpeg - buscar en PATH del sistema primero
            opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        elif "1080p" in format_choice:
            opts['format'] = 'best[height<=1080]/best'
        elif "720p" in format_choice:
            opts['format'] = 'best[height<=720]/best'
        elif "480p" in format_choice:
            opts['format'] = 'best[height<=480]/best'
        else:  # Mejor
            opts['format'] = 'best'
        
        return opts
    
    def progress_hook(self, d):
        """Callback de progreso"""
        if d['status'] == 'downloading':
            if 'total_bytes' in d and d['total_bytes']:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                speed = d.get('speed', 0)
                if speed:
                    speed_mb = speed / (1024*1024)
                    message = f"Descargando {percent:.0f}% ({speed_mb:.1f}MB/s)"
                else:
                    message = f"Descargando {percent:.0f}%"
                
                self.update_progress_animation(percent, message)
        elif d['status'] == 'finished':
            self.update_progress_animation(100, "🎉 ¡Completado!")
    
    def start_download(self):
        """Iniciar descarga"""
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Advertencia", "Ingresa una URL válida")
            return
        
        if self.downloading:
            messagebox.showinfo("Información", "Descarga en progreso")
            return
        
        if not os.path.exists(self.download_path.get()):
            messagebox.showerror("Error", "Carpeta no existe")
            return
        
        platform = self.selected_platform.get()
        format_choice = self.format_var.get()
        
        self.downloading = True
        self.download_btn.config(state='disabled', bg=self.colors['text_light'])
        
        def download_thread():
            try:
                self.update_progress_animation(5, f"Conectando con {platform}...")
                time.sleep(0.5)
                
                ydl_opts = self.get_ydl_opts()
                ydl_opts['progress_hooks'] = [self.progress_hook]
                
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    self.update_progress_animation(10, "Analizando...")
                    time.sleep(0.3)
                    
                    ydl.download([url])
                
                # Éxito
                for i in range(3):
                    self.update_progress_animation(100, "🎉 ¡Éxito!")
                    time.sleep(0.3)
                    self.update_progress_animation(100, "🐱 ¡Completado!")
                    time.sleep(0.3)
                
                messagebox.showinfo("¡Éxito!",
                                   f"¡Descarga completada!\n\n"
                                   f"Plataforma: {platform}\n"
                                   f"Formato: {format_choice}")
                
            except Exception as e:
                error_msg = str(e)
                self.update_progress_animation(0, f"❌ Error: {error_msg[:30]}...")
                messagebox.showerror("Error", f"Error en descarga:\n\n{error_msg}")
            
            finally:
                self.downloading = False
                self.download_btn.config(state='normal', bg=self.colors['success'])
                self.root.after(2000, lambda: self.update_status("Listo para nueva descarga"))
        
        threading.Thread(target=download_thread, daemon=True).start()

def check_dependencies():
    """Verificar dependencias"""
    try:
        import yt_dlp
        return True
    except ImportError:
        messagebox.showerror("Dependencias Faltantes",
                           "yt-dlp no está instalado.\n\n"
                           "Para instalarlo:\n"
                           "pip install yt-dlp")
        return False

def main():
    if not check_dependencies():
        return
    
    try:
        root = tk.Tk()
        app = CompactMediaDownloader(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar:\n{str(e)}")

if __name__ == "__main__":
    main()