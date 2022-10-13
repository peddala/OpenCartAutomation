from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Register import  AccountRegisteration
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() # for logging

    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    def test_login(self,setup):
        self.logger.info("**** Starting test_002_login........*** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  ###creating object of the class HomePage
        self.logger.info("clicking on MyAccount--> Login")
        self.hp.clickMyAcconut()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login.png")
            assert False

        self.driver.close()




