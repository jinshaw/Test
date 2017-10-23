from selenium import webdriver
from login import Login

class Login_test:
    def __init__(self):
         self.driver=webdriver.Chrome()
         self.driver.get("http://ecom-qa.baiwandian.cn/xinyunlian-ecom/login/dl.jhtml")

    def test_login(self,username,password):
        print(username)
        print(password)
         # username='330405110441'
         # password='1234'
        Login().user_login(self.driver,username,password)
        Login().user_logout(self.driver)

user_file=open('account.txt','r')
lines=user_file.readlines()
user_file.close()
for i in lines:
     username = i.split(',')[0]
     password = i.split(',')[1]
     Login_test().test_login(username,password)

