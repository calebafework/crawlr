
import myInfo from myInfo.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains ##maybe
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time
import random

AMAZON_URL= 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_1?dchild=1&keywords=ps5&qid=1625427850&sr=8-1'
WAIT_TIME = 7
PRICE_LIMIT = 700
class gayStation:
    def __init__(self,username, password):
        """Initializes Bot with class-wide vairables."""
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    ##Sign into site
    def signIn(self):
        """ Sign into site """
        driver = self.driver ## Navigate to URL

        ## Enter Username
        ## Name is the field we are looking for. Use inspect if it's a different name.
        username_elem = driver.find_element_by_xpath("//input[@name='email']")
        username_elem.clear()
        username_elem.send_keys(self.username)

    # ON CERTAIN SITES YOU WILL HAVE TO MIMIC REAL TYPING, TYPE EACH LETTER EVERY .5 SECS OR IT WILL BE FLAGGED FOR BOTTING    
        #for letter in self.username:
        #    username_elem.send_keys(letter)

        # Time.sleep allows the website to process what you've done to make it feel more organic.
        # the website is ALWAYS slower than the local machine
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        username_elem.send_keys(Keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))

        ## Enter Password
        password_elem = driver.find_element_by_xpath("input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)

        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        password_elem.send_keys(keys.RETURN)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
    ## Find product product under X amount (not really necessary)
    def findProduct(self):
        """ finds the product with global link """
        driver = self.driver
        driver.get(AMAZON_URL)
        time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        
    ## If product not available wait until it is (not really necessary)
        isAvailable = self.isProductAvailable()

        if isAvailable == 'Currently unavailable.':
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()
        elif isAvailable <= PRICE_LIMIT:
            ## Buy Now 
            buy_now = driver.find.element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.signIn()

            # Place Order Order
                # name should be the html element name
                # .text gives string information
            place_order = driver.find_element_by_name('placeYourOrder1').text
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            ##place_order.click()
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
        else:
            time.sleep(randint(int(WAIT_TIME/2), WAIT_TIME))
            self.findProduct()

    def isProductAvailable(self):
        """ checks if product is available """
        driver = self.driver
        available = driver.find_element_by_class_name('a-color-price').text
        if available == "Currently unavailble.":
            print(f'***** AVAILABLE: {available}')
            return available
        else:
            print(f'***** PRICE: {available}')
            return float(available[1:]) ## $123.12 -> 123.12
    
    def closeBrowser(self):
        """ closes browser """ 
        self.driver.close()

if __name__ == "__main__":
    shopbot = gayStation(username=myinfo.username(), password=myinfo.password())
    shopbot.findProduct()
    shopbot.closeBrowser()

## add product to the cart 
## add payment (may not be needed)
## checkout cart 

## TO DO 
    ## MAKE AN OBJECT FOR SHIPPING DATA
    ## POTENTIAL OBJECT ALSO, FOR BILLING DATA