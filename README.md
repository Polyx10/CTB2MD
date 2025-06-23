# CTB2MD - Migrate from Cherrytree to Obsidian / Migration de Cherrytree vers Obsidian

[![Release](https://img.shields.io/github/v/release/Polyx10/CTB2MD)](https://github.com/Polyx10/CTB2MD/releases)
[![License](https://img.shields.io/github/license/Polyx10/CTB2MD)](https://github.com/Polyx10/CTB2MD/blob/main/LICENSE)
[![macOS](https://img.shields.io/badge/platform-macOS-blue)](https://github.com/Polyx10/CTB2MD/releases)
[![Obsidian](https://img.shields.io/badge/tool-obsidian-purple)](https://obsidian.md)
[![Cherrytree](https://img.shields.io/badge/convert-cherrytree-red)](https://www.giuspen.net/cherrytree/)
[![Download CTB2MD](https://img.shields.io/sourceforge/dt/ctb2md.svg)](https://sourceforge.net/projects/ctb2md/files/latest/download)

[English]

CTB2MD is a powerful yet simple tool designed to help users migrate their notes from Cherrytree (.ctb) to Obsidian-compatible Markdown (.md). Perfect for knowledge base migration, this macOS application preserves your note structure, formatting, and command blocks while converting to clean Markdown that works flawlessly in Obsidian.

### Note de sécurité

⚠️ **Important** : Au premier lancement de CTB2MD, macOS peut afficher un avertissement de sécurité indiquant "Impossible d'ouvrir CTB2MD car le développeur ne peut pas être vérifié". C'est normal pour les applications open-source. Pour résoudre cela :
1. Allez dans Réglages Système → Confidentialité et sécurité
2. Faites défiler jusqu'à l'avertissement de sécurité concernant CTB2MD
3. Cliquez sur "Ouvrir quand même"
4. Confirmez votre choix

Pour plus d'informations, consultez [le guide d'assistance Apple sur l'ouverture d'applications de développeurs non identifiés](https://support.apple.com/fr-fr/guide/mac-help/mh40616/mac).

### Security Notice

⚠️ **Important**: When first launching CTB2MD, macOS might show a security warning saying "CTB2MD cannot be opened because the developer cannot be verified". This is normal for open-source applications. To resolve this:
1. Go to System Settings → Privacy & Security
2. Scroll down to the security warning about CTB2MD
3. Click "Open Anyway"
4. Confirm your choice

For more information, see [Apple's support guide about opening apps from unidentified developers](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac).

## Features

- Simple GUI with file selector
- Convert .ctb files to Markdown
- Preserve layout and formatting
- Support for command blocks
- Compatible with Obsidian

## Installation

1. Download the latest version from the [Releases](../../releases) page
2. Extract the archive
3. Drag CTB2MD.app to your Applications folder

## Usage

1. Double-click CTB2MD.app
2. Select your .ctb file to convert
3. Markdown files will be created in a new folder next to the source file

## Development

To build the application from source:

```bash
git clone https://github.com/Polyx10/CTB2MD.git
cd CTB2MD
./create_app.sh
```

## Requirements

- macOS
- Python 3.x
- tkinter (included with Python)

## Changelog

### v1.0.2
- Nouvelle icône de l'application
- Interface plus épurée

### v1.0.1
- Improved user experience:
  - Removed debug window for cleaner interface
  - Streamlined conversion process
  - Enhanced success messages

---

[Français]

Une application simple pour convertir des fichiers Cherrytree (.ctb) en fichiers Markdown (.md), spécialement conçue pour macOS.

## Fonctionnalités

- Interface graphique simple avec sélecteur de fichiers
- Conversion des fichiers .ctb en Markdown
- Préservation de la mise en page et du formatage
- Support des blocs de code pour les commandes
- Compatible avec Obsidian

## Installation

1. Téléchargez la dernière version depuis la page des [Releases](../../releases)
2. Décompressez l'archive
3. Glissez l'application CTB2MD.app dans votre dossier Applications

## Utilisation

1. Double-cliquez sur CTB2MD.app
2. Sélectionnez votre fichier .ctb à convertir
3. Les fichiers Markdown seront créés dans un nouveau dossier à côté du fichier source

## Historique des versions

### v1.0.2
- Nouvelle icône de l'application
- Interface plus épurée

### v1.0.1
- Amélioration de l'expérience utilisateur :
  - Suppression de la fenêtre de débogage pour une interface plus épurée
  - Processus de conversion simplifié
  - Messages de succès améliorés

## Développement

Pour construire l'application depuis les sources :

```bash
git clone https://github.com/Polyx10/CTB2MD.git
cd CTB2MD
./create_app.sh
```

## Prérequis

- macOS
- Python 3.x
- tkinter (inclus avec Python)

## Screenshots / Captures d'écran

[English]
Screenshots will be added soon. The application features:
- Clean and simple interface
- Dark mode support
- Progress feedback
- Direct access to converted files

[Français]
Les captures d'écran seront ajoutées prochainement. L'application propose :
- Interface simple et épurée
- Support du mode sombre
- Retour sur la progression
- Accès direct aux fichiers convertis

## Star History / Historique des étoiles

[![Star History Chart](https://api.star-history.com/svg?repos=Polyx10/CTB2MD&type=Date)](https://star-history.com/#Polyx10/CTB2MD&Date)

## License / Licence

MIT License
