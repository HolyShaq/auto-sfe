# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

username = ''
password = ''

def findElement(by, value):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))
    return driver.find_element(by, value)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://web2.plm.edu.ph/sfe/')

time.sleep(1)

usernameInput = findElement(By.NAME, 'username')
passwordInput = findElement(By.NAME, 'password')
loginButton = findElement(By.NAME, 'login')

usernameInput.send_keys(username)
passwordInput.send_keys(password)
loginButton.click()

while True:
    subjectsDropdown = findElement(By.NAME, 'subjCodes')
    subjectsDropdown.click()

    options = subjectsDropdown.find_elements(By.TAG_NAME, 'option')
    evaluateButton = findElement(By.ID, 'evaluateBtn')

    for option in options:
        if option.get_attribute('disabled') is None:
            option.click()
            evaluateButton.click()
            break
    else:
        print('No more subjects to evaluate.')
        break

    time.sleep(0.5)

    # First seven pages
    for i in range(7):
        radios = [findElement(By.ID, f'choice[1+{i}]') for i in range(i*6, i*6+6)]
        nextButton = findElement(By.NAME, 'next')
        for radio in radios:
            radio.find_element(By.XPATH, "./..").click()
        nextButton.click()
        time.sleep(0.5)

    # Page 8
    radios = [findElement(By.ID, f'choice[0+{i}]') for i in range(42, 47)]
    inputBox = findElement(By.ID, 'textboxx')
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    inputBox.send_keys('None')
    nextButton.click()
    time.sleep(0.5)

    # Page 9
    radios = [findElement(By.ID, f'choice[0+{i}]') for i in [48, 49, 51]]
    inputBoxFair = findElement(By.NAME, 'choice[50]')
    inputBoxStrength = findElement(By.NAME, 'choice[52]')
    inputBoxSync = findElement(By.NAME, 'choice[53]')
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    inputBoxFair.send_keys('Yes')
    inputBoxStrength.send_keys('Considerate. None.')
    inputBoxSync.send_keys('Yes')
    nextButton.click()
    time.sleep(0.5)

    # Page 10
    inputBoxAsync = findElement(By.NAME, 'choice[54]')
    inputBoxContingency = findElement(By.NAME, 'choice[55]')
    nextButton = findElement(By.NAME, 'next')
    inputBoxAsync.send_keys('Yes')
    inputBoxContingency.send_keys('No technical problems were encountered.')
    nextButton.click()
    time.sleep(0.5)

    # Page 11
    radios = [findElement(By.ID, f'choice[1+{i}]') for i in range(56, 62)]
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    nextButton.click()
    time.sleep(0.5)

    # Page 12
    radios = [findElement(By.ID, f'choice[1+{i}]') for i in [ 62, 63, 64, 67 ]]
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    nextButton.click()
    time.sleep(0.5)

    # Page 13
    radios = [findElement(By.ID, f'choice[1+{i}]') for i in [68, 69]]
    inputBoxObjectives = findElement(By.NAME, 'choice[70]')
    inputBoxImprove = findElement(By.NAME, 'choice[71]')
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    inputBoxObjectives.send_keys('None')
    inputBoxImprove.send_keys('None')
    nextButton.click()
    time.sleep(0.5)

    # Page 14
    radios = [findElement(By.ID, f'choice[1+{i}]') for i in range(72, 78)]
    nextButton = findElement(By.NAME, 'next')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    nextButton.click()
    time.sleep(0.5)

    # Page 15
    radios = [findElement(By.ID, f'choice[1+{i}]') for i in range(78, 81)]
    inputBoxVirtual = findElement(By.NAME, 'choice[81]')
    finishButton = findElement(By.NAME, 'submiteval')
    for radio in radios:
        radio.find_element(By.XPATH, "./..").click()
    inputBoxVirtual.send_keys('Good')
    finishButton.click()
    time.sleep(0.5)

