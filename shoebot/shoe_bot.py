
from selenium import webdriver
from time import sleep

class ShoeBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def trypage(self):
        
        while(True):
            try:
                self.driver.get("https://www.nike.com/launch/t/acg-moc-3-0-tie-dye")
                size = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[16]/button')
                break
            except:
                print("Not online yet")
                continue
            
        
        size.click()
        addtocart = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button')
        sleep(2.5)
        addtocart.click()
        
        while(True):
            try:
                self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div/header/div[2]/section/div[2]/a/span')
                break
            except:
                continue
        
    
        self.driver.get("https://www.nike.com/us/en/checkout/tunnel")
       # checkout = self.driver.find_element_by_xpath('//*[@id="qa-guest-checkout-mobile"]')
       # sleep(3)
       # checkout.click()


def test():
    username = ''
    password = ''
    bot = ShoeBot()
    bot.trypage()
   

      
