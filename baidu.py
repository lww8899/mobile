#!/usr/bin/env python
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re
import HTMLTestRunner

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url="http://www.baidu.com/"
        self.vertificationErrors=[]
        self.accept_next_alert=True

    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def test_baidu_set(self):
        driver=self.driver
        driver.get(self.base_url+"/gaoji/preference.html")
        m=driver.find_element_by_name("NR")
        m.find_element_by_xpath("/html/body/form[1]/table/tbody/tr[3]/td[2]/select/option[4]").click()
        time.sleep(4)

        driver.find_element_by_xpath("//input[@value='保存设置']").click()
        time.sleep(3)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.vertificationErrors)
if __name__=="__main__":
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    testunit.addTest(Baidu("test_baidu_set"))

    filename="E:\\abc\\report\\result.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"百度搜索测试报告",
        description=u"用例执行情况："
    )
    runner.run(testunit)
fix add