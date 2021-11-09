# add-ign-id-to-ban-ign-csv

## Préalables

`pip3 install -r requirements.txt`

## Récupération des fichiers de la BAN IGN 

Le script `01_get_csv.py` récupère les CSV `ban-dept` et `housenumber-id-ign-dept`.

Les fichiers `housenumber-id-ign-dept` effectuent le lien entre une `id_ban_adresse` IGN et une `cleabs` IGN c'est à dire l'identifiant unique de l'adresse dans la BDTOPOV3 de l'IGN.

Le script `check_hn` permet de s'assurer du contenu des fichiers `housenumber-id-ign-dept`.
* Vérification de l'absence de doublons sur `id_ban_adresse` et `cleabs` 
* Vérification de l'absence de valeur nulle

## Ajout de la `cleabs` IGN aux fichiers `ban-dept`

Le script `02_merge_csv.py` permet de rajouter aux fichiers `ban-dept` une colonne `ign` contenant la `cleabs` IGN correspondant à l'`id_ban_adresse`. Les fichiers résultats sont produits dans le dossier `ban-ign-id`.

Le script `check_result.py` permet de vérifier succinctement le contenu des fichiers résultats obtenus.
