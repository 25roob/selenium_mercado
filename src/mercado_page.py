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
        WebDriverWait(self._driver, 5).until(EC.presence_of_element_located((By.NAME, 'as_word')))
        return True

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'as_word')
        return input_field.get_attribute('value')

    @property
    def word_searched(self):
        word_searched = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/aside/div[1]/h1')
        return word_searched.text.lower()

    # This fuunction receives a list of possible working xpaths
    def _search_by_xpaths(self, xpaths):
            # WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            # elemento = self._driver.find_element(By.XPATH, xpath)
            # elemento.click()
            for xpath in xpaths: 
                try:
                    elemento = self._driver.find_element(By.XPATH, xpath)
                    elemento.click()
                    break
                except:
                    continue  

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
                       
        xpath1 = '//*[@id="root-app"]/div/div[1]/aside/section/div[15]/ul/li[10]/a'
        xpath2 = '//*[@id="root-app"]/div/div[1]/aside/section/div[16]/ul/li[10]/a'
        xpath3 = '//*[@id="root-app"]/div/div[1]/aside/form/div[15]/ul/li[10]/a'
        xpath4 = '//*[@id="root-app"]/div/div[1]/aside/form/div[16]/ul/li[10]/a'

        xpaths = [xpath1, xpath2, xpath3, xpath4]

        # def _search_by_xpaths(xpath):
        #     # WebDriverWait(self._driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        #     see_all = self._driver.find_element(By.XPATH, xpath)
        #     see_all.click()

        
        # for ixpath in xpaths: 
        #     try:
        #         MercadoPage._search_by_xpaths(self, ixpath)
        #         break
        #     except:
        #         continue         
        
        MercadoPage._search_by_xpaths(self, xpaths)
          

    # def close_coockiedisclaimer(self):
    #     self._driver.find_element(By.ID, 'newCookieDisclaimerButton').click()

    def select_location_guerrero(self):

        MercadoPage.see_all_locations(self)
        
        # def _search_by_xpaths(xpath):
        #     WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        #     select_location = self._driver.find_element(By.XPATH, xpath)
        #     select_location.click()

        xpath1 = '//*[@id="modal"]/div[2]/a[13]'
        xpath2 = '//*[@id="modal"]/div[2]/div[6]/div[2]/a[2]'
        #         //*[@id="modal"]/div[2]/div[6]/div[2]/a[2]
        #         //*[@id="modal"]/div[2]/a[13]

        xpaths = [xpath1, xpath2]
                
        # try:
        #     MercadoPage._search_by_xpaths(self, xpath1)
        # except:
        #     MercadoPage._search_by_xpaths(self, xpath2)

        MercadoPage._search_by_xpaths(self, xpaths)

        
    # TODO: make one method 'select_location_(location)' for every state using XPATH

    def select_condition_nuevo(self):
        # WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a')))
        # condition_button = self._driver.find_element(By.XPATH, '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a')
        # condition_button.click()

        xpath1 = '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a'
        xpath2 = '//*[@id="root-app"]/div/div[1]/aside/form/div[6]/ul/li[1]/button'

        xpaths = [xpath1, xpath2]

        MercadoPage._search_by_xpaths(self, xpaths)


    # TODO: make a method simmilar to the one above for the "used" condition

    def sorting_option(self, option):
        sort_select_button = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/section/div[1]/div/div/div/div[2]/div/div/button')
        sort_select_button.click()
        # TODO add a way to click in the different options
        if option == 'importance':
            pass
        elif option == 'asc_price':
            pass
        elif option == 'desc_price':
            select_mayor_precio = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]')
            select_mayor_precio.click()
            WebDriverWait(self._driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/button/span'), 'Mayor precio'))
            self._driver.implicitly_wait(3)
        else:
            raise ValueError('Unexpected option\n\nValid options: \n* importance\n* asc_price\n* desc_price')

    def scrape_results(self):
        pass
