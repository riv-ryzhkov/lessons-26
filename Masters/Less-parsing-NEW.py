# pip install bs4
# https://beautiful-soup-4.readthedocs.io/en/latest/


############ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import requests
# import bs4
from bs4 import BeautifulSoup as BS
import csv
import time

#
# ################################################

# import requests
# from bs4 import BeautifulSoup

#
# url = 'https://books.toscrape.com/'
# response = requests.get(url)
#
# # print(response.text)
# # print(type(response.text))
#
# soup = BS(response.text, 'html.parser')
# print(type(soup))
# print(soup)


# print(*dir(soup), sep='\n')



# ##################### start info #############

# url = 'https://books.toscrape.com/'
# response = requests.get(url)
# soup = BS(response.text, 'html.parser')

# print(soup)
# print(soup.prettify())  # tags <div>
# print(type(soup.prettify()))  # tags <div>
# print(soup.head)  # tags <div>
# print(soup.head.title)  # tags <div>
# print(soup.head.title.text)  # tags <div>
# print(soup.div)  # tags <div>
# print(soup.img)  # tags <div>
# print(url+soup.img['src'])  # tags <div>



# element = soup.div.div.div.a.prettify()
# element = soup.div.a
# print(type(element))    # tags <div>
# print(element)  # tags <div>
#
# print(url+element['href'])

#
#
# print(soup.div.a)     # tags <div><a>    </a></div>
# #
# print(soup.find('div').find('a'))   # tags <div><a>    </a></div>
#
#
#
# print(soup.find('head').prettify())   # tag <head>
#
#


# print(soup.find_all('div'))

# pr1 = soup.find_all('div')
# print(type(pr1))
# print(*dir(pr1), sep='\n')
# print(isinstance(pr1, list))

# print(*soup.find_all('div'), sep='\n=====================================================\n')





# for el in soup.find_all('div'):
#     try:
#         if el.a['href'].startswith('http'):
#             print(el.a['href'])
#         else:
#             print(url + el.a['href'])
#     except:
#         print('NO href!')








# print(soup.li)  # tags <h4>
#
#
# tag = soup.li
# tag = soup.li.text
# tag1 = url + soup.li.a['href']
# print(soup.li)
# print(tag)
# print(tag1)
# print(type(tag))




# tag = soup.body
# print(*dir(tag), sep='\n')
# print(tag)
#
#
#
#
#
# print(soup.head.link)
# print(url + soup.head.link['href'])
# print(soup.head.link['rel'])




# print(soup)
# print(soup.text)
# print(type(soup))
# print(type(soup.text))
# print('.'*80)
#

# for i in range(100):
#     soup_text = soup.text.replace('\n\n', '')
#     soup_text = soup_text.replace('  ', ' ')
#     soup_text = soup_text.replace('  ', ' ')
#     soup_text = soup_text.replace('  ', ' ')
# # print(soup_text)
# soup_text = soup_text.replace('\n', '').strip()
# print(soup_text)
# ...................................



# print(soup.find_all('link'))
# print(type(soup.find_all('link')))
#
#
# print(*dir(soup.find_all('link')), sep='\n')  # close to list!!!!!






# print(*soup.find_all('link'), sep='\n')


# for el in soup.find_all('link'):
#     # print(el['href'])
#     if el['href'].startswith('static'):
#         print(url+el['href'])
#     else:
#         print(el['href'])



# .........................

# print(*soup.find_all(['p']), sep='\n')
# print(*soup.find_all(['a', 'h4', 'img']), sep='\n\n')




# res = soup.find_all(['p', 'a'], limit=5)
# for el in range(len(res)):
#     print()
#     print(el+1, ':')
#     print(res[el])
#     print('.'*60)



# ......................................................
#

######################################################################

# url = 'https://books.toscrape.com/'
#
# for page in range(1, 50):
#     print('%'*80)
#     print('Page Number :', page)
#     url1 = f'https://books.toscrape.com/catalogue/page-{page}.html'
#     response = requests.get(url1)
#     soup = BS(response.text, 'html.parser')
#
#     soup = soup.find('ol', class_='row')
#     # print(soup.prettify())
#     soup = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
#     # print(soup[0].prettify())
#     # soup = soup[0]
#
#     for soup_ in soup:
#         my_ref = url + soup_.article.div.a['href']
#         print(my_ref)
#         my_img = url + soup_.article.div.img['src']
#         print(my_img)
#         my_text = soup_.article.h3.a['title']
#         print(my_text)
#         my_price = soup_.article.find("div", class_="product_price").p.text[1:]
#         my_price1 = float(soup_.article.find("div", class_="product_price").p.text[2:]) * 1.05
#         print(my_price)
#         print(my_price1)
#         print('='*60)

#########################################

######################################################################

# url = 'https://books.toscrape.com/'
# response = requests.get(url)
# soup = BS(response.text, 'html.parser')

# books = soup.find('article', class_='product_pod').prettify()
# print(books)



# books = soup.find_all('article', class_='product_pod')
# for i in books:
#     print(i.find('h3').text)
#     print(i.find('h3').a['title'])
#     print(url + i.a['href'])
#     print(url + i.a.img.get('src'))
#     print('='*80)



#
# l1 = soup.find_all(id=True)
# print(type(l1), *l1, sep='\n===========================================')
#
# for el in l1:
#     print("id=", el['id'])







#
# .......................................................

# print(soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")[0].prettify())







################ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import requests
# from bs4 import BeautifulSoup as BS
# import csv
# import time
#
#
#
#
# # базова адреса сайту
# BASE_URL = 'https://books.toscrape.com/'
#
#
# def get_soup(url):
#     """
#     Отримання HTML-коду сторінки
#     та створення об'єкта BeautifulSoup
#     """
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0'
#     }
#
#     response = requests.get(url, headers=headers)
#
#     # перевірка успішності запиту
#     if response.status_code != 200:
#         print(f'Помилка: {response.status_code}')
#         return None
#
#     # створення BeautifulSoup
#     return BS(response.text, 'html.parser')
#
#
# def parse_page(page):
#     """
#     Парсинг однієї сторінки
#     """
#
#     # формування адреси сторінки
#     url = f'https://books.toscrape.com/catalogue/page-{page}.html'
#
#     print(f'\n{"=" * 25}')
#     print(f'СТОРІНКА {page}')
#     print(f'{"=" * 25}')
#
#     soup = get_soup(url)
#
#     # якщо сторінка не отримана
#     if soup is None:
#         return []
#
#     # пошук усіх карток книг
#     books = soup.find_all('article', class_='product_pod')
#
#     result = []
#
#     # перебір знайдених книг
#     for num, book in enumerate(books, start=1):
#
#         # назва книги
#         title = book.h3.a['title']
#
#         # ціна
#         price = float(book.find('p', class_='price_color').text[2:])
#
#         # рейтинг
#         rating = book.p['class'][1]
#
#         # посилання на книгу
#         link = BASE_URL + 'catalogue/' + book.h3.a['href']
#
#         # посилання на зображення
#         image = BASE_URL + book.img['src'].replace('../', '')
#
#         # виведення інформації
#         print(f'{num}. {title}')
#         print(f'Ціна: {chr(163)}{price}')
#         print(f'Нова(моя) Ціна: {chr(163)}{price*1.05}')
#         print(f'Рейтинг: {rating}')
#         print(f'Посилання: {link}')
#         print(f'Зображення: {image}')
#         print('-' * 60)
#
#         # додавання даних у список
#         result.append({
#             'title': title,
#             'price': price,
#             # 'price': str(price).replace('.', ','),
#             'rating': rating,
#             'link': link,
#             'image': image
#         })
#
#     return result
#
#
# def save_to_csv(data, filename='books.csv'):
#     """
#     Збереження даних у CSV-файл
#     """
#
#     with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
#
#         writer = csv.DictWriter(
#             file,
#             fieldnames=['title', 'price', 'rating', 'link', 'image'],
#             delimiter = ';'
#         )
#
#         # запис заголовків
#         writer.writeheader()
#
#         # запис рядків
#         writer.writerows(data)
#
#     print(f'\nДані збережено у файл: {filename}')
#
#
# # список для всіх книг
# all_books = []
#
# # парсинг перших 3 сторінок
# for page in range(1, 4):
#
#     books = parse_page(page)
#
#     # додавання книг до загального списку
#     all_books.extend(books)
#
#     # пауза між запитами
#     time.sleep(1)
#
# # збереження результатів
# save_to_csv(all_books)


################ \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\






##########################################

# ###################################################################################
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BS(response.text, 'html.parser')
#
# quotes = soup.find_all('span', class_='text')
# # print(quotes)
# for n, el in enumerate(quotes, start=1):
#     print(n, ':', el.text)
#
# authors = soup.find_all('small', class_='author')
# for n, el in enumerate(authors, start=1):
#     print(n, ':', el.text)
# #
# #
# tags = soup.find_all('div', class_='tags')
# for n, el in enumerate(tags, start=1):
#     # print(n, ':', el)
#     print(n, ':')
#     tags = el.find_all('a')
#     for i in tags:
#         print(i.text, end=' ')
#     print()
#     print('-'*80)
#
# ############# PAGES ####################

# for i in range(1, 10):
#     print('-'*80)
#     print('Page #:', i)
#
#     url = f'https://quotes.toscrape.com/page/{i}/'
#     response = requests.get(url)
#
#     soup = BS(response.text, 'html.parser')
#
#     quotes = soup.find_all('span', class_='text')
#     authors = soup.find_all('small', class_='author')
#     tags = soup.find_all('div', class_='tags')
#     print('=' * 80)
#     for i in range(len(quotes)):
#         print(quotes[i].text)
#         print('Author: \t' + authors[i].text)
#         tags_for_quote = tags[i].find_all('a', class_='tag')
#         print('tags:  \t\t#', end='')
#         for tag in tags_for_quote:
#             print(tag.text, end=' #')
#         print()
#         print('=' * 80)
#


############################################################################
################ BBC.COM    #####################################
############################################################################

# url = 'https://www.bbc.com/ukrainian/'
#
# response = requests.get(url)
# print(response.status_code)
#
# soup = BS(response.text, "html.parser")
#
# # print(soup)
#
# # soup = soup.find('section', attrs={'role': 'region'})
# # soup = soup.find('section', attrs={'aria-labelledby': 'high-collection-1'})
# # soup = soup.find('section', attrs={'aria-labelledby': 'low-feed-3'})
# soup = soup.find('section', attrs={'aria-labelledby': 'low-feed-2'})
# # print(soup)
#
# allNews = soup.find_all('li')
# # print('allNews :', allNews)
# # print(len(allNews))
#
#
# # soup1 = allNews[0]
# # print(allNews[0].prettify())
# #
# for soup1 in allNews:
#     my_image = soup1.img['src']
#     my_title = soup1.find('div', class_='promo-text').a.text
#     my_text = soup1.find('div', class_='promo-text').p.text if soup1.find('div', class_='promo-text').p else None
#
#     my_time = soup1.find('div', class_='promo-text').time['datetime']
#     my_time = my_time + '  ' + soup1.find('div', class_='promo-text').time.text
#
#     my_ref = soup1.find('div', class_='promo-text').a['href']
#     print('\n', '='*80)
#     print('Title     :', my_title)
#     print('Text      :', my_text)
#     print('Reference :', my_ref)
#     print('Photo     :', my_image)
#     print('Time      :', my_time)
#
#     # my_url = my_ref
#     # my_response = requests.get(my_url)
#     # print(my_response.status_code)
#     # new_soup = BS(my_response.text, "html.parser")
#     # new_text = new_soup.find('main').text
#     # print('All information:', new_text)
#
#
#
# print('*'*80)
#
#
#
# # for el in allNews:
# #     # img = el.img['src']
# #     img = el.find('img')['src']
# #     # title = el.a.text
# #     title = el.find('a').text
# #     time = el.time['datetime'] + '>>' + el.time.text
# #     # time = el.time.text
# #     text = el.p.text
# #     link = el.a['href']
# #     print('time :', time)
# #     # print('.' * 80)
# #     print('title :', title)
# #     # print('.' * 80)
# #     print('short text :', text)
# #     # print('.' * 80)
# #     print('picture :', img)
# #     # print('.' * 80)
# #     print('link :', link)
# #     print('=' * 80)

################################################################################
#### NEWS ######################################################################
###############################################################################


###################    http://mignews.com   ##########################
#
# url = 'http://mignews.com/'
#
# page = requests.get(url)
# print(page.status_code)
#
# filteredNews = {}
#
# soup = BS(page.text, "html.parser")
#
# # allNews = soup.find_all('div', class_="'article-news'")
# # allNews = soup.find_all('div', class_="col-md-6 mt-2 lenta-min")
# allNews = soup.find_all('article', class_="post mb-2")
#
# print(allNews)
# # breakpoint()
# for data in allNews:
#     ref = url + data.a['href']
#     time = data.a.div.text
#     text = data.find('div', class_='text-color-dark').a.text
#     print('Час публікації :', time)
#     print('Повідомлення :', text)
#     print('Посилання :', ref)
#     print('='*80)

#
#
#
#
# print(allNews[2].prettify())
# for data in allNews:
#     filteredNews[data.text.strip()] = data.a['href']
# print('=' * 80)
# for key, vol in filteredNews.items():
#     print(key)
#     if vol.startswith('/'):
#         print('http://mignews.com/mobile'+vol)
#     else:
#         print(vol)
#     print('=' * 80)


###################    www.pravda.com.ua   ##########################

# url = 'https://www.pravda.com.ua/'
#
# page = requests.get(url)
# print(page.status_code)
#
# filteredNews = {}
#
# soup = BS(page.text, "html.parser")
#
# allNews = soup.findAll('div', class_="article_topic_news")
# # allNews = soup.findAll('div', class_="article_news")
# # allNews = soup.findAll('div', class_="article_title")
# # print(allNews[2].prettify())
#
#
# #     1st  way
# #====================================
# for data in allNews:
#     print(data.a.text.strip())
#     print(url + data.a['href'] if data.a['href'].startswith('/') else data.a['href'])
#     print('='*60)
# print('*'*80)




#     2nd  way
#====================================

# filteredNews = {}
#
# for data in allNews:
#     filteredNews[data.a.text.strip()] = data.a['href']
# print('=' * 80)
#
# # print(filteredNews)
# # breakpoint()
#
# for key, vol in filteredNews.items():
#     print(key)
#     print(url + vol if vol.startswith('/') else vol)
#     print('=' * 80)





#################################################
############### SPORT.UA ########################
#################################################

# url ='https://sport.ua/uk'
#
# response = requests.get(url)
# print(response.status_code)
#
# soup = BS(response.text, "html.parser")
#
# # soup = soup.find(id="newsline")
# # soup = soup.find(id="most_popular_news")
# soup = soup.find(id="gambling_news")
# # print(soup)
#
# all_news = soup.find_all("div", class_="item")
# # print(all_news)
# for el in all_news:
#     # el = all_news[3]
#     sport = el.span.text
#     print(sport)
#     time = el.find("span", class_="item-date").text
#     print(time)
#     text = el.a.text.strip()
#     print(text)
#     ref = el.a["href"]
#     print(ref)
#     print('='*80)






#################################################

# url ='https://sport.ua/uk'
#
# response = requests.get(url)
# print(response.status_code)
#
# soup = BS(response.text, "html.parser")
#
# # soup = soup.find(id='most_popular_news')
# soup = soup.find_all(id='popular')
# soup = soup[1]
# # soup = soup.find(id='blogs')
# # print(soup.prettify())
# news_list = soup.findAll('div', class_="item")
# # # print(news_list[2].prettify())
# # # breakpoint()
# for el in news_list:
#     news = el.find('div', class_="item-row")
# #     # print(news.prettify())
# #     # breakpoint()
#     print('='*80)
#     print('sport      :', news.span.text)
#     print('time       :', news.find('span', class_='item-date').text.strip())
#     news = el.find('div', class_="item-title item-title--b")
#     # print(news.prettify())
#     # breakpoint()
# #     # print(news.img['alt'])
#     print('Title      :', news.a.text)
#     print('img        :', news.img['data-src'])
#     print('referanse  :', news.a['href'])
#     # print('='*80)


###################################################################
############# SPORT.UA (розширений)   ############

# def get_content(url, table_name):
# # def get_content(url):
#     res = []
#     page = requests.get(url)
#     print(page.status_code)
#     soup = BS(page.text, "html.parser")
#     news_line = soup.find(id='newsline')
#     # news_line = soup.find(id='most_popular_news')
#     allNews = news_line.findAll('div', 'item')
#     # allNews = news_line.findAll('div', 'item-row')
#
#     fav = input('Input your favorite sport in Ukrainian or "всі": ')
#
#     for data in allNews:
#         time_pub = data.find('span', attrs={'class': 'item-date'})
#         time_pub = time_pub.text.strip()
#
#         sport = data.find('span', attrs={'class': 'item-sport'})
#         sport = sport.text.strip()
#
#         title = data.a.text.strip()
#
#         href = data.a['href']
#
#         if fav.lower() == sport.lower() or fav.lower() == 'всі':
#             print(time_pub)
#             print(sport)
#             print(title)
#             print(href)
#             print('=' * 60)
#
#             # res.append({'sport': sport, 'title': title, 'time_pub': time_pub, 'link': href})
#             res.append({table_name[0]: sport, table_name[1]: title, table_name[2]: time_pub, table_name[3]: href})
#     return res
#
#
# def write_content(content, table_name):
# # def write_content(content):
#     # csv_title = ['sport', 'title', 'time_pub', 'link']
#     csv_title = table_name
#     # print(csv_title)
#
#     with open('sport.csv', 'w', newline='', encoding='utf-8-sig') as f:
#     # with open('sport.csv', 'w') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
# #
# #
# #
# table_name = ['my_sport', 'my_title', 'time', 'good_link']
#
# url = 'https://new.sport.ua/uk'
# # # url = 'https://new.sport.ua'
# news = get_content(url, table_name)
# # news = get_content(url)
# write_content(news, table_name)
#
# # write_content(news)



######################################################
############# LINKS    ###############################
######################################################
# import requests
# from bs4 import BeautifulSoup as BS
#
#
# url = 'https://bottlepy.org/docs/dev/'
# # url = 'https://cnn.com/'
# result = requests.get(url)
# soup = BS(result.text, features='html.parser')
#
#
# my_links = soup.find_all('a')
# # print(*my_links, sep='\n')
# for el in my_links:
#     if el.get('href') and el.get('href').startswith('http'):
#         print(el['href'])
#     elif not el.get('href'):
#         pass
#     else:
#         print(url + el['href'])



# .........................................................
#
# def get_links(url):
#     result = requests.get(url)
#     soup = BS(result.text, features='html.parser')
#
#     links = [url+element.get('href') for element in soup.find_all('a') if element.get('href') and not str(element.get('href')).startswith('http')]
#     links1 = [element.get('href') for element in soup.find_all('a') if element.get('href') and str(element.get('href')).startswith('http')]
#     return links+links1
#
#
#
# urls = [
#     # 'https://bottlepy.org/docs/dev/',
#     # 'https://sport.ua/uk/',
#     # 'https://price.ua/',
#     # 'https://bbc.com/',
#     # 'https://beautiful-soup-4.readthedocs.io/en/latest/',
#     # 'https://cnn.com/'
#     'https://www.weatheronline.co.uk'
# ]
#
#
# for url in urls:
#     print('Links in', url)
#     for num, link in enumerate(get_links(url), start=1):
#         print(num, ':', link)
#     print('='*80)
#



# ################################# olx ###################################
# def get_content(url, table_name):
#     resp = requests.get(url)
#     print(resp.status_code)
#     rows = []
#     # session = requests.session()
#     if resp.status_code == 200:
#         soup = BS(resp.text, 'html.parser')
#
#         tr_list = soup.find_all('div', attrs={'class': 'css-1sw7q4x'})
#         # print(*tr_list, sep='\n\n\n')
#         # breakpoint()
#         count = 0
#
#         for tr in tr_list:
#             count += 1
#
#             title = tr.find('h6')
#             # print(title)
#             # breakpoint()
#             title_text = title.text if title != None else 'NoTitle'
#             title_text = title_text.replace('\n', '')
#             # print('title_text :', title_text)
#             # breakpoint()
#             href = tr.a['href'] if tr.a != None else 'Noref'
#             # href = title.a['href'].replace(';promoted', '')
#             href = 'https://www.olx.ua' + href if href.startswith('/') else href
#             # print('ref: ', href)
#             # breakpoint()
#             # td_price = tr.find('td', attrs={'class': 'td-price'})
#             price_text = tr.find('p').text if tr.find('p') != None else 'договорная'
#             price_str = price_text
#             # print('price_str :', price_str, type(price_str))
#             # breakpoint()
#             price_temp = ''.join(c for c in price_str if c.isdigit())
#             # print(price_temp, type(price_temp))
#             # breakpoint()
#             if price_temp:
#                 price = int(price_temp) * 1.05
#             else:
#                 price = 'договорная'
#             # print(price, type(price))
#             # breakpoint()
#
#             # tmp = {'title': title_text, 'price_str': price_str, 'price': price, 'url': href}
#             tmp = {
#                 table_name[0]: title_text,
#                 table_name[1]: price_str,
#                 table_name[2]: price,
#                 table_name[3]: href
#             }
#             rows.append(tmp)
#         return rows
#
#
# def write_content(content, table_name):
#     csv_title = table_name
#     # csv_title = ['title', 'price_str', 'price', 'url']
#     print(csv_title)
#     with open('olx.csv', 'w', encoding='utf-8-sig') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
#
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
# # url = 'https://www.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/materinskie-platy/?page={}'
# url = 'https://m.olx.ua/elektronika/kompyutery-i-komplektuyuschie/komplektuyuschie-i-aksesuary/videokarty/?page={}'
# # url = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/?currency=UAH&page={}'
#
#
# res = []
# table_name = ['title', 'price_str', 'price', 'url']
# count = 0
# for i in range(1, 4):
#     time.sleep(2)
#     res += get_content(url.format(i), table_name)
# print('='*80)
# for i in res:
#     count += 1
#     print('Object No.', count, ':')
#     print('.'*80)
#     for key, val in i.items():
#         print(key, val, sep='\t')
#     print('=' * 80)
# write_content(res, table_name)
#
#

##########################################
########################     ТСН   ##############################
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
#
#
# def parse_tsn_main_news():
#     # Головна сторінка сайту
#     base_url = "https://tsn.ua/"
#
#     # Налаштування сесії для імітації браузера
#     # Це допомагає уникнути блокування автоматичних запитів
#     session = requests.Session()
#     session.headers.update({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
#         "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
#     })
#
#     try:
#         # Надсилаємо запит до сайту
#         response = session.get(base_url, timeout=10)
#         response.raise_for_status()  # Перевірка, чи сторінка завантажилась успішно
#
#         # Створюємо об'єкт BeautifulSoup для парсингу HTML-коду
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # На TSN головні новини зазвичай знаходяться в тегах <article>
#         articles = soup.find_all('article')
#
#         print("--- Останні новини з головної сторінки TSN.ua ---\n")
#
#         processed_titles = set()  # Для уникнення дублікатів
#         count = 0
#
#         for article in articles:
#             # Шукаємо заголовок (зазвичай у тегах h2, h3 або всередині посилання 'a')
#             title_tag = article.find(['h3', 'h2', 'a'], class_=lambda x: x and ('title' in x or 'card' in x))
#
#             if not title_tag:
#                 continue
#
#             title = title_tag.get_text(strip=True)
#
#             # Якщо заголовок порожній або вже був виведений — пропускаємо
#             if not title or title in processed_titles:
#                 continue
#
#             # Знаходимо посилання на статтю
#             link_tag = article.find('a', href=True)
#             if link_tag:
#                 # Перетворюємо відносне посилання (/ukrayina/...) на повне (https://tsn.ua/...)
#                 link = urljoin(base_url, link_tag['href'])
#             else:
#                 link = "Посилання відсутнє"
#
#             # Шукаємо час публікації (тег <time>)
#             time_tag = article.find('time')
#             time_val = time_tag.get_text(strip=True) if time_tag else "Сьогодні"
#
#             # Виводимо результат у консоль
#             print(f"🕒 {time_val} | {title}")
#             print(f"🔗 {link}")
#             print("-" * 40)
#
#             processed_titles.add(title)
#             count += 1
#
#             # Обмежимо вивід, щоб не захаращувати консоль
#             if count >= 12:
#                 break
#
#     except requests.exceptions.RequestException as e:
#         print(f"❌ Помилка при спробі отримати дані: {e}")
#     except Exception as e:
#         print(f"❌ Сталася непередбачена помилка: {e}")
#
#
# if __name__ == "__main__":
#     parse_tsn_main_news()

################################## END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###############   DZ  Домашнє завдання ################################
########################################################################


# # DZ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# # ua.korrespondent.net
#
# url = 'https://ua.korrespondent.net/'


# pip install bs4     # запустить в терминале!!!!!!!

# https://beautiful-soup-4.readthedocs.io/en/latest/

#
import requests
from bs4 import BeautifulSoup as BS











#####################################################################

#############################################################################
############## PRICE.UA ХОЛОДИЛЬНИКИ / ПЛАНШЕТЫ #############################
#
# def get_content(url, name):
#
#     resp = requests.get(url)
#     print(resp.status_code)
#     result = []
#
#     # session = requests.session()
#
#     if resp.status_code == 200:
#         page = BS(resp.text, 'html.parser')
#         product = page.find(id='fluid-grid')
#         # print(page)
#         # breakpoint()
#         # product = page.find(id='list-grid')
#         product = page.find_all('div', class_='product-list')
#
#         # print(product.prettify())
#         # breakpoint()
#         # list_products = product.find_all('div', attrs={'class': 'product-block type2 ga_container black-link-style split-4-cards is-model'})
#         # list_products = product.find_all('div', attrs={'class': 'product-block'})
#         list_products = product.find_all('div', attrs={'class': 'wrapper-product wrapper-product-alt is-model top3-exist wishlist-exist'})
#         print(*list_products[5], sep='\n')
#         breakpoint()
#         for div in list_products:
#             prod = div.find('div', attrs={'class': 'white-wrap'})
#             title = prod.a['title']
#             href = prod.a['href']
#             pic = 'https:' + prod.img['src']
#
#             price_wrap = div.find('div', attrs={'class': 'price-wrap'})
#             price_str = price_wrap.text
#             # print(price_str)
#             # breakpoint()
#
#             price = [el for el in price_str if el.isdigit()]
#             # print(price)
#             # breakpoint()
#             price = int(''.join(price)) * 1.01
#             # print(price)
#             # breakpoint()
#
#             # tmp = {'title': title, 'price_str': price_str, 'price': price, 'pic': pic, 'url': href}
#             tmp = {name[0]: title, name[1]: price_str, name[2]: price, name[3]: pic, name[4]: href}
#             result.append(tmp)
#         return result
#
#
# def write_content(content, name):
#     # csv_title = ['title', 'price_str', 'price', 'pic', 'url']
#     csv_title = name
#     # print(csv_title)
#     with open('price.csv', 'w', encoding='utf-8-sig') as f:
#     # with open('price.csv', 'w') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)
#
#
#
# url = 'https://price.ua/ua/catc52t2'
# # url = 'https://price.ua/ua/catc6399t2.html'
# # url = 'https://price.ua/ua/catc501t2/page{}.html'
# # url = 'https://price.ua/ua/catc371t2/page{}.html'
# # url = 'https://price.ua/ua/catc52t2/page{}.html'
# # url = ('https://price.ua/ua/catc52t2')
#
# # url = 'https://price.ua/ua/smartfony/ccid1t2/page{}.html'
#
# csv_title = ['My_title', 'Old_price_str', 'my_NEW_price', 'pic', 'url']
#
# print(get_content(url, csv_title))
# breakpoint()
# res = []
#
# for i in range(1, 3):
#     time.sleep(1)
#     res += get_content(url.format(i), csv_title)
# for i in res:
#     for key, val in i.items():
#         print(key, ':', val, sep='\t')
#     print('-' * 60)
#
# write_content(res, csv_title)


###################################################################
####################  MON #############################
#########################################################


# url ='https://mon.gov.ua'
#
# session = requests.session()
#
# page = requests.get(url)
# print(page.status_code)
#
# soup = BS(page.text, "html.parser")
#
# soup = soup.find(id='layout-content')
# articles = soup.find_all('div', class_='main-item_content')
# # print(articles[0])
#
# for el in articles:
#     print(el.find('div', class_='date').text)
#     print(el.a.text)
#     print(url+el.a['href'])
#     print('='*80)
#
#
# # ........................................
# # all = soup.find_all('a')
# # for n, i in enumerate(all):
# #     if i.has_attr('href') and i['href'] != '#':
# #         print('.' * 80)
# #         print(n, ':', i.text.strip().replace('\n', ''))
# #         if i['href'].startswith('http'):
# #             print(i['href'])
# #         else:
# #             print(f"{url}{i['href']}")
#

#####################################################################


# url = 'https://tsn.ua/'
# page = requests.get(url)
# print(page.status_code)
# soup = BS(page.text, "html.parser")
#
# article = soup.find_all('li', class_='l-grid__main')
# # article = soup.find_all('div', class_='l-sidebar__gap')
# # print(*article, sep='\n')
# i = 0
# for el in article:
#     # el = article[i]
#     # print('-'*50)
#     # print(el)
#     i += 1
#     print(i, ':')
#     time = el.text
#     ref = el.a['href']
#     # img = el.a.img['src']
#     print('Article :', time.replace('\n', '').strip())
#     print('Link    :', ref)
#     # print('Image   :', img)
# print('='*50)










##################################################
########### ROZETKA 403  !!!!!!!!!!! #############
##################################################

# # url = 'https://rozetka.com.ua/ua/notebooks/c80004/'
# url = 'https://rozetka.com.ua/'
# resp = requests.get(url)
# print(resp.status_code, url)
#
# # def parsing(url, name):
# # # # def parsing(url):
# #     resp = requests.get(url)
# #     print(resp.status_code, url)
# #     # breakpoint()
# #     rows = []
# #     if resp.status_code == 200:
# #         page = BS(resp.text, 'html.parser')
# #         # print(page)
# #         # breakpoint()
# #         table = page.find_all('li', class_='catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted')
# #         # print(table[2])
# #         # breakpoint()
# #         for el in table:
# #             title = el.find('span', class_='goods-tile__title').text
# #             # print(title)
# #             # breakpoint()
# #             price_val = el.find('span', class_='goods-tile__price-value').text
# #             price_val = [i for i in price_val if i.isdigit()]
# #             # print(price_val)
# #             # breakpoint()
# #             price_val = int(''.join(price_val))
# #             # print(price_val)
# #             # breakpoint()
# #             my_price = price_val * 1.01
# #             # print(price_val)
# #             # breakpoint()
# #             currency = el.find('span', class_='goods-tile__price-currency').text
# #             if currency == '₴':
# #                 currency = 'грн.'
# #             # print(title)
# #             # print(price_val, currency)
# #             # breakpoint()
# #             # print('.'*80)
# #             # rows.append({'title': title, 'price': price_val, 'my price': my_price, 'currency': currency})
# #             tmp = {name[0]: title, name[1]: price_val, name[2]: my_price, name[3]: currency}
# #             rows.append(tmp)
# #     return rows
# #
# #
# # def write_content(content, name):
# #     csv_title = name
# #     with open('rozetka.csv', 'w') as f:
# #     # with open('rozetka.csv', 'w', errors='ignore') as f:
# #     # with open('rozetka.csv', 'w', encoding='utf8') as f:
# #         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
# #         wr.writeheader()
# #         wr.writerows(content)
# #
# #
# #
# # # result = parsing(url, )
# # # write_content(result)
# # #
# # #
# # # # url = 'https://rozetka.com.ua/ua/notebooks/c80004/page={}/'
# # # # url = 'https://hard.rozetka.com.ua/ua/processors/c80083/page={}/'
# # #
# # urls = [
# #     # 'https://rozetka.com.ua/ua/notebooks/c80004/page={}/',
# #     # 'https://rozetka.com.ua/ua/care_lamps/c278086/page={}/',
# #     # 'https://hard.rozetka.com.ua/ua/processors/c80083/page={}/',
# #     # 'https://rozetka.com.ua/ua/mobile-phones/c80003/page={}/',
# #     # 'https://bt.rozetka.com.ua/ua/microwaves/c80162/page={}/',
# #     # 'https://rozetka.com.ua/ua/elektrosamokati/c4657382/page={}/'
# # ]
# # #
# # csv_title = ['title of product', 'old price', 'new price', 'currency']
# # res = parsing(url, csv_title)
# # write_content(res, csv_title)
# #
# # res = []
# #
# # for url in urls:
# #     for i in range(1, 2):
# #         time.sleep(0.5)
# #         res += parsing(url.format(i), csv_title)
# #
# # for i in res:
# #     for key, val in i.items():
# #         print(key, ':', val, sep='\t')
# #     print('-' * 80)
# # write_content(res, csv_title)
#

############################################ END


# import http.client
#
#
# host = "rozetka.com.ua"
# conn = http.client.HTTPSConnection(host)
# conn.request("GET", '/ua/notebooks/c80004', headers={"Host": host})
# response = conn.getresponse()
# print(response.status, response.reason)


