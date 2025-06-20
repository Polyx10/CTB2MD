#!/bin/bash

# Nom de l'application
APP_NAME="CTB2MD.app"
APP_PATH="$HOME/Desktop/$APP_NAME"

# Créer la structure de l'application
mkdir -p "$APP_PATH/Contents/"{MacOS,Resources}

# Copier le script Python
cp ctb2md.py "$APP_PATH/Contents/Resources/"

# Créer le script launcher
cat > "$APP_PATH/Contents/MacOS/launcher" << 'EOL'
#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
RESOURCES="$( dirname "$DIR" )/Resources"
/usr/bin/env python3 "$RESOURCES/ctb2md.py"
EOL

# Rendre le launcher exécutable
chmod +x "$APP_PATH/Contents/MacOS/launcher"

# Créer le fichier Info.plist
cat > "$APP_PATH/Contents/Info.plist" << 'EOL'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>launcher</string>
    <key>CFBundleIconFile</key>
    <string>AppIcon</string>
    <key>CFBundleIdentifier</key>
    <string>com.local.ctb2md</string>
    <key>CFBundleName</key>
    <string>CTB2MD</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.10</string>
    <key>CFBundleSupportedPlatforms</key>
    <array>
        <string>MacOSX</string>
    </array>
</dict>
</plist>
EOL

# Créer une icône simple
cat > "$APP_PATH/Contents/Resources/AppIcon.icns" << 'EOL'
icns
EOL

echo "Application créée sur le bureau : $APP_NAME"
