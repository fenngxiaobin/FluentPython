import os
import time
import sys
import re

import requests
from concurrent import futures
from flags import get_all_pics,save_pic,get_pic,show

MAX_WORKERS = 20
BASE_URL = "https://www.supfree.net/pagefile/6123"
DEST_DIR = "./Flag_Pics"

def download_one(cc):
    image = get_pic(cc)
    show(cc)
    save_pic(image,cc+".gif")
    return cc

def download_many(cc_list):
    workers = min(MAX_WORKERS,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one,cc_list)
    return len(cc_list)

if __name__ == "__main__":
    url = "https://www.supfree.net/search.asp?id=6123"
    name_lists = get_all_pics(url)
    print(len(name_lists))
    t0 = time.time()
    download_many(name_lists)
    delta = time.time()-t0
    print(delta)

