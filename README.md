# CTB2MD - Convertisseur Cherrytree vers Markdown

Une application simple pour convertir des fichiers Cherrytree (.ctb) en fichiers Markdown (.md), spécialement conçue pour macOS.

## Fonctionnalités

- Interface graphique simple avec sélecteur de fichiers
- Conversion des fichiers .ctb en Markdown
- Préservation de la mise en page et du formatage
- Support des blocs de code pour les commandes
- Compatible avec Obsidian

## Installation

1. Téléchargez la dernière version de l'application depuis la page [Releases](../../releases)
2. Décompressez l'archive
3. Glissez l'application CTB2MD.app dans votre dossier Applications

## Utilisation

1. Double-cliquez sur CTB2MD.app
2. Sélectionnez votre fichier .ctb à convertir
3. Les fichiers Markdown seront créés dans un nouveau dossier à côté du fichier source

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

## Licence

MIT License
