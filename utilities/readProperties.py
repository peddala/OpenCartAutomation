import configparser
import  os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configerations\\config.ini")  ##to read the data from congig.ini file

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get("commonInfo","baseURL")
        return  url

    @staticmethod
    def getUseremail():
        email=config.get("commonInfo","email")
        return email

    @staticmethod##with out creating object we can directly call this function using the class
    def getPassword():
        password=config.get("commonInfo","password")
        return  password