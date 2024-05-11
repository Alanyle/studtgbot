from bs4 import BeautifulSoup as BS # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings()

def parse(data):
    page = requests.get('https://pogoda.mail.ru/prognoz/'+data, verify=False)
    print(page.status_code) # смотрим ответ сайта
    soup = BS(page.text, "html.parser") # передаем страницу в bs4
    bdate = soup.findAll('div', class_="information__header__left")
    btemp = soup.findAll('div', class_="information__content__additional information__content__additional_temperature")
    desc = ' '
    temp = ' '
    if (len(bdate)):
        for data in bdate:  # проходим циклом по содержимому контейнера
            if data.find('div'):  # находим тег <p>
                desc = ' '.join(data.text.split())  # записываем в переменную содержание тега
            if desc != ' ':
                print(desc)
    else:
        print("no date")
    if (len(btemp)):
        for data in btemp: # проходим циклом по содержимому контейнера
            if data.find('span'): # находим тег <p>
                temp = ' '.join(data.text.split()) # записываем в переменную содержание тега
            if temp != ' ':
                print(temp)
    else:
        print("no temperature")
    return desc + "\n" + temp
if __name__ == '__main__':
    parse()