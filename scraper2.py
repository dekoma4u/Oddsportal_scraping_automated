from selenium import webdriver
import time
import matplotlib.pyplot as plt
import pandas as pd
import csv

#Chromedriver path
driver = webdriver.Chrome(executable_path="/Users/ugooezekoma/Documents/chromedriver")
driver.get('https://www.oddsportal.com/esports/europe/counter-strike-esl-pro-league-season-13/results/#/page/2/')
time.sleep(1)
driver.find_element('xpath', '//*[@id="onetrust-accept-btn-handler"]').click()
print("cookies checked out already")
time.sleep(1)
for amen in range(1,50):
    try:
        driver.find_element('xpath', '//*[@id="tournamentTable"]/tbody/tr['+str(amen)+']/td[2]/a').is_enabled()
        print("Item found. Scraping starts now ...")
        print("Add the name of the game to a txt file")

        def clicker(title):
            with open("games/game_list2.txt", "a") as text_file:
                already = text_file.write(title + ",")
            return already
        clicker(driver.find_element('xpath', '//*[@id="tournamentTable"]/tbody/tr['+str(amen)+']/td[2]/a').text)

        driver.find_element('xpath', '//*[@id="tournamentTable"]/tbody/tr['+str(amen)+']/td[2]/a').click()

        def teamResult(result):
            with open("games/game_list2.txt", "a") as text_file:
                team = text_file.write(result + '\n')
            return team
        teamResult(driver.find_element('xpath', '//*[@id="event-status"]/p').text)
        print("The match name and final result are added to the text file.")

        def fi(a):
            try:
                driver.find_element('xpath', a).text
            except:
                return False
        def ffi(a):
            if (fi(a) != False):
                return driver.find_element('xpath', a).text
        def ell(i, j):
            return ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']')
        def f(i, x):
            try:
                x[ell(i,1)]=[ell(i,2), ell(i,3), ell(i,4), ell(i,5)]
            except:
                print('')
        def tryc(f1, f2):
            try:
                driver.find_element('xpath', f1).click()
            except:
                print('')
            try:
                driver.find_element('xpath', f2).click()
            except:
                print('')
        #Find title
        def tryp(f1, f2):
            if (driver.find_element('xpath', f1).text != ' '):
                return driver.find_element('xpath', f2).text
        def operation(i):
            tryc('//*[@id="tournamentTable"]/tbody/tr['+str(i)+']/td[2]/a', '//*[@id="tournamentTable"]/tbody/tr['+str(i)+']/td[2]/a[2]')
            time.sleep(1)
            x = dict();
            for i in range(1, 11):
                f(i,x)
            time.sleep(1)
            driver.back()
            print("scraped finished. Output is appended to a csv file")
            with open("odds/odds2.csv", "a") as outfile:
                wait_over = csv.writer(outfile)
                wait_over.writerow(x.keys())
                bc = wait_over.writerows(zip(*x.values()))
            return bc
        print(operation(1))

    except:
        print("Unfortunately, the path is not clickable, try next ...")
        continue
# //*[@id="tournamentTable"]/tbody/tr[2]/th[1]/span
# //*[@id="tournamentTable"]/tbody/tr[7]/th[1]/span
# //*[@id="tournamentTable"]/tbody/tr[12]/th[1]/span
# //*[@id="tournamentTable"]/tbody/tr[17]/th[1]/span
