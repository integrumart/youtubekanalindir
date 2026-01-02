; Inno Setup Script for YouTube Kanal İndirici
; Bu script setup.exe oluşturmak için kullanılır

[Setup]
AppName=YouTube Kanal İndirici
AppVersion=1.0.0
AppPublisher=IntegrumArt
DefaultDirName={autopf}\YouTubeKanalIndirici
DefaultGroupName=YouTube Kanal İndirici
OutputDir=installer_output
OutputBaseFilename=YouTubeKanalIndirici_Setup
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
WizardStyle=modern
SetupIconFile=
UninstallDisplayIcon={app}\YouTubeKanalIndirici.exe

[Languages]
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"

[Tasks]
Name: "desktopicon"; Description: "Masaüstünde kısayol oluştur"; GroupDescription: "Ek kısayollar:"

[Files]
Source: "dist\YouTubeKanalIndirici.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\YouTube Kanal İndirici"; Filename: "{app}\YouTubeKanalIndirici.exe"
Name: "{autodesktop}\YouTube Kanal İndirici"; Filename: "{app}\YouTubeKanalIndirici.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\YouTubeKanalIndirici.exe"; Description: "YouTube Kanal İndirici'yi çalıştır"; Flags: nowait postinstall skipifsilent
