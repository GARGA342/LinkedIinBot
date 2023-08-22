from selenium import webdriver
from time import sleep
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement

class Bot():
    def __init__(self):
        #Chose driver to browse
        options = Options()
        options.add_argument("executable_path=/home/garga/Projects/Python/LinkedInBot/geckodriver")

        #Define webdriver
        self.driver = webdriver.Firefox(options=options)

    def getPage(self, page = ""):
        try:
            #Find page in browser
            self.driver.get(page)
            sleep(randint(1, 4))
        except:    
            print("Não foi possível acessar o site")
            exit(1) 

    def login():
        print(f'\n\nSeu login deve ser feito manualmente. Assim que logar, tecle ENTER.\n\n')
        input()
        sleep(randint(1, 4))

    def findElement(self, elem = "") -> any:
        try:
            #Find element in page and returns it
            return self.driver.find_element(By.XPATH, elem)
        
        except:
            print(f'Não foi possível encontrar o elemento \n\t{elem}')
            return False

    def clickElement(elem) -> bool:
        try:
            elem.click()
            sleep(randint(1, 4))
            return True
        except:                
            return False

    def refreshPage(self):
            self.driver.refresh
            sleep(randint(1, 4))

bot = Bot()

#Open website -> "https://br.linkedin.com/"
bot.getPage("https://br.linkedin.com/?original_referer=")

#Enter login manually
bot.login()

#Element find
elem = bot.findElement("/html/body/div[5]/header/div/nav/ul/li[2]")

#Element click
bot.clickElement(elem)

#Find element and click
bot.clickElement(bot.findElement("/html/body/div[5]/header/div/nav/ul/li[2]"))

#Scroll page
bot.scrollPage()

i=1
while(True):
    #Repeatedly click the "connect" button
    elem = bot.findElement(f'/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/ul/li[{i}]/div/section/div[3]/footer/button/span')
                    
    if isinstance(elem, WebElement):
        bot.clickElement(elem)
        i+=1
    else:
        bot.refreshPage()
        i=1