from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class MercadoPage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://www.mercadolibre.com/'
        self.search_locator = 'as_word'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'as_word')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        return input_field.get_attribute('value')

    @property
    def word_searched(self):
        word_searched = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/div[1]/h1')
        return word_searched.text.lower()

    def open(self):
        self._driver.get(self._url)

    def search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.clear()
        input_field.send_keys(keyword)

    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        input_field.submit()

    def select_country(self, country_ID):
        country_button = self._driver.find_element(By.ID, country_ID)
        country_button.click()

    def see_all_locations(self):
        self._driver.find_element(By.ID, 'newCookieDisclaimerButton').click()
        # WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/aside/section/div[16]/ul/li[10]/a')))
        see_all = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/section/div[15]/ul/li[10]/a')
        see_all.click()
        
        # //*[@id="root-app"]/div/div[1]/aside/section/div[15]/ul/li[10]/a

    # def close_coockiedisclaimer(self):
    #     self._driver.find_element(By.ID, 'newCookieDisclaimerButton').click()

    def select_location_guerrero(self):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modal"]/div[2]/a[13]')))
        select_location = self._driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/a[13]')
        select_location.click()
        
        # //*[@id="modal"]/div[2]/a[13]
        # //*[@id="modal"]/div[2]/div[6]/div[2]/a[2]

    # TODO: make one method 'select_location_(location)' for every state using XPATH

    def select_condition_nuevo(self):
        WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a')))
        condition_button = self._driver.find_element(By.XPATH, '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a')
        condition_button.click()

    # TODO: make a method simmilar to the one above for used condition

    def scrape_results(self):
        pass
