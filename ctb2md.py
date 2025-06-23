#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import re

class CTB2MD:
    def __init__(self):
        # Créer et cacher la fenêtre principale
        self.root = tk.Tk()
        self.root.withdraw()
        
        # Demander à l'utilisateur de choisir un fichier
        file_path = filedialog.askopenfilename(
            title="Choisir un fichier Cherrytree",
            filetypes=[("Fichiers Cherrytree", "*.ctb"), ("Tous les fichiers", "*.*")]
        )
        
        if file_path:
            self.convert_file(file_path)
    
    @staticmethod
    def clean_xml_content(content):
        # Supprimer les balises XML et leurs attributs
        content = re.sub(r'<\?xml.*?\?>', '', content)
        content = re.sub(r'<node.*?>', '', content)
        content = re.sub(r'</node>', '', content)
        content = re.sub(r'<rich_text.*?>', '', content)
        content = re.sub(r'</rich_text>', '', content)
        return content

    def convert_file(self, input_path):
        try:
            # Créer le dossier de sortie (même nom que le fichier sans extension)
            output_dir = os.path.splitext(input_path)[0]
            os.makedirs(output_dir, exist_ok=True)
            
            # Connexion à la base SQLite
            with sqlite3.connect(input_path) as conn:
                cursor = conn.cursor()
                
                # Examiner la structure de la table
                cursor.execute("PRAGMA table_info(node)")
                columns = cursor.fetchall()
                # Récupérer tous les nœuds avec toutes les colonnes
                cursor.execute("SELECT * FROM node ORDER BY node_id")
                nodes = cursor.fetchall()
                
                # Convertir chaque nœud
                for node in nodes:
                    # Récupérer les données du nœud
                    node_data = dict(zip([col[1] for col in columns], node))
                    name = node_data.get('name', 'sans_titre')
                    content = node_data.get('txt', '')
                    syntax = node_data.get('syntax', 'plain')
                    
                    # Nettoyer le nom pour le fichier
                    safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in name)
                    safe_name = safe_name.strip() or "sans_titre"
                    
                    if content:
                        # Nettoyer le contenu XML
                        content = self.clean_xml_content(content)
                        
                        # Gérer les attributs weight et link
                        while ' weight="heavy"' in content:
                            content = content.replace(' weight="heavy"', '')
                        while ' link="' in content:
                            start = content.find(' link="')
                            end = content.find('"', start + 7)
                            if end != -1:
                                link = content[start + 7:end]
                                content = content[:start] + content[end + 1:]
                                # Ajouter le lien en format Markdown s'il existe
                                if link.startswith('webs '):
                                    url = link[5:]
                                    content = content.replace(url, f'[{url}]({url})')
                        
                        # Convertir les entités HTML
                        content = content.replace("&lt;", "<").replace("&gt;", ">")
                        content = content.replace("&amp;", "&")
                        
                        # Normaliser les sauts de ligne
                        content = content.replace("\r\n", "\n").replace("\r", "\n")
                        
                        # Si c'est du texte brut
                        if syntax == 'plain':
                            # Séparer en lignes
                            lines = []
                            in_command_block = False
                            command_lines = []
                            
                            for line in content.split("\n"):
                                line = line.strip()
                                
                                # Si c'est une ligne de commande
                                if any(cmd in line for cmd in ['sudo', 'clamscan']):
                                    if not in_command_block:
                                        if command_lines:  # Finir le bloc précédent
                                            lines.extend(['```bash', '\n'.join(command_lines), '```', ''])
                                            command_lines = []
                                        in_command_block = True
                                    command_lines.append(line)
                                else:
                                    if in_command_block:
                                        # Finir le bloc de commandes
                                        if command_lines:
                                            lines.extend(['```bash', '\n'.join(command_lines), '```', ''])
                                            command_lines = []
                                        in_command_block = False
                                    
                                    if line:  # Ligne normale avec texte
                                        lines.append(line)
                                    else:  # Ligne vide
                                        if lines and lines[-1] != '':
                                            lines.append('')
                            
                            # Gérer le dernier bloc de commandes si nécessaire
                            if command_lines:
                                lines.extend(['```bash', '\n'.join(command_lines), '```'])
                            
                            # Joindre toutes les lignes
                            content = "\n".join(lines)
                        else:
                            # Convertir les balises HTML en Markdown
                            content = content.replace("<b>", "**").replace("</b>", "**")
                            content = content.replace("<i>", "_").replace("</i>", "_")
                            content = content.replace("<code>", "`").replace("</code>", "`")
                            content = content.replace("<s>", "~~").replace("</s>", "~~")
                            
                            # Gérer les listes
                            content = content.replace("<ul>", "\n").replace("</ul>", "\n")
                            content = content.replace("<ol>", "\n").replace("</ol>", "\n")
                            content = content.replace("<li>", "* ").replace("</li>", "\n")
                            
                            # Gérer les paragraphes
                            content = content.replace("<p>", "").replace("</p>", "\n\n")
                            content = content.replace("<br/>", "\n")
                            content = content.replace("<br>", "\n")
                            
                            # Préserver les espaces au début des lignes
                            lines = content.split("\n")
                            content = "\n".join(line.rstrip() for line in lines)
                        
                        # Préserver les lignes vides multiples car elles font partie de la mise en page
                        content = "\n".join(content.split("\n"))
                        
                        # Assurer des sauts de ligne avant les titres
                        content = content.replace("\n#", "\n\n#")
                    
                    # Écrire le fichier Markdown
                    with open(f"{output_dir}/{safe_name}.md", 'w', encoding='utf-8') as f:
                        f.write(f"# {name}\n\n{content if content else ''}")
            
            messagebox.showinfo("Succès", f"Conversion terminée ! Les fichiers ont été créés dans :\n{output_dir}")
            
            # Proposer d'ouvrir le dossier
            if messagebox.askyesno("Ouvrir le dossier", "Voulez-vous ouvrir le dossier contenant les fichiers convertis ?"):
                os.system(f'open "{output_dir}"')
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la conversion :\n{str(e)}")
    

if __name__ == '__main__':
    CTB2MD()
