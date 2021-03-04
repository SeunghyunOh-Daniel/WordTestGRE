from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://translate.google.co.kr/?sl=en&tl=ko&text=inclined&op=translate'
driver = webdriver.PhantomJS()
driver.get(url)

# waiting for the page to load - TODO: change
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "content")))

data = driver.page_source
driver.close()

soup = BeautifulSoup(data, "html.parser")
