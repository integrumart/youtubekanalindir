@echo off
REM YouTube Kanal İndirici Build Script
REM Bu script uygulamayı .exe ve setup.exe olarak derler

echo ========================================
echo YouTube Kanal Indirici Build Script
echo ========================================
echo.

REM Sanal ortam kontrolü
if not exist "venv\" (
    echo Sanal ortam bulunamadi. Olusturuluyor...
    python -m venv venv
    if errorlevel 1 (
        echo HATA: Sanal ortam olusturulamadi!
        pause
        exit /b 1
    )
)

REM Sanal ortamı aktifleştir
echo Sanal ortam aktif ediliyor...
call venv\Scripts\activate.bat

REM Bağımlılıkları yükle
echo.
echo Bagimliliklari yukleniyor...
pip install -r requirements.txt
if errorlevel 1 (
    echo HATA: Bagimliliklar yuklenemedi!
    pause
    exit /b 1
)

REM PyInstaller ile .exe oluştur
echo.
echo PyInstaller ile .exe olusturuluyor...
pyinstaller --clean youtube_downloader.spec
if errorlevel 1 (
    echo HATA: .exe olusturulamadi!
    pause
    exit /b 1
)

echo.
echo ========================================
echo .exe basariyla olusturuldu!
echo Konum: dist\YouTubeKanalIndirici.exe
echo ========================================
echo.

REM Inno Setup için kontrol (opsiyonel)
where iscc >nul 2>nul
if %errorlevel% equ 0 (
    echo.
    echo Inno Setup ile setup.exe olusturuluyor...
    iscc setup_script.iss
    if errorlevel 1 (
        echo UYARI: setup.exe olusturulamadi!
    ) else (
        echo.
        echo ========================================
        echo setup.exe basariyla olusturuldu!
        echo Konum: installer_output\YouTubeKanalIndirici_Setup.exe
        echo ========================================
    )
) else (
    echo.
    echo UYARI: Inno Setup bulunamadi!
    echo setup.exe olusturmak icin Inno Setup yuklenmeli.
    echo Indirme linki: https://jrsoftware.org/isdl.php
)

echo.
echo Build islemi tamamlandi!
pause
