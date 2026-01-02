# YouTube Kanal İndirici

YouTube kanallarındaki tüm içeriği MP3 veya MP4 formatında indirmenizi sağlayan masaüstü uygulaması.

## Özellikler

✨ **Temel Özellikler:**
- 🎥 YouTube kanal linkinden tüm videoları indirebilme
- 🎵 MP3 (sadece ses) formatında indirme
- 📹 MP4 (video) formatında indirme
- 📁 İndirme klasörü seçimi
- 📊 İndirme durumu ve ilerleme takibi

♿ **Erişilebilirlik:**
- NVDA ekran okuyucu ile tam uyumlu
- Tüm butonlar ve alanlar klavye ile erişilebilir
- Sesli geri bildirim desteği

## Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- FFmpeg (MP3 dönüşümü için)

### Geliştirme Ortamı Kurulumu

1. Repository'yi klonlayın:
```bash
git clone https://github.com/integrumart/youtubekanalindir.git
cd youtubekanalindir
```

2. Sanal ortam oluşturun ve aktif edin:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

4. FFmpeg'i yükleyin:
   - **Windows**: [FFmpeg İndir](https://ffmpeg.org/download.html)
   - **Linux**: `sudo apt-get install ffmpeg`
   - **Mac**: `brew install ffmpeg`

### Çalıştırma

```bash
python main.py
```

## Executable (.exe) Oluşturma

### Windows'ta Setup.exe Oluşturma

1. [Inno Setup](https://jrsoftware.org/isdl.php) programını yükleyin

2. Build script'ini çalıştırın:
```bash
build.bat
```

Bu işlem:
- `dist\YouTubeKanalIndirici.exe` oluşturur
- `installer_output\YouTubeKanalIndirici_Setup.exe` setup dosyasını oluşturur

### Linux/Mac'te Binary Oluşturma

```bash
chmod +x build.sh
./build.sh
```

## Kullanım

1. Uygulamayı başlatın
2. YouTube kanal linkini giriş alanına yapıştırın
   - Örnek: `https://www.youtube.com/@kullaniciadi`
3. İndirme formatını seçin:
   - **MP4**: Video + Ses
   - **MP3**: Sadece Ses
4. İsteğe bağlı: İndirme klasörünü değiştirin
5. "İndirmeyi Başlat" butonuna tıklayın
6. İndirme tamamlanana kadar bekleyin

## NVDA Ekran Okuyucu ile Kullanım

Uygulama NVDA ekran okuyucu ile tamamen uyumludur:

- **Tab** tuşu ile alanlar arasında geçiş yapın
- Her alan odaklandığında sesli bildirim alırsınız
- **Enter** ile butonlara tıklayın
- Format seçimi için **ok tuşları** kullanabilirsiniz

## Teknolojiler

- **Python 3**: Ana programlama dili
- **tkinter**: GUI framework
- **yt-dlp**: YouTube video indirme kütüphanesi
- **accessible-output2**: Ekran okuyucu desteği
- **PyInstaller**: .exe oluşturma
- **Inno Setup**: Windows installer oluşturma

## Sorun Giderme

### FFmpeg Hatası

Eğer MP3 dönüşümü çalışmıyorsa:
1. FFmpeg'in yüklü olduğundan emin olun
2. FFmpeg'in sistem PATH'inde olduğunu kontrol edin
3. Terminal/CMD'de `ffmpeg -version` komutunu çalıştırarak test edin

### İndirme Hataları

- İnternet bağlantınızı kontrol edin
- YouTube linkinin doğru olduğundan emin olun
- Kanal linki yerine video linki kullanmadığınızdan emin olun

### Erişilebilirlik Sorunları

- NVDA'nın çalıştığından emin olun
- `accessible-output2` paketinin yüklü olduğunu kontrol edin

## Lisans

Bu proje LICENSE dosyasında belirtilen lisans altında dağıtılmaktadır.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Pull request göndermekten çekinmeyin.

## İletişim

Sorularınız için issue açabilirsiniz.
