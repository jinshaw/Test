#-*- coding: utf-8 -*-
class Login():
#登录
    def user_login(self,driver,username,password):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//*[@id='container']/div[2]/div[2]/div[2]/div[2]/input").click()
#登出
    def user_logout(self,driver):
        driver.find_element_by_link_text("[退出]").click()
        driver.quit()