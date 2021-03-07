from bs4 import BeautifulSoup
import requests
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
# from PyQt5.QtGui import QApplication
from PyQt5.QtWidgets import QApplication
# from PyQt4.QtCore import QUrl
from PyQt5.QtCore import QUrl
# from PyQt4.QtWebkit import QWebPage
from PyQt5.QtWebKitWidgets import QWebPage
# from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
import urllib.request
# change PyQt4 >> PyQt6
class Client(Qwebpage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connec(self.on_page_load)
        self.mainFrame().load(Qurl(url))
        self.app_exec_()
    def on_page_load(self):
        self.app.quit()
'''
#### This program scrapes naukri.com's page and gives our result as a
#### list of all the job_profiles which are currently present there.
'''
#url of the page we want to scrape
url = "https://www.naukri.com/top-jobs-by-designations# desigtop600"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'id' : 'nameSearch'})
job_profiles = all_divs.find_all('a')

# printing top ten job profiles
count = 0
for job_profile in job_profiles :
	print(job_profile.text)
	count = count + 1
	if(count == 10) :
		break

driver.close() # closing the webdriver
'''
# unfamiliar_skill = input('>')
url = 'https://translate.google.co.kr/?sl=en&tl=ko&text=press&op=translate'

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "lxml")
all_divs = soup.find('div', class_ = 'fw3eif')
print(all_divs.text)


#
# client_response = Render(url)
# client_response.show()
# source = client_response.mainFrame().toHtml()
# soup = bs.BeautifulSoup(source, 'lxml')
# js_test = soup.find('c-wiz', class_ = 'zQTmif SSPGKf RvYhPd BIdYQ aL9XFd')
# print(js_test)
#
# # def find_jobs():
# html_text = requests.get(url)
# soup = BeautifulSoup(html_text.content, 'lxml')
# work = soup.find('c-wiz', class_ = 'zQTmif SSPGKf RvYhPd BIdYQ aL9XFd')
# work2 = work.find('div', class_ = 'T4LgNb')
# work3 = work2.find('div', class_ = 'WFnNle')
# work4 = work3.find('c-wiz', class_ = 'MOkH4e BSw7K iYelWb LUoOL')
#
#
#
# work5 = work4.find('div', class_ = 'OlSOob')
# work6 = work5.find('c-wiz', class_ = 'QsA0jb')
# work7 = work6.find('div', class_ = 'kGmWO')
# work8 = work7.find('c-wiz', class_ = 'zpzJBc')
# Parser to section
# ref. https://stackoverflow.com/questions/45036358/beautifulsoup-is-not-reading-the-section-tags-as-expected
# https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python
# work9 = work8.find('section', aria-labelledby = 'rdwk3')

# print(work8.get_text)
# for index, job enumerate(jobs):
#     published_date = job.find('span', class_ = 'sim-posted').span.text
#     if 'few' in published_date:
#         company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
#         skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
#         more_info = job.header.h2.a['href']
#         if unfamiliar_skill not in skill:
#             with open(f'posts/{index}.txt. 'w') as f:
#                 f.write(f"Company Name: {company_name.strip()} \n")
#                 f.write(f"Required Skills: {skills.strip()} \n")
#                 f.write(f"More Info: {more_info}")
#             print(f'File saved: {index}')

# if __name__ == '__main__':
#     while True:
#         find_jobs()
#         time_wait = 10
#         print(f'Waiting {time_wait} minutes...')
#         time.sleep(time_wait * 60)

driver.close() # closing the webdriver
