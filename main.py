#Import Selenium
from selenium import webdriver
import pandas as pd
import time

#Writing our First Selenium Python Test
web = 'https://1xstavka.ru/en/line/Football/1841614-UEFA-European-Championship-2020/' #you can choose any other league (update 1)
driver = webdriver.Chrome()
driver.get(web)

#Make ChromeDriver click a button
time.sleep(5) #add implicit wait, if necessary

#Initialize your storage
teams = []
x12 = [] #3-way
odds_events = []


#Looking for 'sports titles'
sport_title = driver.find_elements_by_class_name('c-events__item')

for sport in sport_title:
    # selecting only football
    parent = sport.find_element_by_xpath('./..') #immediate parent node
    grandparent = parent.find_element_by_xpath('./..')
    #Looking for single row events
    single_row_events = grandparent.find_elements_by_class_name('c-events__item c-events__item_col')

    #Getting data
    for match in single_row_events:
        #'odd_events'
        odds_event = match.find_elements_by_class_name('c-bets')

        odds_events.append(odds_event)
        # Team names
        for team in match.find_elements_by_class_name('c-events__name'):
            teams.append(team.text)

    #Getting data: the odds
    for odds_event in odds_events:
        for n, box in enumerate(odds_event):
            rows = box.find_elements_by_xpath('.//*')
            if n == 0:
                x12.append(rows[0].text)
print(parent)
driver.quit()
#Storing lists within dictionary
dict_gambling = {'Teams': teams, '1x2': x12}
#Presenting data in dataframe
df_gambling = pd.DataFrame.from_dict(dict_gambling)
print(df_gambling)

