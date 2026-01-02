# Kullanım Kılavuzu - YouTube Kanal İndirici

## İçindekiler
1. [Kurulum](#kurulum)
2. [İlk Çalıştırma](#ilk-çalıştırma)
3. [Temel Kullanım](#temel-kullanım)
4. [Erişilebilirlik Özellikleri](#erişilebilirlik-özellikleri)
5. [Sık Sorulan Sorular](#sık-sorulan-sorular)

## Kurulum

### Windows Kullanıcıları için

1. `YouTubeKanalIndirici_Setup.exe` dosyasını indirin
2. Setup dosyasına çift tıklayın
3. Kurulum sihirbazını takip edin
4. FFmpeg'i yükleyin:
   - https://ffmpeg.org/download.html adresinden indirin
   - Sistem PATH'ine ekleyin

### Python ile Çalıştırma

```bash
# Repository'yi klonlayın
git clone https://github.com/integrumart/youtubekanalindir.git
cd youtubekanalindir

# Sanal ortam oluşturun
python -m venv venv

# Windows'ta:
venv\Scripts\activate

# Linux/Mac'te:
source venv/bin/activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı çalıştırın
python main.py
```

## İlk Çalıştırma

1. Uygulamayı başlattığınızda ana pencere açılacaktır
2. "YouTube Kanal İndirici uygulaması başlatıldı" mesajını duyacaksınız (NVDA aktifse)
3. Ana pencerede şu alanlar bulunur:
   - Kanal linki giriş alanı
   - Format seçimi (MP3/MP4)
   - İndirme klasörü seçimi
   - İndirmeyi başlat butonu
   - İndirme durumu log alanı

## Temel Kullanım

### Adım 1: YouTube Kanal Linkini Girin

1. İlk giriş alanına tıklayın veya Tab tuşu ile gidin
2. YouTube kanal linkini yapıştırın
   - Örnek: `https://www.youtube.com/@kullaniciadi`
   - Veya: `https://www.youtube.com/c/KanalAdi`
   - Kanal ana sayfası URL'si olmalıdır

### Adım 2: Format Seçin

**MP4 (Video)** seçeneği:
- Hem video hem ses indirir
- Daha büyük dosya boyutu
- Videoları izlemek için

**MP3 (Sadece Ses)** seçeneği:
- Sadece ses indirir
- Daha küçük dosya boyutu
- Müzik dinlemek için
- Görme engelliler için önerilen

### Adım 3: İndirme Klasörünü Seçin (İsteğe Bağlı)

- Varsayılan: `Kullanıcı/Downloads/YouTube`
- "Klasör Seç" butonuna basarak değiştirilebilir
- Seçilen klasör otomatik olarak oluşturulur

### Adım 4: İndirmeyi Başlatın

1. "İndirmeyi Başlat" butonuna basın (Enter veya Space)
2. İndirme başlayacaktır
3. Log alanında ilerlemeyi takip edebilirsiniz
4. Her video için durum güncellemesi alırsınız

## Erişilebilirlik Özellikleri

### NVDA Ekran Okuyucu Desteği

Uygulama NVDA ekran okuyucu ile tam uyumludur:

#### Sesli Bildirimler
- Uygulama başlatıldığında duyuru
- Her alan odaklandığında bilgilendirme
- Format seçimi değiştiğinde duyuru
- İndirme başladığında duyuru
- İndirme tamamlandığında duyuru

#### Klavye Kısayolları
- **Tab**: Sonraki alana geç
- **Shift+Tab**: Önceki alana geç
- **Enter/Space**: Butona bas
- **Ok tuşları**: Radio butonları arasında geçiş
- **Alt+F4**: Uygulamayı kapat

### Odak Sırası
1. Kanal linki giriş alanı
2. MP4 radio butonu
3. MP3 radio butonu
4. İndirme klasörü giriş alanı
5. Klasör Seç butonu
6. İndirmeyi Başlat butonu

### Her Alanda Sesli Duyurular
- **Kanal linki alanı**: "Kanal linki giriş alanı"
- **MP4 butonu**: "MP4 video formatı seçildi"
- **MP3 butonu**: "MP3 ses formatı seçildi"
- **İndirme klasörü**: "İndirme klasörü"
- **İndirme butonu**: "İndirmeyi başlat butonu"

## Sık Sorulan Sorular

### S: MP3 dönüşümü çalışmıyor?
**C:** FFmpeg'in yüklü olduğundan emin olun. Terminal/CMD'de `ffmpeg -version` komutunu çalıştırarak test edin.

### S: "Geçersiz YouTube linki" hatası alıyorum?
**C:** YouTube kanal linkinin doğru formatda olduğundan emin olun. Kanal ana sayfası URL'si olmalıdır, tek video linki değil.

### S: İndirme çok yavaş?
**C:** İnternet hızınıza ve kanal içeriğinin boyutuna bağlıdır. Büyük kanallar saatler sürebilir.

### S: Bazı videolar indirilmiyor?
**C:** Özel veya yaş kısıtlamalı videolar indirilemeyebilir. Uygulama bu videoları atlayıp devam eder.

### S: NVDA duyurularını duymuyorum?
**C:** 
- NVDA'nın çalıştığından emin olun
- `accessible-output2` paketinin yüklü olduğunu kontrol edin
- Uygulamayı yeniden başlatın

### S: İndirilen dosyalar nerede?
**C:** Varsayılan olarak `Kullanıcı/Downloads/YouTube` klasöründe. Farklı bir klasör seçtiyseniz orada olacaktır.

### S: Kanalın tüm videoları değil de sadece bazılarını indirebilir miyim?
**C:** Bu sürümde tüm kanal içeriği indirilir. Tek video indirmek için video linkini kullanabilirsiniz.

### S: İndirme sırasında bilgisayarımı kapatabilir miyim?
**C:** Hayır, uygulama çalışmaya devam etmelidir. İndirme tamamlanana kadar bilgisayarınızı açık tutun.

### S: Uygulamayı komut satırından kullanabilir miyim?
**C:** Şu anda sadece GUI versiyonu mevcuttur. Komut satırı versiyonu gelecek güncellemelerde eklenebilir.

## Destek

Sorunlarınız için GitHub'da issue açabilirsiniz:
https://github.com/integrumart/youtubekanalindir/issues

## Güncellemeler

En son sürüm için repository'yi kontrol edin:
https://github.com/integrumart/youtubekanalindir
