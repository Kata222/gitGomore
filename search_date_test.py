from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://gomore.se/")

driver.find_element_by_xpath("//span[text()='Acceptera alla']").click()

driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[1]/div/div[1]").click()
driver.find_element_by_xpath("//div//input").send_keys('Malmö')
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[1]/div/div[2]/div[1]").click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/section[1]/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div').click()
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[3]/div[1]/div[1]/div[2]/div/div[3]/div[27]").click()
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[3]/div[1]/div[2]/div[2]/div/div/li[31]/span").click()

time.sleep(5)

driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[28]").click()
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[3]/div[3]/div[2]/div[2]/div/div/li[39]/span").click()

time.sleep(5)
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/button").click()

cars = driver.find_elements_by_xpath("//div[contains(@class,'js-results')]//h2")
car_names = [car.get_attribute("textContent") for car in cars]
for name in car_names:
    print("Car name: " + name)

#prices = driver.find_elements_by_xpath("//div[contains(@class,'js-results')]//span[@class='mb1']")
prices = driver.find_element_by_xpath("//div[contains(@class]//span[contains(@class,'f1') and contains(@class,'f2-sm')]")

price_values = [price.get_attribute("textContent") for price in prices]
for price in price_values:
    print("Price is " + price)








