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

	return all_divs.text

def enterDay():
	day = input("Enter which day: ")
	if(int(day) > 30):
		print(f"error:out of range")
		return 0
	else:
		return int(day)

def makeProblem(pd_frame, day):
	numRandom = np.random.randint(1, 102, 30)
	problem_list = []
	for value in pd_frame.values:
		if(value[0] == day):
			if(value[2] in numRandom):
				problem_list.append([value[0], value[2], value[3]])
	return problem_list

def printProblem(data_list):
	print(f"--------QUIZ, DAY {data_list[0][0]:d}--------")
	for val in data_list:
		print(val[2])
	print(f"---------------------------------------------")

def main():
	#https://realpython.com/python-timer/
	tic = time.perf_counter()

	day = enterDay()
	if(day == 0):
		print(f"enter another value")

	df = pd.read_excel(data_name, sheet_name=data_sheet)
	problem_list = makeProblem(df, day)

	toc = time.perf_counter()
	print(f"Process time in {toc - tic:0.4f} secondes")

	printProblem(problem_list)

if __name__=="__main__":
	main()
