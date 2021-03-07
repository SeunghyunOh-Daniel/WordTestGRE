import os,sys
import random
import time
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
import requests
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

'''
# How to install chromedriver and parsing
import chromedriver_install as cdi
path = cdi.install(file_directory='c:\\data\\chromedriver\\', verbose=True, chmod=True, overwrite=False, version=None)
print('Installed chromedriver to path: %s' % path)
'''
sys.path.append("/Users/seunghyunoh/workplace/Data/")
data_path = "/Users/seunghyunoh/workplace/Data/wordlist/"
data_name = "1.xlsx"
data_sheet = "표제어 list"
data_result = "result/result.txt"

def search_mean(word):

    urlRef = ['https://translate.google.co.kr/?sl=en&tl=ko&text=', '&op=translate']
    url = urlRef[0]+str(word)+urlRef[1]
    print(url)
    # initiating the webdriver. Parameter includes the path of the webdriver.
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url)

    # if you search about dynamic driver, then you have to wait 'loading'
    # this is just to ensure that the page is loaded
    time.sleep(5)

    html = driver.page_source

    # this renders the JS code and stores all
    # of the information in static HTML code.

    # Now, we could simply apply bs4 to html variable, html.parser or lxml
    soup = BeautifulSoup(html, "lxml")
    all_divs = soup.find('div', class_ = 'fw3eif')
    try:
        mean = all_divs.text
    except AttributeError:
        mean = 'NonePage'
    driver.close()
    return mean

def search_means(word_list):
    driver = webdriver.Chrome('./chromedriver')
    for i in range(len(word_list)):
        urlRef = ['https://translate.google.co.kr/?sl=en&tl=ko&text=', '&op=translate']
        url = urlRef[0]+str(word_list[i][2])+urlRef[1]
        print(url)
        # initiating the webdriver. Parameter includes the path of the webdriver.
        driver.get(url)

        # if you search about dynamic driver, then you have to wait 'loading'
        # this is just to ensure that the page is loaded
        time.sleep(5)

        html = driver.page_source

        # this renders the JS code and stores all
        # of the information in static HTML code.

        # Now, we could simply apply bs4 to html variable, html.parser or lxml
        soup = BeautifulSoup(html, "lxml")
        all_divs = soup.find('div', class_ = 'fw3eif')
        try:
            mean = all_divs.text
        except AttributeError:
            mean = 'NonePage'

        word_list[i].append(mean)

    driver.close()

def import_words(pd_frame):
    word_list = []
    for value in pd_frame.values:
        word_list.append([value[0], value[2], value[3]])
    return word_list

def add_mean2word(data_list):
    # data_list[2]: word
    for i in range(len(data_list)):
        data_list[i].append(search_mean(data_list[i][2]))

    for i in range(len(data_list)):
        print(data_list[i][3])

    return(data_list)

def export_data(data_list):
    with open(data_name.split(".")[0]+'.txt', 'w+') as f:
        #enumerate
        cnt = 0
        for x in range(len(data_list)):
            f.write(str(cnt)+", ")
            for y in range(len(data_list[x])):
                print(f"({x},{y})")
                if(y == len(data_list[x])-1):
                    f.write(str(data_list[x][y])+"\n")
                    continue
                f.write(str(data_list[x][y])+", ")
            cnt = cnt + 1

def main():
	#https://realpython.com/python-timer/
    tic = time.perf_counter()
    df = pd.read_excel(data_name, sheet_name=data_sheet)
    words = import_words(df)
    search_means(words)
    export_data(words)
    toc = time.perf_counter()
    print(f"Process time in {toc - tic:0.4f} secondes")


if __name__=="__main__":
	main()
