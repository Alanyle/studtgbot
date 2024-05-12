from bs4 import BeautifulSoup as BS # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings()
import random

def parse():
    try:
        page = requests.get('https://anekdoty.ru/pro-programmistov/', verify=False)
        print(page.status_code) # смотрим ответ сайта
        soup = BS(page.text, "html.parser") # передаем страницу в bs4
        tl = soup.findAll('div', class_="description content-blocks")
        tx = soup.findAll('div', class_="holder")
        ttl = ' '
        anek = ' '
        list =[]
        if (len(tl)):
            for data in tl:  # проходим циклом по содержимому контейнера
                if data.find('h1'):  # находим тег <p>
                    ttl = ' '.join(data.text.split())  # записываем в переменную содержание тега
                if ttl != ' ':
                    print("title " + ttl)
                else:
                    print("no ttl")
        else:
            print("no title")
        if (len(tx)):
            for data in tx: # проходим циклом по содержимому контейнера
                inner_divs = data.find_all('p')
                if data.find('div'): # находим тег <p>
                    if len(inner_divs):
                        anek = inner_divs[0].text.strip()
                        if anek != ' ':
                            print("anek " + anek)
                            list.append(anek)
                        else:
                            print("no anek")
        else:
            print("no text")
        return ttl + "\n" + random.choice(list[:15])
    except:
        print("Wrong")
        return "Ошибка"
if __name__ == '__main__':
    parse()