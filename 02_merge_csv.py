#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import os
import sys
import re
import shutil
from multiprocessing.pool import ThreadPool

ban_p = re.compile("^ban-([AB0-9]+).csv.gz")
hn_t = "housenumber-id-ign-{}.csv.gz"
out_dir = "ban-ign-id"
jobs = 6

if os.path.exists(out_dir):
    shutil.rmtree(out_dir)
os.mkdir(out_dir)

def merge_file(ban_f):
    n = re.search(ban_p,ban_f).group(1)
    hn_f = hn_t.format(n)
    df_ban = pd.read_csv("ban/"+ban_f,sep=';',encoding='utf-8',dtype=object)
    df_hn = pd.read_csv("housenumber-id-ign/"+hn_f,sep=';',encoding='utf-8')
    result = df_ban.merge(df_hn,how='left',on='id_ban_adresse')
    out_file = 'ban-'+n+'.csv.gz'
    result.to_csv(os.path.join(out_dir,out_file),index=False,encoding='utf-8',sep=';',compression='gzip')
    return str(ban_f) + " traité"

def main():
    file_list = os.listdir("ban")
    results = ThreadPool(jobs).imap_unordered(merge_file,file_list)
    for r in results:
        print(r)

if __name__ == "__main__":
    main()
