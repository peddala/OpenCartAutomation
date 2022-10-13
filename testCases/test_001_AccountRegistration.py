from pageObjects.HomePage import HomePage
from pageObjects.Register import  AccountRegisteration
from utilities import randomString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() # for logging

    def test_account_reg(self,setup):
        ###launching the application
        self.logger.info("**** test_001_AccountRegistration started *** ")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.hp=HomePage(self.driver) ###creating object of the class HomePage
        self.logger.info("clicking on MyAccount--> register")
        self.hp.clickMyAcconut()
        self.hp.clickRegister()

        self.logger.info("Proving customer details for registration")
        self.regpage=AccountRegisteration(self.driver)##creating the object of the Class AccountRegistration
        self.regpage.setFirstName("John")
        self.regpage.setLastName("xxx")
        self.email=randomString.random_string_generator()+"@gmail.com"
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("abc123")
        self.regpage.clickPrivacyPolicy()
        self.regpage.clickContinue()
        self.confirmationMsg=self.regpage.getConfirmationMsg()
        # if self.confirmationMsg=="Your Account Has Been Created!":
        #     self.logger.info("Account registration is passed..")
        #     assert True
        #     self.driver.close()
        #
        # else:
        #     self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg1.png")
        #     self.logger.error("Account registration is failed.")
        #     self.driver.close()
        #     assert False

        if self.confirmationMsg == True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
            self.driver.close()
            assert False

        self.logger.info("**** test_001_AccountRegistration finished *** ")




