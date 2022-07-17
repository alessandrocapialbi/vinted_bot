from telnetlib import EC
from time import sleep

import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

driver = uc.Chrome(use_subprocess=True)
driver.get("https://www.vinted.com")
window_before = driver.window_handles[0]
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Italia']"))).click()
sleep(1)
driver.find_element("id", "onetrust-accept-btn-handler").click()
sleep(1)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Iscriviti | Accedi']"))).click()
sleep(1)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Accedi con Google']"))).click()
sleep(1)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
sleep(1)
driver.find_element("id", "identifierId").send_keys("capialbi.alessandro@gmail.com")
sleep(1)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Avanti']"))).click()
sleep(1)
wait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys("3DPM&^DMO3S0b*oCpSvVdppOm")
sleep(0.5)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Avanti']"))).click()
sleep(1)
driver.switch_to.window(window_before)
sleep(1)
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@title='Gonna Jeans, prezzo: 8,95 €, brand: Vintage, taglia: S / IT 40 / EU 36']").click()))
sleep(5)
'''
privacy = driver.find_element_by_xpath('//*[@id="info_privacy"]')
driver.execute_script("arguments[0].click();", privacy)
cookies = driver.find_element_by_xpath('//*[@id="info_easylesson"]')
driver.execute_script("arguments[0].click();", cookies)
driver.find_element_by_xpath('//*[@id="oauth_btn"]').click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys("7047037")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("F%zrKNU0&ahU!sJ#e44l")
driver.find_element_by_xpath('/html/body/div/div/div/div[1]/form/div[5]/button').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[4]/div/div[2]/div[1]/div/div[6]/div/div[2]/div[1]/a').click()
driver.find_element_by_xpath('/html/body/div[4]/div[4]/div[6]/div[1]/div[2]/div/div[1]/a').click()
driver.find_element_by_xpath('//*[@id="973490"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="973502"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="973537"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="973467"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('//*[@id="973491"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[3]/button').click()'''




