#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import os
import sys
import re
import shutil

ban_ign_id_t = "ban-{}.csv.gz"
ban_p = re.compile("^ban-([AB0-9]+).csv.gz")
result_dir = "ban-ign-id"
source_dir = "ban"

# On vérifie que le fichier est identifique avant et après ajour de la colonne ign

for source_file in os.listdir(source_dir):
    if ban_p.match(source_file):
        n = re.search(ban_p,source_file).group(1)
        result_file = ban_ign_id_t.format(n)
        print("Vérification de " + str(result_file))
        df_ban = pd.read_csv(os.path.join(source_dir,source_file),sep=';',encoding='utf-8',dtype=object)
        df_ban_ign = pd.read_csv(os.path.join(result_dir,result_file),sep=';',encoding='utf-8',dtype=object)
        df_ban_ign = df_ban_ign.drop(['ign'],axis=1)
        if not df_ban.equals(df_ban_ign):
            print("ERREUR !")
            sys.exit(0)
