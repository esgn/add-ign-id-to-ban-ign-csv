#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import sys
import re
import shutil

hn_dir = "housenumber-id-ign"
hn_p = re.compile("^housenumber-id-ign-([AB0-9]+).csv.gz")

for hn_file in os.listdir(hn_dir):
    if hn_p.match(hn_file):
        print("Vérification de " + str(hn_file))
        df_hn = pd.read_csv(os.path.join(hn_dir, hn_file),
                            sep=';', encoding='utf-8', dtype=object)
        if df_hn['id_ban_adresse'].duplicated().any():
            print("[ERREUR] Doublons sur id_ban_adresse")
            sys.exit(0)
        if df_hn['ign'].duplicated().any():
            print("[ERREUR] Doublons sur ign")
            sys.exit(0)
        if df_hn['id_ban_adresse'].isnull().values.any():
            print("[ERREUR] Valeurs nulles dans id_ban_adresse")
            sys.exit(0)
        if df_hn['ign'].isnull().values.any():
            print("[ERREUR] Valeurs nulles dans id_ban_adresse")
            sys.exit(0)
    else:
        print("[ERREUR] Nom du fichier invalide : " + hn_file)
        sys.exit(0)
