from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


LOCATION = "Malmö"
@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Dator\\Desktop\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://gomore.se/")
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Acceptera alla']"))
    )
    accept_button.click()
    yield driver
    driver.quit()


def test_search_location(setup_driver):
    driver = setup_driver
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div[1]/div/div[1]"))
    )
    search_button.click()
    search_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div//input"))
    )
    search_input.send_keys(LOCATION)
    search_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/div[1]/div/div[2]/div[1]"))
    )
    search_result.click()
    expected_city = "Malmö"
    assert search_input.get_attribute("value") == expected_city

def test_select_date(setup_driver):
    driver = setup_driver
    test_search_location(driver)

    pickup_borrow_day = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[3]/div[27]/span"))
    )
    pickup_borrow_day.click()

    pickup_borrow_time = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[2]/div/div/li[8]/span"))
    )
    pickup_borrow_time.click()

    pickup_leave_day = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/div[3]/div[3]/div[1]/div[2]/div/div[3]/div[28]/span"))
    )
    pickup_leave_day.click()

    pickup_leave_time = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div/li[33]/span"))
    )
    pickup_leave_time.click()


def test_submit_search(setup_driver):
    driver = setup_driver
    test_select_date(driver)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/section[1]/div[2]/div/div/div/button"))
    )
    submit_button.click()

def test_check_search_results(setup_driver):
    driver = setup_driver
    test_submit_search(driver)

    page_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/div[2]/h1"))
    ).text
    expected_title = "Hyr bilarna i ditt närområde"
    assert page_title == expected_title

def test_choose_car_type(setup_driver):
    driver = setup_driver
    test_submit_search(driver)

    car_type_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[1]/button"))
    )
    car_type_button.click()

    window_title = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[1]/div/h3"))
    ).text

    expected_title = "Biltyp"
    assert window_title == expected_title

def test_choose_gearbox(setup_driver):
    driver = setup_driver
    test_check_search_results(driver)

    car_type_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[2]/button"))
    )
    car_type_button.click()

    window_title = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/h3"))
    ).text

    expected_title = "Växellåda"
    assert window_title == expected_title

def test_create_profile(setup_driver):
    driver = setup_driver
    test_check_search_results(driver)

    car_type_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/nav/div[2]/a[3]/span"))
    )
    car_type_button.click()

    window_title = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/h1"))
    ).text

    expected_title = "Upprätta profil på GoMore"
    assert window_title == expected_title
