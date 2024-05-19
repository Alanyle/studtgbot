from bs4 import BeautifulSoup as BS # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import urllib3
urllib3.disable_warnings()

def parse(data):
    try:
        if data.lower() !="sport":
            page = requests.get('https://ria.ru/'+data.lower(), verify=False)
        else:
            page = requests.get('https://rsport.ria.ru/', verify=False)
            tl = "Спорт"
        print(page.status_code) # смотрим ответ сайта
        soup = BS(page.text, "html.parser") # передаем страницу в bs4
        title0 = soup.findAll('div', class_="tag-input")
        title2 = soup.findAll('div', class_="page__media-title")
        text = soup.findAll('div', class_="list-item__content")
        text0 = soup.findAll('div', class_="cell-main-photo__desc")
        text2 = soup.findAll('div', class_="cell-list__list")
        title = ' '
        txt = ' '
        list =[]
        if (len(title0) or len(title2)):
            if (len(title2)): #title
                title0=title2
            for data in title0:  # проходим циклом по содержимому контейнера
                if data.find('a'):  # находим тег <p>
                    title = ' '.join(data.text.split())  # записываем в переменную содержание тега
                if title != ' ':
                    print(title)
                else:
                    print("no title")

        if (len(text0)):
            for data in text0: # проходим циклом по содержимому контейнера
                inner_divs = data.find_all('div')
                if data.find('div'): # находим тег <p>
                    if len(inner_divs) >= 2:
                        news_text = inner_divs[1].text.strip()  # Второй div содержит текст новости
                        if news_text != ' ':
                            print(news_text)
                            list.append(news_text)
                        else:
                            print("no text 0")
        if (len(text2)):
            for data in text2: # проходим циклом по содержимому контейнера
                inner_divs = data.find_all('span')
                if data.find('span'): # находим тег <p>
                    if len(inner_divs) >= 2:
                        news_text = inner_divs[0].text.strip()  # Первый div содержит текст новости
                        if news_text != ' ':
                            print(news_text)
                            list.append(news_text)
                        else:
                            print("no text 2")
        if (len(text)):
            for data in text: # проходим циклом по содержимому контейнера
                if data.find('a'): # находим тег <p>
                    txt = ' '.join(data.text.split()) # записываем в переменную содержание тега
                if txt != ' ':
                    print(txt)
                    list.append(txt)
        else:
            print("no text")
        print(len(list))
        return title + "\n\n" + '\n'.join(list[:15])
    except:
        print("Wrong categ")
        return "Неправильная категория"
if __name__ == '__main__':
    print(parse("economy"))
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