import configparser

config = configparser.RawConfigParser()
# config.read("..\\Configuration\\config")        # D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest_Nopcommerce\\Configuration\\config
config.read("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest_Nopcommerce\\Configuration\\config")        # D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest_Nopcommerce\\Configuration\\config


class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password
