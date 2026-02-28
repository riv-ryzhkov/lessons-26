# pip install bs4
# https://beautiful-soup-4.readthedocs.io/en/latest/


import requests
from bs4 import BeautifulSoup as BS
import csv
import time


################################################

import requests
from bs4 import BeautifulSoup


# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)

# print(response.text)
# print(type(response.text))

# soup = BeautifulSoup(response.text, 'html.parser')
# print(type(soup))
# print(soup)


# print(*dir(soup), sep='\n')



# ##################### start info #############

# print(soup.div.prettify())  # tags <div>


# o = soup.div.prettify()
# o = soup.div
# print(type(o))    # tags <div>
# print(o)  # tags <div>



# print(soup.div.a)     # tags <div><a>    </a></div>


# print(soup.find('div').find('a'))   # tags <div><a>    </a></div>



# print(soup.find('head'))   # tag <head>


# print(soup.find('head').find_all('link')[1])  # tags <head><link> [1]  </link></head>
# print(soup.find('head').find_all('link')[1]['href'])  # tags <head><link> [1]<href=" ">  </link></head>


# print(soup.div.a)  # tags <div><a>    </a></div>
# print(soup.div.a.svg['xmlns']) # tags <div><a><svg xmlns=" "></svg></a></div>



# print(soup.h4)  # tags <h4>


# tag = soup.li
# tag = soup.li.text
# tag = soup.li.a['href']
# tag = soup.li.a['target']
# print(soup.li)
# print(tag)
# print(type(tag))




# tag = soup.body
# # print(*dir(tag), sep='\n')
# # print(tag)
#
# # print(tag.a)
# print(tag.span)
# print(tag.span['class'])






# print(soup.head.link)
# print(soup.head.link['href'])
# print(soup.head.link['rel'])
# print(soup.head.link['type'])




# print(soup)
# print(soup.text)
# print(type(soup))
# print(type(soup.text))
# print('.'*80)
#
# print(soup.text.replace('\n\n', ''))


# ...................................

# print(soup.prettify())
# print(type(soup.prettify()))



# print(soup.link)
# print(type(soup.link))





# print(soup.find_all('link'))
# print(type(soup.find_all('link')))
#
#
# print(*dir(soup.find_all('link')), sep='\n')  # close to list!!!!!






# print(*soup.find_all('link'), sep='\n')


# for el in soup.find_all('link'):
#     # print(el['href'])
#     if el['href'].startswith('/'):
#         print('https://scrapingclub.com'+el['href'])
#     else:
#         print(el['href'])



# .........................

# print(*soup.find_all(['p']), sep='\n')
# print(*soup.find_all(['a', 'h4']), sep='\n\n')




# res = soup.find_all(['p', 'a'])
# print(type(res))
# print(*res, sep='\n\n')




# res = soup.find_all(['p', 'a'], limit=5)
# for el in range(len(res)):
#     print()
#     print(el+1, ':')
#     print(res[el])
#     print('.'*60)



# ......................................................


# print(soup.find(id="banner"))
# print('len id = ', len(soup.find_all(id="banner")))


# print('len id=True :', len(soup.find_all(id=True)))
# print(*soup.find_all(id=True), sep='\n' + '.'*150 + '\n\n')


# .......................................................


# print(soup.find_all(class_="container"))

# print(*soup.find_all(class_="nav-link"), sep='\n')

# print(soup.find_all('h4'))


# print(soup.find_all('div', class_="alert"))
# print(soup.find_all('div', class_="alert-success"))

# print(soup.find_all('div', role="alert"))




# print(soup.find_all('div', class_='px-4 mb-6 w-full sm:w-1/3 md:w-1/4 lg:w-4/12'))
# print(soup.find_all('div', class_='px-4 mb-6 w-full sm:w-1/3 md:w-1/4'))
# print(soup.find_all('div', class_='w-full px-4 mb-6 sm:w-1/3 md:w-1/4 lg:w-4/12'))

# print(soup.select('div.w-full.px-4.mb-6'))   # вільна послідовність
# print(soup.select('div.px-4.mb-6.w-full'))   # вільна послідовність






# print(soup.a)
# print(soup.find('a'))




# print(soup('a'))
# print(soup.find_all('a'))





# res = soup(['p', 'a'], limit=10)
# for el in res:
#     print(el)
#     print('.'*40)
#
#


##########################################
# parsing
###############################
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
#
# soup = BS(response.text, 'html.parser')
# # print(type(soup))
# # print(soup)
#
# items = soup.find_all('div', class_='w-full rounded border')
#
# print(type(items))
# print(*dir(items), sep='\n')
#
#
# print(items)
#
# print(type(items[0]))
#
# # print(*dir(items[0]), sep='\n')
#
#
# print(items[0].prettify())
#
# link = 'https://scrapingclub.com' + items[0].a['href']
# print(link)
# title = items[0].h4.text
# print(title)
# price = items[0].h5.text
# print(price)
#
#
#
# # for i in items:
# for n, i in enumerate(items, start=1):
# #     # print(i)
# # #     # breakpoint()
#     image = i.img['src']
#     name = i.find('h4').text.strip()
#     price = i.find('h5').text
#     price = '$' + str(float(price[1:]) + 1)
#     print(f'{n}:  {price} за {name} https://scrapingclub.com{image}')


###################### pages ######################
# url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
# response = requests.get(url)
#
# soup = BS(response.text, 'html.parser')
#
# def parsing(url):
#     # url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     items = soup.find_all('div', class_='w-full rounded border')
#     for n, i in enumerate(items, start=1):
#         image = i.img['src']
#         name = i.find('h4').text.strip()
#         price = i.find('h5').text
#         price = '$' + str(float(price[1:]) + 1)
#         print(f'{n}:  {price} за {name} https://scrapingclub.com{image}')
#
#
# for i in range(5):
#     url = f'https://scrapingclub.com/exercise/list_basic/?page={i}'
#     print(f'###### PAGE {i+1} ' + '#' * 40)
#     parsing(url)
#     print('=' * 80)




###################################################################################
# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# # # print(response.text)
# soup = BS(response.text, 'html.parser')
# # # print(type(soup))
# # # print(soup)
# #
# #
# quotes = soup.find_all('span', class_='text')
# # print(quotes)
# for n, el in enumerate(quotes, start=1):
#     print(n, ':', el.text)
#
#
#
# authors = soup.find_all('small', class_='author')
# for n, el in enumerate(authors, start=1):
#     print(n, ':', el.text)
#
#
# tags = soup.find_all('div', class_='tags')
# for n, el in enumerate(tags, start=1):
#     # print(n, ':', el)
#     print(n, ':')
#     tags = el.find_all('a')
#     for i in tags:
#         print(i.text, end=' ')
#     print()
#     print('-'*80)

# ############# PAGES ####################
#
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



############################################################################
################ BBC.COM    #####################################
############################################################################

# url = 'https://www.bbc.com/ukrainian'
#
# response = requests.get(url)
# print(response.status_code)
#
# soup = BS(response.text, "html.parser")

# print(soup)

#
# soup = soup.find('section', attrs={'aria-labelledby': 'Головне'})
# # print(soup)
#
# allNews = soup.find_all('li')
# # print('allNews :', allNews)
# print(len(allNews))
#
#
# # soup1 = allNews[0]
# # print(allNews[0].prettify())
#
# for soup1 in allNews:
#     my_image = soup1.img['src']
#     my_title = soup1.find('div', class_='promo-text').a.text
#     my_text = soup1.find('div', class_='promo-text').p.text
#
#
#     my_time = soup1.find('div', class_='promo-text').time['datetime']
#     my_time = my_time + '  ' + soup1.find('div', class_='promo-text').time.text
#
#
#
#     my_ref = soup1.find('div', class_='promo-text').a['href']
#     print('='*80)
#     print('Title     :', my_title)
#     print('Text      :', my_text)
#     print('Reference :', my_ref)
#     print('Photo     :', my_image)
#     print('Time      :', my_time)
#
#     my_url = my_ref
#     my_response = requests.get(my_url)
#     print(my_response.status_code)
#     new_soup = BS(my_response.text, "html.parser")
#     new_text = new_soup.find('main').text
#     print('All information:', new_text)
#
#
#
# print('*'*80)
#


# for el in allNews:
#     # img = el.img['src']
#     img = el.find('img')['src']
#     # title = el.a.text
#     title = el.find('a').text
#     time = el.time['datetime'] + '>>' + el.time.text
#     # time = el.time.text
#     text = el.p.text
#     link = el.a['href']
#
#     print('time :', time)
#     print('.' * 80)
#     print('title :', title)
#     print('.' * 80)
#     print('short text :', text)
#     print('.' * 80)
#     print('picture :', img)
#     print('.' * 80)
#     print('link :', link)
#     print('=' * 80)

################################################################################
#### NEWS ######################################################################
###############################################################################
#
#
# url_list = ['http://mignews.com/mobile', 'https://www.pravda.com.ua']
# class_list = ['text-color-dark', "article_news"]
# # url = 'http://mignews.com/mobile'
# # url = 'https://www.pravda.com.ua'
#
# for i in range(2):
#     url = url_list[i]
#     my_class = class_list[i]
#     # # # # #
#     page = requests.get(url)
#     print(page.status_code)
#     print(page.url)
#     #
#     soup = BS(page.text, "html.parser")
#     # # # # print(soup)
#
#     # allNews = soup.findAll('div', class_='text-color-dark')
#     # allNews = soup.findAll('div', class_="article_news")
#     allNews = soup.findAll('div', class_=my_class)
#     # print(allNews[0].text.strip())
#     # print('https://mignews.com' + allNews[0].a['href'])
#     # #
#     #
#     # #     1st  way
#     # #====================================
#     for data in allNews:
#         # print(data.text)
#         print(data.text.strip())
#         print('https://mignews.com' + data.a['href'])
#
#
#         # print('http://mignews.com/mobile'+data.a['href'])
#         # print('https://www.pravda.com.ua/'+data.a['href'])
#         print('='*60)
#     print('*'*80)
#     print('*'*80)
#     print('*'*80)
#


#
# #     2nd  way
# #====================================
#
# filteredNews = {}
#
# for data in allNews:
#     filteredNews[data.text.strip()] = data.a['href']
# print('=' * 80)
#
# # print(filteredNews)
# # breakpoint()
#
# for key, vol in filteredNews.items():
#     print(key)
#     if vol.startswith('/'):
#         # print('http://mignews.com'+vol)
#         # print('https://www.pravda.com.ua'+vol)
#         print(url+vol)
#     else:
#         print(vol)
#     print('=' * 80)


#############################################

#
# url = 'https://www.pravda.com.ua/'
#
# page = requests.get(url)
# print(page.status_code)
#
# filteredNews = {}
#
# soup = BS(page.text, "html.parser")
# # allNews = soup.findAll('div', class_="article_header")
# allNews = soup.findAll('div', class_="article_news")
# # print(allNews[2].prettify())
# for data in allNews:
#     filteredNews[data.text.strip()] = data.a['href']
# print('=' * 80)
# for key, vol in filteredNews.items():
#     print(key)
#     if vol.startswith('/'):
#         print('https://www.pravda.com.ua'+vol)
#     else:
#         print(vol)
#     print('=' * 80)


#################################################
############### SPORT.UA ########################
#################################################
#
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
#
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
#     print(csv_title)
#
#     with open('sport.csv', 'w', encoding='utf8') as f:
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
import requests
from bs4 import BeautifulSoup as BS

#
# # url = 'https://bottlepy.org/docs/dev/'
# url = 'https://cnn.com/'
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


#
# # .........................................................
# #
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
#     'https://bottlepy.org/docs/dev/',
#     'https://sport.ua/uk/',
#     'https://price.ua/',
#     'https://bbc.com/',
#     'https://beautiful-soup-4.readthedocs.io/en/latest/',
#     'https://cnn.com/'
# ]
#
#
# for url in urls:
#     print('Links in', url)
#     for num, link in enumerate(get_links(url), start=1):
#         print(num, ':', link)
#     print('='*80)



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
#
#         # print(product.prettify())
#         # breakpoint()
#         # list_products = product.find_all('div', attrs={'class': 'product-block type2 ga_container black-link-style split-4-cards is-model'})
#         list_products = product.find_all('div', attrs={'class': 'product-block'})
#         # print(*list_products[5], sep='\n')
#         # breakpoint()
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
#     with open('price.csv', 'w', encoding='utf8') as f:
#     # with open('price.csv', 'w') as f:
#         wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         wr.writeheader()
#         wr.writerows(content)

#
# url = 'https://price.ua/ua/catc371t2/page{}.html'
# # url = 'https://price.ua/ua/catc1081t2/page{}.html'
# url = 'https://price.ua/ua/catc52t2/page{}.html'
# url = 'https://price.ua/ua/catc52t2'
# url = 'https://price.ua/ua/catc52t2/page{}.html'
# url = 'https://price.ua/ua/catc6399t2.html'
# url = 'https://price.ua/ua/catc6399t2/page{}.html'
# url = 'https://price.ua/ua/catc501t2/page{}.html'

# csv_title = ['My_title', 'Old_price_str', 'my_NEW_price', 'pic', 'url']
#
# # print(get_content(url, csv_title))
# # breakpoint()
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


# url ='https://mon.gov.ua/'
#
#
#
#
#
# # session = requests.session()
# page = requests.get(url)
# print(page.status_code)
#
# soup = BS(page.text, "html.parser")
#
# soup = soup.find('div', class_='news-block')

# articles = soup.find_all('article')
# # print(articles[0])
#
# for el in articles:
#     print(el.div.text)
#     print(el.span.text)
#     print(el.a['href'])
#     print('='*80)


# # ........................................
# all = soup.find_all('a')
# for n, i in enumerate(all):
#     if i.has_attr('href') and i['href'] != '#':
#         print('.' * 80)
#         print(n, ':', i.text.strip().replace('\n', ''))
#         if i['href'].startswith('http'):
#             print(i['href'])
#         else:
#             print(f"https://mon.gov.ua/{i['href']}")



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
#     with open('olx.csv', 'w', encoding='utf8') as f:
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



##########################################


################################## END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
###############   DZ  Домашнє завдання ################################
########################################################################


# # DZ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# pip install bs4     # запустить в терминале!!!!!!!

# https://beautiful-soup-4.readthedocs.io/en/latest/


import requests
from bs4 import BeautifulSoup as BS


def get_content(url, table_name):
    response = requests.get(url)
    print(response.status_code)
    soup = BS(response.text, "html.parser")
    result = []
    news_list = soup.find_all('div', class_='l-sidebar__gap')
    # print(news_list)
    # breakpoint()
    for news in news_list:
        # print(news.prettify())
        href = news.a.get('href')
        title = news.a.text.replace('\n', '').strip()
        time = news.time.text if news.time else 'NoTime'
        news_dic = {
            table_name[0]: time,
            table_name[1]: title,
            table_name[2]: href
        }
        result.append(news_dic)
    return result

def write_content(content, table_name):
    csv_title = table_name
    with open('news.csv', 'w', encoding='utf-8-sig') as f:
        wr = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        wr.writeheader()
        wr.writerows(content)


url = 'https://tsn.ua/'
table_name = ['time', 'title', 'reference']
count = 0
content = get_content(url, table_name)
for el in content:
    count += 1
    print('='*80)
    print(f'News No.{count} :')
    for key, val in el.items():
        print(key, ':', val)
write_content(content, table_name)





