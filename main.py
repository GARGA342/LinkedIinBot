class Bot:
    from selenium import webdriver
    from time import sleep
    from random import randint
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options

    def __init__(self):
        #Chose driver to browse
        options = self.Options()
        options.add_argument("executable_path=/home/garga/Projects/Python/LinkedInBot/geckodriver")

        #Define webdriver
        self.driver = self.webdriver.Firefox(options=options)

    def getPage(self, page):
        try:
            #Find page in browser
            self.driver.get(page)
            self.sleep(self.randint(1, 4))
        except:
            print("Não foi possível acessar o site")
            exit(1)

    def login(self):
        print(f'\n\nSeu login deve ser feito manualmente. Assim que logar, tecle ENTER.\n\n')
        input()
        self.sleep()

    def findElement(self, elem):
        try:
            #Find element in page and returns it
            return self.clickElement(self.driver.find_element(self.By.XPATH, elem))
        except:
            print(f'Não foi possível encontrar o elemento \n\t{elem}')
            exit(1)

    def clickElement(self, elem):
        try:
            #########################################################################
            pass
        except:
            print(f'Não foi possível acessar o elemento \n\t{elem}')
            exit(1)

#Open website -> "https://br.linkedin.com/"
linkedin = Bot()
linkedin.getPage("https://br.linkedin.com/")

#Enter login
linkedin.login()

#Element find
elem = linkedin.findElement("/html/body/div[5]/header/div/nav/ul/li[2]")

#Element click
#linkedin.clickElement(elem)

#    #Find element and click
#    elem = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[2]')
#    elem.click()
#
#    #Wait 4 seconds and scroll page
#    sleep(4)
#    driver.execute_script("window.scrollTo(0, 2300);")
#
#    #Wait 2 seconds and repeatedly click the "connect" button
#    sleep(2)
#
#    while(True):
#        elem = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/ul/li[1]/div/section/div[3]/footer/button/span")
#        elem.click()
#        sleep(1)
#        try:
#            elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]/span")
#            elem.click()
#            sleep(1)
#        except:
#            None        