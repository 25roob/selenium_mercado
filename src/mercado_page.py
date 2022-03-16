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
                return None
            except:
                continue  
        
        raise ValueError("None of the registered XPATHs matches, the list shoud be actualized")

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
        xpath1 = '/html/body/div[2]/div[1]/div[2]/button[1]'
        close_coockie_disc = [xpath1]
        MercadoPage._search_by_xpaths(self, close_coockie_disc)

    def see_all_locations(self):
                               
        xpath1 = '//*[@id="root-app"]/div/div[1]/aside/section/div[15]/ul/li[10]/a'
        xpath2 = '//*[@id="root-app"]/div/div[1]/aside/section/div[16]/ul/li[10]/a'
        xpath3 = '//*[@id="root-app"]/div/div[1]/aside/form/div[15]/ul/li[10]/a'
        xpath4 = '//*[@id="root-app"]/div/div[1]/aside/form/div[16]/ul/li[10]/a'
        xpath5 = '//*[@id="root-app"]/div/div[1]/aside/form/div[14]/ul/li[10]/a'
        xpath6 = '//*[@id="modal"]/div[2]/a[13]'
        xpath7 = '//*[@id="root-app"]/div/div[1]/aside/form/div[15]/ul/li[10]/a'
        

        xpaths = [xpath1, xpath2, xpath3, xpath4, xpath5, xpath6, xpath7]
        c = 0
        while True:
            try:
                MercadoPage._search_by_xpaths(self, xpaths)
                return None
            except:
                self._driver.refresh()
                c += 5
            if c == 5:
                raise ValueError('Too many failed attempts at see_all_locations func')
        
    def select_location_guerrero(self):

        MercadoPage.see_all_locations(self)
        
        xpath1 = '//*[@id="modal"]/div[2]/a[13]'
        xpath2 = '//*[@id="modal"]/div[2]/div[6]/div[2]/a[2]'
        
        xpaths = [xpath1, xpath2]
        
        MercadoPage._search_by_xpaths(self, xpaths)

        
    # TODO: make one method 'select_location_(location)' for every state using XPATH

    def select_condition_nuevo(self):
        
        xpath1 = '/html/body/main/div/div[1]/aside/section/div[6]/ul/li[1]/a'
        xpath2 = '//*[@id="root-app"]/div/div[1]/aside/form/div[6]/ul/li[1]/button'
        xpath3 = '//*[@id="root-app"]/div/div[1]/aside/form/div[3]/ul/li[1]/button'

        xpaths = [xpath1, xpath2, xpath3]

        MercadoPage._search_by_xpaths(self, xpaths)


    # TODO: make a method simmilar to the one above for the "used" condition

    def sorting_option(self, option):
        xpath_s_s_button = '//*[@id="root-app"]/div/div[1]/section/div[1]/div/div/div/div[2]/div/div/button'
        xpath_s_o_mayor_precio = '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/div/ul/a[2]'
        xpath_confirm_option = '//*[@id="root-app"]/div/div/section/div[1]/div/div/div/div[2]/div/div/button/span'

        sort_select_button = self._driver.find_element(By.XPATH, xpath_s_s_button)
        sort_select_button.click()

        # TODO add a way to click in the different options
        if option == 'importance':
            pass
        elif option == 'asc_price':
            pass
        elif option == 'desc_price':
            select_mayor_precio = self._driver.find_element(By.XPATH, xpath_s_o_mayor_precio)
            select_mayor_precio.click()
            # WebDriverWait(self._driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, xpath_confirm_option), 'Mayor precio'))
            # self._driver.implicitly_wait(3)
        else:
            raise ValueError('Unexpected option\n\nValid options: \n* importance\n* asc_price\n* desc_price')

    def scrape_results(self):
        xpath1 = '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a/div/div[3]/h2'
        xpath2 = '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[2]/div/div/a/div/div[3]/h2'
        xpath3 = '//*[@id="root-app"]/div/div[1]/section/ol[2]/li[1]/div/div/a/div/div[3]/h2'
        xpath3 = '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[3]/div/div/a/div/div[3]/h2'
        #         //*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a/div/div[3]/h2
        

        result, price = '', ''
        while result == '' or price == '':         
            try: 
                result = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a/div/div[3]/h2')
                texto = result.text
                price = self._driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a/div/div[1]/div/div/div/span[1]/span[2]/span[2]')
                price_t = price.text
            except:
                # raise ValueError("None of the registered XPATHs matches, the list shoud be actualized")
                self._driver.refresh()

        print('----->' + texto + ' ' + price_t + '<------')

        c = 0
        results = []
        prices = []
        for j in range(24):
            try: 

                for i in range(2):
                    try:
                        result = self._driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[1]/section/ol[{j+1}]/li[{i+1}]/div/div/a/div/div[3]/h2')
                        print(str(result.text), end='')
                        results.append(result.text)
                        price = self._driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[1]/section/ol[{j+1}]/li[{i+1}]/div/div/a/div/div[1]/div/div/div/span[1]/span[2]/span[2]')
                        print(' ' + str(price.text))
                        prices.append(price.text)
                        c += 1
                    except:
                        continue
            except:
                continue
        print('Elementos encontrados: ' + str(c))
        print(results)
        print(prices)

        # ol, li = 1, 1
        # names = []
        # for _ in range(50):
        #     try:
        #         product = self._driver.find_element(By.XPATH, f'//*[@id="root-app"]/div/div[1]/section/ol[{ol}]/li[{li}]/div/div/a/div/div[3]/h2').text
        #         names.append(product)
        #         li += 1
        #     except:
        #         ol += 1
                       
        
        # print('Se encontraron' + str(len(names)))

