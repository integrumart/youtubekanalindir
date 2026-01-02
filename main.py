#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Kanal İndirici
Youtube kanallarındaki tüm içeriği MP3 veya MP4 olarak indirmenizi sağlar.
NVDA ekran okuyucu ile uyumludur.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import sys
import threading
import queue
import yt_dlp
from pathlib import Path

# Accessible output için, eğer yüklüyse kullan
try:
    import accessible_output2.outputs.auto
    screen_reader = accessible_output2.outputs.auto.Auto()
    SCREEN_READER_AVAILABLE = True
except ImportError:
    SCREEN_READER_AVAILABLE = False
    screen_reader = None


class YouTubeKanalIndirici:
    """YouTube kanal indirme uygulaması ana sınıfı"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Kanal İndirici")
        self.root.geometry("700x500")
        
        # Pencereyi ekranın ortasına yerleştir
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Varsayılan indirme klasörü
        self.download_path = str(Path.home() / "Downloads" / "YouTube")
        
        # İndirme durumu
        self.downloading = False
        self.download_queue = queue.Queue()
        
        self.create_widgets()
        self.announce("YouTube Kanal İndirici uygulaması başlatıldı")
        
    def announce(self, message):
        """Ekran okuyucu ile mesaj duyur"""
        if SCREEN_READER_AVAILABLE and screen_reader:
            try:
                screen_reader.speak(message)
            except Exception:
                pass
        print(f"[Duyuru] {message}")
    
    def create_widgets(self):
        """GUI bileşenlerini oluştur"""
        
        # Ana çerçeve
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Başlık
        title_label = ttk.Label(
            main_frame, 
            text="YouTube Kanal İndirici",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Kanal URL girişi
        url_label = ttk.Label(main_frame, text="YouTube Kanal Linki:")
        url_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        self.url_entry.bind('<FocusIn>', lambda e: self.announce("Kanal linki giriş alanı"))
        
        # Format seçimi
        format_label = ttk.Label(main_frame, text="İndirme Formatı:")
        format_label.grid(row=3, column=0, sticky=tk.W, pady=(15, 5))
        
        self.format_var = tk.StringVar(value="mp4")
        
        format_frame = ttk.Frame(main_frame)
        format_frame.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        self.mp4_radio = ttk.Radiobutton(
            format_frame,
            text="MP4 (Video)",
            variable=self.format_var,
            value="mp4",
            command=lambda: self.announce("MP4 video formatı seçildi")
        )
        self.mp4_radio.grid(row=0, column=0, padx=(0, 20))
        
        self.mp3_radio = ttk.Radiobutton(
            format_frame,
            text="MP3 (Sadece Ses)",
            variable=self.format_var,
            value="mp3",
            command=lambda: self.announce("MP3 ses formatı seçildi")
        )
        self.mp3_radio.grid(row=0, column=1)
        
        # İndirme klasörü seçimi
        path_label = ttk.Label(main_frame, text="İndirme Klasörü:")
        path_label.grid(row=5, column=0, sticky=tk.W, pady=(15, 5))
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.path_entry = ttk.Entry(path_frame, width=40)
        self.path_entry.insert(0, self.download_path)
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        self.path_entry.bind('<FocusIn>', lambda e: self.announce("İndirme klasörü"))
        
        path_button = ttk.Button(
            path_frame,
            text="Klasör Seç",
            command=self.select_download_path
        )
        path_button.grid(row=0, column=1)
        path_frame.columnconfigure(0, weight=1)
        
        # İndir butonu
        self.download_button = ttk.Button(
            main_frame,
            text="İndirmeyi Başlat",
            command=self.start_download
        )
        self.download_button.grid(row=7, column=0, columnspan=2, pady=(20, 10))
        self.download_button.bind('<FocusIn>', lambda e: self.announce("İndirmeyi başlat butonu"))
        
        # Durum çubuğu
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=8, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        # Durum mesajı
        self.status_label = ttk.Label(
            main_frame,
            text="Hazır",
            foreground="blue"
        )
        self.status_label.grid(row=9, column=0, columnspan=2, pady=5)
        
        # Log alanı
        log_label = ttk.Label(main_frame, text="İndirme Durumu:")
        log_label.grid(row=10, column=0, sticky=tk.W, pady=(10, 5))
        
        # Log text widget ve scrollbar
        log_frame = ttk.Frame(main_frame)
        log_frame.grid(row=11, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.log_text = tk.Text(log_frame, height=8, width=60, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(log_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        # Ana çerçeve için ağırlıklar
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(11, weight=1)
        
    def select_download_path(self):
        """İndirme klasörü seç"""
        folder = filedialog.askdirectory(
            title="İndirme Klasörü Seçin",
            initialdir=self.download_path
        )
        if folder:
            self.download_path = folder
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
            self.announce(f"İndirme klasörü seçildi: {folder}")
            self.log(f"İndirme klasörü: {folder}")
    
    def log(self, message):
        """Log mesajı ekle"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def update_status(self, message, color="blue"):
        """Durum mesajını güncelle"""
        self.status_label.config(text=message, foreground=color)
        self.root.update_idletasks()
    
    def start_download(self):
        """İndirme işlemini başlat"""
        if self.downloading:
            messagebox.showwarning(
                "Uyarı",
                "Bir indirme işlemi zaten devam ediyor!"
            )
            return
        
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror(
                "Hata",
                "Lütfen bir YouTube kanal linki girin!"
            )
            self.announce("Hata: Kanal linki girilmedi")
            return
        
        # URL kontrolü - YouTube kanal veya video linki
        if not any(domain in url.lower() for domain in ["youtube.com/", "youtu.be/"]):
            messagebox.showerror(
                "Hata",
                "Geçerli bir YouTube linki girin!"
            )
            self.announce("Hata: Geçersiz YouTube linki")
            return
        
        # İndirme klasörünü oluştur
        try:
            os.makedirs(self.download_path, exist_ok=True)
        except Exception as e:
            messagebox.showerror(
                "Hata",
                f"İndirme klasörü oluşturulamadı: {e}"
            )
            return
        
        self.downloading = True
        self.download_button.config(state=tk.DISABLED)
        self.progress.start()
        
        format_type = self.format_var.get()
        self.announce(f"İndirme başlatılıyor. Format: {format_type}")
        self.log(f"İndirme başlatıldı...")
        self.log(f"URL: {url}")
        self.log(f"Format: {format_type.upper()}")
        self.log(f"Klasör: {self.download_path}")
        self.update_status("İndiriliyor...", "green")
        
        # Arka planda indirme işlemini başlat
        thread = threading.Thread(
            target=self.download_channel,
            args=(url, format_type),
            daemon=True
        )
        thread.start()
    
    def download_channel(self, url, format_type):
        """YouTube kanalını indir (arka plan thread)"""
        try:
            # yt-dlp ayarları
            ydl_opts = {
                'format': 'bestaudio/best' if format_type == 'mp3' else 'best',
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'ignoreerrors': True,
                'no_warnings': False,
                'extract_flat': False,
                'progress_hooks': [self.progress_hook],
            }
            
            # MP3 için audio extraction ayarları
            if format_type == 'mp3':
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.log("Kanal bilgileri alınıyor...")
                info = ydl.extract_info(url, download=True)
                
                if 'entries' in info:
                    video_count = len(list(info['entries']))
                    self.log(f"Toplam {video_count} video bulundu.")
                else:
                    self.log("Tek bir video indiriliyor.")
            
            self.root.after(0, self.download_complete, True, "İndirme başarıyla tamamlandı!")
            
        except Exception as e:
            error_msg = f"İndirme hatası: {str(e)}"
            self.root.after(0, self.download_complete, False, error_msg)
    
    def progress_hook(self, d):
        """İndirme ilerlemesi hook"""
        if d['status'] == 'downloading':
            filename = os.path.basename(d.get('filename', 'Bilinmeyen'))
            self.root.after(0, self.log, f"İndiriliyor: {filename}")
        elif d['status'] == 'finished':
            filename = os.path.basename(d.get('filename', 'Bilinmeyen'))
            self.root.after(0, self.log, f"Tamamlandı: {filename}")
    
    def download_complete(self, success, message):
        """İndirme tamamlandığında çağrılır"""
        self.downloading = False
        self.progress.stop()
        self.download_button.config(state=tk.NORMAL)
        
        if success:
            self.update_status(message, "green")
            self.log("\n" + message)
            self.announce(message)
            messagebox.showinfo("Başarılı", message)
        else:
            self.update_status("İndirme başarısız", "red")
            self.log("\n" + message)
            self.announce("İndirme başarısız oldu")
            messagebox.showerror("Hata", message)


def main():
    """Ana uygulama başlangıcı"""
    root = tk.Tk()
    app = YouTubeKanalIndirici(root)
    root.mainloop()


if __name__ == "__main__":
    main()
