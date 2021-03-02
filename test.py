# from googletrans import Translator
import requests
from bs4 import BeautifulSoup

def main():
	# translator = Translator()
	# result = translator.translate('inclined', dest = 'ko')

	# print(result.src)
	# print(result.dest)
	# print(result.text)
	
	url = 'https://translate.google.com/?hl=en&tab=TT&sl=en&tl=ko&text=inclined&op=translate'
	response =  requests.get(url)

	if response.status_code == 200:
		html = response.text
		soup = BeautifulSoup(html, 'html.parser')
		title = soup.select_one('#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.kGmWO > c-wiz > section > div > div > div.Sp3AF > div:nth-child(1) > div > div > div.eqNifb > div.JAk00.OvhKBb')	
		print(title)

	else:
		print("out")
		print(response.status_code)
if __name__=="__main__":
	main();