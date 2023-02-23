from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://gomore.se/")

driver.find_element_by_xpath("//span[text()='Acceptera alla']").click()
driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/div[1]/div/div[1]").click()
driver.find_element_by_xpath("//div//input").send_keys('Malmö')






