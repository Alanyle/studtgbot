from bs4 import BeautifulSoup as BS # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings()

def parse(data):
    if data !="sport":
        page = requests.get('https://ria.ru/'+data, verify=False)
    else:
        page = requests.get('https://rsport.ria.ru/', verify=False)
        tl = "Спорт"
    print(page.status_code) # смотрим ответ сайта
    soup = BS(page.text, "html.parser") # передаем страницу в bs4
    tl = soup.findAll('div', class_="tag-input")
    tl2 = soup.findAll('div', class_="page__media-title")
    tx = soup.findAll('div', class_="list-item__content")
    tx0 = soup.findAll('div', class_="cell-main-photo__desc")
    tx2 = soup.findAll('div', class_="cell-list__list")
    ttl = ' '
    txt = ' '
    txt2 = ' '
    list =[]
    if (len(tl) or len(tl2)):
        if (len(tl2)): #title
            tl=tl2
        for data in tl:  # проходим циклом по содержимому контейнера
            if data.find('a'):  # находим тег <p>
                ttl = ' '.join(data.text.split())  # записываем в переменную содержание тега
            if ttl != ' ':
                print(ttl)
            else:
                print("no title")

    if (len(tx0)):
        for data in tx0: # проходим циклом по содержимому контейнера
            inner_divs = data.find_all('div')
            if data.find('div'): # находим тег <p>
                if len(inner_divs) >= 2:
                    news_text = inner_divs[1].text.strip()  # Второй div содержит текст новости
                    if news_text != ' ':
                        print(news_text)
                        list.append(news_text)
                    else:
                        print("no text 0")
    if (len(tx2)):
        for data in tx2: # проходим циклом по содержимому контейнера
            inner_divs = data.find_all('span')
            if data.find('span'): # находим тег <p>
                if len(inner_divs) >= 2:
                    news_text = inner_divs[0].text.strip()  # Второй div содержит текст новости
                    if news_text != ' ':
                        print(news_text)
                        list.append(news_text)
                    else:
                        print("no text 2")
    if (len(tx)):
        for data in tx: # проходим циклом по содержимому контейнера
            if data.find('a'): # находим тег <p>
                txt = ' '.join(data.text.split()) # записываем в переменную содержание тега
            if txt != ' ':
                print(txt)
                list.append(txt)
    else:
        print("no text")
    return ttl + "\n" + '\n'.join(list)
if __name__ == '__main__':
    parse('culture')
#politics t x
#world t x
#economy
#society
#incidents
#defense_safety
#science
#https://rsport.ria.ru/
#culture
#religion t2 x x0
#tourism t2 x2