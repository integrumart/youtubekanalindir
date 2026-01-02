#!/bin/bash
# YouTube Kanal İndirici Build Script (Linux/Mac)
# Bu script uygulamayı binary olarak derler

echo "========================================"
echo "YouTube Kanal Indirici Build Script"
echo "========================================"
echo

# Sanal ortam kontrolü
if [ ! -d "venv" ]; then
    echo "Sanal ortam bulunamadi. Olusturuluyor..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "HATA: Sanal ortam olusturulamadi!"
        exit 1
    fi
fi

# Sanal ortamı aktifleştir
echo "Sanal ortam aktif ediliyor..."
source venv/bin/activate

# Bağımlılıkları yükle
echo
echo "Bagimliliklari yukleniyor..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "HATA: Bagimliliklar yuklenemedi!"
    exit 1
fi

# PyInstaller ile binary oluştur
echo
echo "PyInstaller ile binary olusturuluyor..."
pyinstaller --clean youtube_downloader.spec
if [ $? -ne 0 ]; then
    echo "HATA: Binary olusturulamadi!"
    exit 1
fi

echo
echo "========================================"
echo "Binary basariyla olusturuldu!"
echo "Konum: dist/YouTubeKanalIndirici"
echo "========================================"
echo
echo "NOT: Windows setup.exe olusturmak icin"
echo "     Windows'ta build.bat calistirin"
echo

echo "Build islemi tamamlandi!"
