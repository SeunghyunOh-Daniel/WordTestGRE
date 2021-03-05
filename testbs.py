from bs4 import BeautifulSoup
import requests
import time

# unfamiliar_skill = input('>')
url = 'https://translate.google.co.kr/?sl=en&tl=ko&text=inclined&op=translate'
# def find_jobs():
html_text = requests.get(url)
soup = BeautifulSoup(html_text.content, 'lxml')
work = soup.find('c-wiz', class_ = 'zQTmif SSPGKf RvYhPd BIdYQ aL9XFd')
work2 = work.find('div', class_ = 'T4LgNb')
work3 = work2.find('div', class_ = 'WFnNle')
work4 = work3.find('c-wiz', class_ = 'MOkH4e BSw7K iYelWb LUoOL')



work5 = work4.find('div', class_ = 'OlSOob')
work6 = work5.find('c-wiz', class_ = 'QsA0jb')
work7 = work6.find('div', class_ = 'kGmWO')
work8 = work7.find('c-wiz', class_ = 'zpzJBc')
# Parser to section
# ref. https://stackoverflow.com/questions/45036358/beautifulsoup-is-not-reading-the-section-tags-as-expected
# https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python
# work9 = work8.find('section', aria-labelledby = 'rdwk3')

print(work8.get_text)
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
