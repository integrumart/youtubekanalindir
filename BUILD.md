# Developer Build Guide - YouTube Kanal İndirici

## Quick Start for Building Executables

This guide explains how to build the YouTube Channel Downloader application into standalone executables and installers.

## Prerequisites

### For All Platforms
- Python 3.8 or higher
- pip package manager
- Git

### For Windows Build (Recommended for distribution)
- Windows 10/11
- [Inno Setup](https://jrsoftware.org/isdl.php) (for creating setup.exe)
- [FFmpeg](https://ffmpeg.org/download.html) (for MP3 conversion)

### For Linux/Mac Build
- FFmpeg (`sudo apt-get install ffmpeg` or `brew install ffmpeg`)

## Building on Windows

### Step 1: Prepare Environment

```batch
:: Clone the repository
git clone https://github.com/integrumart/youtubekanalindir.git
cd youtubekanalindir

:: Create virtual environment
python -m venv venv
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt
```

### Step 2: Build Executable

Simply run the build script:

```batch
build.bat
```

This will:
1. Create a virtual environment (if not exists)
2. Install all dependencies
3. Run PyInstaller to create `YouTubeKanalIndirici.exe` in `dist\` folder
4. Run Inno Setup (if available) to create installer in `installer_output\` folder

### Step 3: Outputs

After successful build:
- **Executable**: `dist\YouTubeKanalIndirici.exe`
- **Installer**: `installer_output\YouTubeKanalIndirici_Setup.exe`

### Manual Build (Advanced)

If you want to build manually:

```batch
:: Activate virtual environment
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Build with PyInstaller
pyinstaller --clean youtube_downloader.spec

:: Build installer (requires Inno Setup in PATH)
iscc setup_script.iss
```

## Building on Linux/Mac

### Step 1: Prepare Environment

```bash
# Clone the repository
git clone https://github.com/integrumart/youtubekanalindir.git
cd youtubekanalindir

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Build Binary

Run the build script:

```bash
chmod +x build.sh
./build.sh
```

This will create a native binary in `dist/YouTubeKanalIndirici`

**Note**: Linux/Mac builds create native binaries for the host platform. They cannot create Windows .exe files. For Windows distribution, build on Windows.

## Testing the Build

### Test the Executable

Windows:
```batch
dist\YouTubeKanalIndirici.exe
```

Linux/Mac:
```bash
dist/YouTubeKanalIndirici
```

### Test the Application

1. The GUI should open
2. Try entering a YouTube channel URL
3. Select a format (MP3 or MP4)
4. Click "İndirmeyi Başlat"
5. Verify downloads work

## Build Configuration

### PyInstaller Spec File

The `youtube_downloader.spec` file controls the build process:

- **One-file mode**: Everything bundled into single .exe
- **No console window**: GUI application (set `console=False`)
- **Hidden imports**: Includes accessibility libraries
- **UPX compression**: Reduces file size

### Inno Setup Script

The `setup_script.iss` file controls the installer:

- Turkish language support
- Desktop shortcut option
- Program Files installation
- Start menu shortcuts
- Uninstaller

## Customization

### Changing App Icon

1. Create an icon file (`.ico` format)
2. Update `youtube_downloader.spec`:
   ```python
   icon='path/to/icon.ico'
   ```
3. Update `setup_script.iss`:
   ```ini
   SetupIconFile=path/to/icon.ico
   ```

### Changing Version

Update in `setup_script.iss`:
```ini
AppVersion=1.0.0
```

### Changing Company Name

Update in `setup_script.iss`:
```ini
AppPublisher=YourCompanyName
```

## Distribution

### Windows Distribution Options

1. **Standalone EXE**: Share `dist\YouTubeKanalIndirici.exe`
   - Single file
   - No installation needed
   - Portable

2. **Installer**: Share `installer_output\YouTubeKanalIndirici_Setup.exe`
   - Professional installation experience
   - Start menu integration
   - Uninstaller included
   - Recommended for end users

### Important Notes

- Users need FFmpeg installed separately for MP3 conversion
- Include FFmpeg installation instructions with distribution
- Consider bundling FFmpeg in future versions

## Troubleshooting Build Issues

### "Module not found" errors

```batch
pip install --upgrade -r requirements.txt
```

### PyInstaller fails

```batch
pip install --upgrade pyinstaller
pyinstaller --clean youtube_downloader.spec
```

### Inno Setup not found

- Install from https://jrsoftware.org/isdl.php
- Add to PATH or run manually

### Build works but app crashes

- Test in virtual environment first: `python main.py`
- Check if all dependencies are in `requirements.txt`
- Add missing modules to `hiddenimports` in spec file

## CI/CD Considerations

For automated builds:

1. Use GitHub Actions or similar
2. Build on Windows runner for .exe
3. Store artifacts
4. Sign executables (optional but recommended)
5. Create GitHub releases

Example workflow structure:
- Install Python
- Install dependencies
- Run build.bat
- Upload artifacts

## Development Workflow

Recommended workflow for contributors:

1. Make changes to `main.py`
2. Test with `python main.py`
3. Run tests with `python test_app.py`
4. Build with `build.bat` or `build.sh`
5. Test the built executable
6. Commit changes

## Support

For build issues, check:
- Python version (3.8+)
- All dependencies installed
- PyInstaller is up to date
- No antivirus blocking the build

Open an issue on GitHub if problems persist:
https://github.com/integrumart/youtubekanalindir/issues
