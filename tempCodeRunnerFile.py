import pyautogui
import webbrowser
from selenium import webdriver
import pyperclip 
import datetime
import time as pytime

pyautogui.PAUSE = 2.5
#pyautogui.hotkey('ctrl','t')
#pyautogui.press("windows")
url = 'https://portalrm.montreal.com.br/Corpore.Net/Login.aspx'
#chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
#webbrowser.get('chrome').open_new(url)
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('//*[@id="txtUser"]').send_keys('97021456')
driver.find_element_by_xpath('//*[@id="txtPass"]').send_keys('J3@nbsp1')
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
driver.find_element_by_xpath('//*[@id="ctl18_REC_PtoEspCartaoActionWeb_LinkControl"]').click()
now = datetime.datetime.now()
data=now.strftime('%d%m%Y')

intdate = driver.find_element_by_xpath('//*[@id="ctl26_dpInicioPerMes_txtDate"]')
intdate.clear()
intdate.send_keys(data)
pytime.sleep(5)
findate = driver.find_element_by_xpath('//*[@id="ctl26_dpFimPerMes_txtDate"]')
findate.clear()
findate.send_keys(data)

driver.find_element_by_xpath('//*[@id="ctl26_btnAtualizar_tblabel"]').click()

driver.find_element_by_xpath('//*[@id="ctl26_gridEspelhoCartao_gridEspelhoCartao_ctl02_ctl26_gridEspelhoCartao_gridEspelhoCartao:RMWSelectTemplate"]').click()

driver.find_element_by_xpath('//*[@id="ctl26_ctl01_ctl21"]').click()
pytime.sleep(2)
driver.find_element_by_xpath('//*[@id="ctl26_ctl01_ctl09"]/tbody/tr/td[2]/span').click()