from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://gomore.se/")

driver.find_element("xpath","//span[text()='Acceptera alla']").click()

driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div[1]/div/div[1]").click()
driver.find_element("xpath","//div//input").send_keys('Malmö')
driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/div[1]/div/div[2]/div[1]").click()
time.sleep(5)

driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[3]/div[27]/span").click()
driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div/li[8]/span").click()
time.sleep(5)

driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[28]/span").click()
driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div/li[33]/span").click()

time.sleep(5)
driver.find_element("xpath","/html/body/section[1]/div[2]/div/div/div/button").click()

cars = driver.find_elements("xpath","//div[contains(@class,'js-results')]//h2")
car_names = [car.get_attribute("textContent") for car in cars]
for name in car_names:
    print("Car name: " + name)