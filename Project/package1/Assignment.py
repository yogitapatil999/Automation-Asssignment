import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    driver=webdriver.Chrome(executable_path=r'c:\chromedriver')
    def testfirst(self):
        self.driver.get("https://www.calculator.net")
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[4]').click()#"*" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]').click()#number 5
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]').click()#number 5
        multi=222075
        total=self.driver.find_element_by_xpath('//*[@id="sciOutPut"]').text
        self.assertEqual(float(multi),float(total),"multiplication Failed")
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()# "AC" Button
        
    def testsecond(self):
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[4]').click()#"/" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        Div=20
        total=self.driver.find_element_by_xpath('//*[@id="sciOutPut"]').text
        self.assertEqual(float(Div),float(total),"Division Failed")
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()# "AC" Button
        
        
    def testthird(self):
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[1]/div/div[5]/span[1]').click()#"(" sign
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()#"-" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[1]/div/div[5]/span[2]').click()#")" sign
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[4]').click()#"+" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]').click()#number 5
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[2]').click()#number 5
        Add=111111
        total=self.driver.find_element_by_xpath('//*[@id="sciOutPut"]').text
        self.assertEqual(float(Add),float(total),"Addition Failed")
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()# "AC" Button
        
          
    def testfourth(self):
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[2]').click()#number 8
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()#"-" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[1]/div/div[5]/span[1]').click()#"(" sign
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[4]').click()#"-" operator
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[4]/span[1]').click()#number 0
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[3]').click()#number 9
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[2]/span[1]').click()#number 4
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[1]/span[2]').click()#number 8
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[2]').click()#number 2
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[3]/span[3]').click()#number 3
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[1]/div/div[5]/span[2]').click()#")" sign
        sub=23329646
        total=self.driver.find_element_by_xpath('//*[@id="sciOutPut"]').text
        self.assertEqual(float(sub),float(total),"Substraction failed")
        self.driver.find_element_by_xpath('//*[@id="sciout"]/tbody/tr[2]/td[2]/div/div[5]/span[3]').click()# "AC" Button
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()