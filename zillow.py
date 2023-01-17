from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import time

output = []


class Bot():
    def __init__(self):

        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.get('https://www.zillow.com/gulfport-fl/sold/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Gulfport%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-82.75872495275878%2C%22east%22%3A-82.6583030472412%2C%22south%22%3A27.714824334088206%2C%22north%22%3A27.777568735527446%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24990%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22filterState%22%3A%7B%22doz%22%3A%7B%22value%22%3A%2236m%22%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D')

    def click(self, xpath, timex, DEBUG_NAME):
        try:
            self.driver.find_element_by_xpath(xpath).click()
            time.sleep(timex)
            print(f'clicked {DEBUG_NAME}')
        except NoSuchElementException:
            print(f'element {DEBUG_NAME} was not found ')
        except ElementNotInteractableException:
            print(f'element {DEBUG_NAME} is not interactable ')

    def type(self, xpath, words, timex, DEBUG_NAME):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(words)
            time.sleep(timex)
            print(f'typed {DEBUG_NAME}')
        except NoSuchElementException:
            print(f'element {DEBUG_NAME} was not found ')
        except ElementNotInteractableException:
            print(f'element {DEBUG_NAME} is not interactable ')

    def clear_type(self, xpath, timex, DEBUG_NAME):
        try:
            self.driver.find_element_by_xpath(xpath).clear()
            time.sleep(timex)
            print(f'typed {DEBUG_NAME}')
        except NoSuchElementException:
            print(f'element {DEBUG_NAME} was not found ')
        except ElementNotInteractableException:
            print(f'element {DEBUG_NAME} is not interactable ')

    def get_attribute(self, xpath, attribute, DEBUG_NAME):
        try:
            return self.driver.find_element_by_xpath(xpath).get_attribute(attribute)
        except NoSuchElementException:
            print(f'element {DEBUG_NAME} was not found ')
        except NoSuchAttributeException:
            print(
                f'attribute {attribute} in element {DEBUG_NAME} was not found ')

    def getAdvancedAttribute(self, method, methodValue, attribute,  DEBUG_NAME):
        try:

            if method == 'class_name':
                return self.driver.find_element_by_class_name(methodValue).get_attribute(attribute)
            if method == 'xpath':
                return self.driver.find_element_by_xpath(methodValue).get_attribute(attribute)
            if method == 'tag_name':
                return self.driver.find_element_by_tag_name(methodValue).get_attribute(attribute)
            if method == 'name':
                return self.driver.find_element_by_name(methodValue).get_attribute(attribute)
            if method == 'css_selector':
                self.driver.find_element_by_css_selector(
                    methodValue).get_attribute(attribute)
        except Exception:
            print(f'Exception {Exception} in function getAdvancedAttribute')

    def getText(self, xpath, DEBUG_NAME):
        try:
            return self.driver.find_element_by_xpath(xpath).text
        except NoSuchElementException:
            print(f'element not found DEBUG_NAME: {DEBUG_NAME} xpath: {xpath}')
        except NoSuchAttributeException:
            print(
                f'attribute not found DEBUG_NAME: {DEBUG_NAME} xpath: {xpath}')

    def getChildren(self, xpath, DEBUG_NAME):
        try:

            if str(xpath)[0] == '<':

                return xpath.find_elements_by_xpath('./*')
            else:
                return self.driver.find_element_by_xpath(xpath).find_elements_by_xpath('./*')
        except NoSuchElementException:
            print(
                f'attribute not found DEBUG_NAME: {DEBUG_NAME} xpath: {xpath}')
        except NoSuchAttributeException:
            print(
                f'attribute not found DEBUG_NAME: {DEBUG_NAME} xpath: {xpath}')

    def main(self):
        with open('test.txt', 'r') as file:
            lines = file.readlines()

        for line in lines:
            self.driver.get(line)
            time.sleep(3)
            address = self.getText(
                '/html/body/div[1]/div[6]/div[3]/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h1/span[1]', 'ADDRESS')
            print(address)


bot = Bot()
bot.main()
# /html/body/div[1]/div[5]/div/div/div/div[1]/ul/li[2]/article/div[2]/a
