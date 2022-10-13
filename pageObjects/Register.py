from selenium.webdriver.common.by import By
class AccountRegisteration():
    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_password_name="password"
    chk_policy_name="agree"
    button_continue_xpath="//button[normalize-space()='Continue']"
    txt_confirmmsg_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self,driver):
        self.driver=driver

    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME, self.txt_email_name).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(pwd)


    def clickPrivacyPolicy(self):
        self.chk_privacypolicy=self.driver.find_element(By.NAME,self.chk_policy_name)
        self.driver.execute_script("arguments[0].click();", self.chk_privacypolicy)

    def clickContinue(self):
        self.button_submit=self.driver.find_element(By.XPATH,self.button_continue_xpath)
        self.driver.execute_script("arguments[0].click();", self.button_submit)


    def getConfirmationMsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.txt_confirmmsg_xpath).is_dispalyed()
        except:
            return False





