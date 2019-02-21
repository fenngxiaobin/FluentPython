import os
import time
import sys
import re

import requests

# 列出国旗列表
flags = ("china","chaoxian","laowo","yuenan","yindu")

BASE_URL = "https://www.supfree.net/pagefile/6123"

DEST_DIR = "./Flag_Pics"

def get_all_pics(url):
    '''
     获取所有图片的地址 使用正则表达式匹配
    '''
    rsp = requests.get(url)
    htm = rsp.content.decode('gbk')
    pic_list = re.findall('src="/pagefile/6123/\w*.gif"',htm)
    print(pic_list)
    for i in range(len(pic_list)):
        pic_list[i] = pic_list[i].split('/')[3].split('.')[0]
    return pic_list


def save_pic(img,filename):
    '''
     保存图片
    '''
    path = os.path.join(DEST_DIR,filename)
    with open(path,'wb') as fb:
        fb.write(img)


def get_pic(cc):
    '''
     下载文件
    '''
    url = "{}/{cc}.gif".format(BASE_URL,cc=cc)
    resp = requests.get(url)
    return resp.content

def show(text):
    '''
     显示进度
    '''
    print(text,end = " ")
    sys.stdout.flush()

def download_many(cc_list):
    '''
     批量顺序下载
    '''
    for cc in cc_list:
        image = get_pic(cc)
        show(cc)
        save_pic(image,cc+".gif")
    return len(cc_list)

if __name__ == "__main__":
    url = "https://www.supfree.net/search.asp?id=6123" 
    name_lists = get_all_pics(url)
    t0 = time.time()
    download_many(name_lists)
    delta = time.time() - t0
    print(delta)
