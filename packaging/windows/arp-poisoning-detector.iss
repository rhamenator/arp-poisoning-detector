#define AppName "ARP Poisoning Detector"
#ifndef AppVersion
  #define AppVersion "0.1.0"
#endif

[Setup]
UninstallDisplayIcon={app}\app-icon.ico
SetupIconFile=app-icon.ico
AppId={{C712561C-0DBE-4B67-8146-9F7FC77281F1}
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={autopf}\ARP Poisoning Detector
DefaultGroupName={#AppName}
OutputDir=..\..\artifacts
OutputBaseFilename=arp-poisoning-detector-{#AppVersion}-windows-x64-setup
Compression=lzma2
SolidCompression=yes
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
ChangesEnvironment=yes

[Files]
Source: "app-icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\..\dist\arp-poisoning-detector.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ARP Poisoning Detector"; Filename: "{app}\arp-poisoning-detector.exe"; IconFilename: "{app}\app-icon.ico"

[Registry]
Root: HKCU; Subkey: "Environment"; ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Check: NeedsPathUpdate

[Code]
function NeedsPathUpdate(): Boolean;
begin
  Result := Pos(ExpandConstant('{app}'), GetEnv('PATH')) = 0;
end;
