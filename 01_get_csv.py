import requests
from bs4 import BeautifulSoup
import os
import shutil
import sys
from multiprocessing.pool import ThreadPool

jobs = 5
out_dir = ""

def extract_all_links_from_webpage(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser').find_all('a')
    links = [link.get('href') for link in soup]
    return links

def download_file_from_url(url):
    file_name_start_pos = url.rfind("/") + 1
    filename = url[file_name_start_pos:]
    out_file = os.path.join(out_dir, filename)
    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(out_file, 'wb') as f:
            for data in r:
                f.write(data)
    else:
        print(filename + " failed")
        print("ERROR DOWNLOADING FILE")
        sys.exit(0)
    return filename + " downloaded"

def download_dataset(url,output_directory):
    all_links = extract_all_links_from_webpage(url)
    all_links = all_links[1:] 
    all_links = [url+x for x in all_links]
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.mkdir(output_directory)
    global out_dir 
    out_dir = output_directory
    results = ThreadPool(jobs).imap_unordered(download_file_from_url, all_links)
    for r in results:
        print(r)   

def main():    
    # GET HOUSENUMBER
    url="https://adresse.data.gouv.fr/data/ban/export-api-gestion/latest/housenumber-id-ign/"
    out_dir = "housenumber-id-ign"
    download_dataset(url,out_dir)
    # GET IGN BAN
    url="https://adresse.data.gouv.fr/data/ban/export-api-gestion/latest/ban/"
    out_dir = "ban"
    download_dataset(url,out_dir)

if __name__ == "__main__":
    main()
