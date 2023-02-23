from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://gomore.se/")

driver.find_element("xpath","//span[text()='Acceptera alla']" ).click()
driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div[1]/div/div[1]").click()
driver.find_element("xpath","//div//input").send_keys('Malmö')









