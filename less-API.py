

# GET - отримання
# POST - створення (отримання авторизованої інформації)
# PUT - оновлення
# DELETE - видалення


#       pip install requests
#
import requests
import json



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

r = requests.get('https://api.github.com/events', timeout=3)


# print(r)

# print(*dir(r), sep='\n')



# print(r.status_code)
# print(type(r.text), r.text)
# print(type(r.json()[0]), r.json()[0])




# r_json = r.json()
# r_text = json.dumps(r_json, indent=4)
# print(r_text)


# print('status :', r.status_code)
# print('headers :', r.headers)
# print('type-headers :', type(r.headers))

# print(*dir(r.headers), sep='\n')
# print(isinstance(r.headers, dict))
#
#
# for key, val in r.headers.items():
#     print(key, ':', val)


# print('Server :', r.headers['Server'])
# print('Date', r.headers['Date'])
# print('Date', r.headers.get('Date'))




# print(type(r.json()))

# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[3]), r.json()[3])

# d1 = r.json()[5]

# print(type(d1))
# print(d1)
# print(*d1)
# print('keys', d1.keys())
# t = tuple(d1.keys())
# print(type(t))
# print(t[0])
# print('keys', *dir(d1.keys()), sep='\n')
# print('values', d1.values())
# print('items', d1.items())

# for key, vol in d1.items():
#     print(key, ':', vol)


# w = json.dumps(r.json()[3], indent=4)
# print(w)


# for key, val in r.json()[3].items():
#     print(key, ':', val)

# print('get_json :', r.json())
# print('get_json_0 :', r.json()[0])
# print(r.json()[0]['type'])
# print('get_json_id :', r.json()[0]['id'])
# print('get_json_type :', r.json()[0]['type'])



payload = {
    'key1': 'value1',
    'key2': ['value2', 'value3']
}

# r = requests.get('https://httpbin.org/get', params=payload)
r = requests.get('https://httpbin.org/get?name=Vasya&Surname=Koval&country=Ukraine&country=France')
#
# print(r.text)
# print(r)


# print(r.json())
# print(isinstance(r.json(), dict))
# print(type(r.json())==dict)
# print(type(r.json()))



# print(r.url)
# print(type(r.url))

# r = requests.get("https://httpbin.org/get?key1=value1&key2=value2&key2=value3")
# print('url :', r.url)
# print(type(r.json()))
# print(type(r.text))
# print(r.text)

# # print(*dir(r.text), sep='\n')
# print(r.text[27:33])
# print(r.json()['args']['key2'])
# print('='*80)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r = requests.get('https://api.github.com/events')
# # print(type(r))
# print(*dir(r), sep='\n')
# print('encodind :', r.encoding)
# print('content :', r.content)
# print(type(r.json()))
# print(r.json())
# print('json :', type(r.json()[0]), r.json()[0])
# for key, vol in r.json()[0].items():
#     print(key, ':', vol)
# print(*dir(r), sep='\n')

# r = requests.get('https://api.github.com/events')
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(7))

# !!!!!!!!!!!!!!!!!!!!!!!!!

# response = requests.get("https://httpbin.org/get?key1=value1&key2=value2")

# response = requests.get('https://api.github.com/events')
# print(response.text)
# print('type :', type(response.json()))
# print(*dir(response.json()), sep='\n')
# print('type-headers :', type(response.headers))
# # print(dir(response.headers))
# print(response.headers)
# # print(*dir(response), sep='\n')
# for key, value in response.headers.items():
#     print(key, ':', value)


# print('type-text :', type(response.text))
# print('text :', response.text)
# print(isinstance(response.text, str))
# print(type(response.text)== str)
# print(type(response.text))
# for i in range(len(response.json())-1):
#     print(i+1, ': type-json :', type(response.json()[i]))
#     print('json :', response.json()[i])
# print('json :', response.json()[i].get('args'))
# print(isinstance(response.json(), list))
# print(*dir(response.headers), sep='\n')
# print(*dir(response.json()), sep='\n')
# print(*dir(response.text), sep='\n')
# print(response.json()[0])
# print(isinstance(response.json()[0], dict))
#
# print(*dir(response.json()[0]), sep='\n')

#############################################################
# https://openweathermap.org/api



# response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90')


#
# town = input('Введіть назву міста : ')
#
#
# data = {
# 	'q': town,
# 	'units': 'metric',
# 	'APPID':'b18eeec4ac22e23cfd6a45375dd0cf90'
# }
#
# response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=data)
#
#
# print(response.status_code)
# # res_text = response.text
# # print(res_text)
#
# res_json = response.json()
# # print(json.dumps(res_json, indent=4))
#
#
#
# city = res_json['name']
# ceil = res_json['weather'][0]['main']
# temp = res_json['main']['temp']
#
#
# print('=' * 80)
# print('Погода в місті', city)
# print('Небо :', ceil)
# print('Температура :', temp)
# print('=' * 80)
#
# #..........................
#
# print(res_json['weather'][0]['main'])
# print(type(res_json['weather'][0]['main']))
#
#
# print('=' * 80)
# print(response.json()['weather'])
# print(response.json()['weather'][0]['main'])
# print(response.json()['weather'][0]['description'])
# print(response.json()['main']["feels_like"])
#
# for i in response.json():
#     w = json.dumps(i, indent=4)
#     print(w)
#
#
# inx = response.url.find('?')
# print(inx)
# host_url = response.url[:inx]
# short_url = response.url[inx+1:]
# print(host_url)
# print(short_url)
# breakpoint()

############################################



# ======================== POST ===================

# data = {
#     'login': 'value',
#     'password': 'value1'
# }
#
# # r = requests.post('https://httpbin.org/post', data=data)
#
# r = requests.post('https://httpbin.org/post?page=page21', data=data)
#
# # print(r.url)
# # print('type :', type(r.text))
# # print('post_text :', r.text)
# #
# print('type-json', type(r.json()))
# print('json', r.json())
# print(json.dumps(r.json(), indent=4))
#
# print('get_json :', r.json())
# # print('type :', type(r.json()))
# print('inst :', isinstance(r.json(), dict))
# print('get_json_form :', r.json()['form'])
# print('get_json_headers :', r.json()['headers'])
# print('get_json_headers_Accept :', r.json()['headers']['Accept-Encoding'])



# ==================== PUT =========================

# d = {'login': 'my_login', 'password': 'my_password'}
# # r = requests.put('https://httpbin.org/put', data=d)
#
# r = requests.put('https://httpbin.org/put?page=page1', data={'key': 'value', 'key1': 'value2'})
# # print('put_text :', r.text)
# print(json.dumps(r.json(), indent=4))
# print('url :', r.url)
# print('get_json :', r.json())
# print('get_json_form :', r.json()['form'])




# ==================== DELETE ===================

# # r = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
# # r = requests.delete('https://httpbin.org/delete?page=page1', data={'login': 'my_login'})
# r = requests.delete('https://httpbin.org/delete', params={'page': 'page31'}, data={'login': 'my_login'})
#
# # params = {
# #     'key': "u2JnV5UpCmumAYaETsLxLUc7ctHM84bjazoehWO8HiwM"
# # }
# # r = requests.delete('https://httpbin.org/delete', params=params, data={'login': 'my_login'})
# # print('delete_text :', r.text)
# print('url :', r.url)
# print(r.json())




########################################################
#        https://api.dictionaryapi.dev/api/v2/entries/en/
########################################################

import requests


# url_bas = "https://api.dictionaryapi.dev/api/v2/entries/en/"
#
# url_word = input('Input english word : ')
# url = url_bas + url_word
#
# response = requests.get(url)
#
# res = response.json()
# result = json.dumps(res, indent=4)
# print(result)


#######################################################
#   Random CATs     https://www.freepublicapis.com/tags/popular
#                   https://api.thecatapi.com/v1/images/search
#######################################################

# url = 'https://www.dnd5eapi.co/api/races/dwarf'
#
# response = requests.get(url)
#
# print(response.text)
# r_json = json.dumps(response.json(), indent=4)
# print(r_json)

#######################################################

#
# import requests
#
# for i in range(10):
#
#     url = "https://api.thecatapi.com/v1/images/search"
#
#     response = requests.get(url).json()
#     res_print = json.dumps(response, indent=4)
#     print(res_print)


####################################################################
#### OIL PRICE #####################################################
####################################################################

import requests
import json
#
# # https://www.oilpriceapi.com/
#
#
# url = 'https://api.oilpriceapi.com/v1/prices/latest'
# headers = {
#   'Authorization': 'Token 96b90c2a2bf598680d40989ab38d54ea',
#   'Content-Type': 'application/json'
# }
#
#
# response = requests.get(url=url, headers=headers)
#
# print('status :', response.status_code)
# print('url :', response.url)
#
# # print('type-headers :', type(response.headers))
# # for key, vol in response.headers.items():
# #     print(key, ':', vol)
# # print('.'*80)
#
#
# print('type-json :', type(response.json()))
# res = response.json()
# print(json.dumps(res, indent=4))
#
#
# print('Price of oil is :', res['data']['price']*1.002, '$USA')



# # ####################### MONOBANK ###################

import requests
import datetime


url = 'https://api.monobank.ua/bank/currency'

# response = requests.get(url)
#
#
# res = response.json()
# print(json.dumps(res, indent=4))
# print(response.json())

# currencyCodeA	980  гривня
# currencyCodeB	840  долл США
# currencyCodeA	978  євро



# -----------------------------------------
# r = requests.get(url)
# print(r.status_code)
# # print(r.json())
# print('продаж доллар США:', r.json()[0]['rateSell'])
# print('купівля доллар США:', r.json()[0]['rateBuy'])
# print('продаж EURO:', r.json()[1]['rateSell'])
# print('купівля EURO:', r.json()[1]['rateBuy'])
#
#
# res = r.json()
# for i in range(len(res)):
#     for key, vol in res[i].items():
#         print(key, ':', vol)
#     print('.'*80)

# # -----------------------------------------------------
# response = requests.get(url)
# # print(*dir(response), sep='\n')
# # print(response.text)
#
# print(response.status_code)
# print(response.json())
# print('response.text      : ', type(response.text))
# print('response.json()[0] : ', type(response.json()[0]))
# for i in response.json():
#     for key, value in i.items():
#         if key == 'date':
#             print(key, datetime.datetime.fromtimestamp(value), sep='\t')
#         else:
#             print(key, value, sep='\t')
#         # print(key, value, sep='\t')
#     print('-' * 80)



##########################################################
################### PRIVAT BANK      #####################
##########################################################
import requests


url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

# response = requests.get(url)
#
# print(response.status_code)
# res = response.json()
# # print(type(res))
# # # print(res)
# # print(json.dumps(res, indent=4))
# #
# # print(res[0]['sale'])
# # for i in res:
# #     print(json.dumps(i, indent=4))
#
# for i in res:
#     print('.'*80)
#     for key, vol in i.items():
#         print(key, ':\t', vol)
# print('='*80)

########################################################
                            # NBU
# import requests
#
#
# url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
#
# response = requests.get(url_nbu)
# # print(type(response))
# res = response.json()
# result = json.dumps(res, indent=4)
# print(result)
# for i in range(len(res)):
# # #     # print(res[i])
# # #     # breakpoint()
# #     if res[i]['cc'] == 'EUR':
#     if res[i]['cc'] == 'PLN':
# #     if res[i]['cc'] == 'XPD':
#         print(i)
# # print('Курс  EUR:', res[31]['rate'])
# # print('Курс  USD:', res[24]['rate'])
# print('Курс  Платина:', res[32]['rate'])
# # print('Курс  Паладія:', res[60]['rate'])



#######################################################
################## open-weather #######################
#######################################################
# import requests
# import json
# from datetime import datetime
#
#
# url = 'https://api.openweathermap.org/data/2.5/weather'
# params = {"id": "524901",
#           "appid": "fdd717a05cc211b145bfadd1e754f749",
#           # "q": 'London',
#           "q": input('Input city and country with "," : '),
#           }
#
# response = requests.get(url, params=params)
#
# # print(response.url)
# # print(response.status_code)
# # print(response.json())
# res = response.json()
# print('.'*80)
# res_print = json.dumps(res, indent=4)
# # print(res_print)
# # for key, vol in res.items():
# #     print(key, '\t:', vol)
# print(f"The weather in {res['name']} :")
# w = res['weather'][0]
# t = res['main']
# print('main        :', w['main'])
# print('temperature :', int((t['temp']-273.15)*100)/100)
# print('feels_like  :', int((t['feels_like']-273.15)*100)/100)
# print('temp_min    :', int((t['temp_min']-273.15)*100)/100)
# print('temp_max    :', int((t['temp_max']-273.15)*100)/100)
# print('pressure    :', t['pressure'], 'MPa')
# print('description :', w['description'])
# print('visibility  :', str(res['visibility']/100) + '%')
# print('clouds      :', res['clouds']['all'], '%')
# print('wind :')
# print('\t', 'speed :', res['wind']['speed'])
# print('\t', 'deg   :', res['wind']['deg'])
# print('time   :', datetime.fromtimestamp(res['dt']))


################################################################

# import requests
#
# url = "https://meteostat.p.rapidapi.com/stations/hourly"
#
# querystring = {"station":"10637","start":"2020-01-01","end":"2020-01-01","tz":"Europe/Berlin"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "meteostat.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# res = response.json()
# result = json.dumps(res, indent=4)
# print(result)



################################################################

#
# import requests
#
# url = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/scheduled-events/2025-11-04"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "sportapi7.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
#
# print(json.dumps(response.json(), indent=4))
#


################################################################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/schedule"
#
# querystring = {
#     "station_id":"dcbd21fc-9603-11e6-9066-549f350fcb0c",
#     "date":"15.03.2025"}
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# res = response.json()
# print(json.dumps(res, indent=4))
#
# station = input('Station from :')
# lenth = len(res['schedule']['departures'])
# for i in range(lenth):
#     for name in res['schedule']['departures'][i]['stops']:
#         if station in name['name']:
#
#             print(name['name'])
#             print(name['uuid'])
#             print('.'*80)


# Berlin central bus station
# dcbaaee6-9603-11e6-9066-549f350fcb0c
# 40d8f682-8646-11e6-9066-549f350fcb0c
#
# Strasbourg
# 40d90f52-8646-11e6-9066-549f350fcb0c
#
# Paris (Bercy Seine)
# dcc5426b-9603-11e6-9066-549f350fcb0c

####################################
####################################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
# querystring = {"query":input('Station :')}
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# res = response.json()
# print(json.dumps(res, indent=4))
#
# print(res[0]['city']['name'], res[0]['city']['id'])
# print(res[0]['id'])
#######################################################################
# Paris CDG Airport 472ef68b-be37-43d2-94ce-72d570493e52
# dcc05c30-9603-11e6-9066-549f350fcb0c

# Strasbourg 40d90f52-8646-11e6-9066-549f350fcb0c
# dcbac843-9603-11e6-9066-549f350fcb0c
#
# import requests
#
# url = "https://flixbus2.p.rapidapi.com/trips"
#
# querystring = {
#     "from_id":"472ef68b-be37-43d2-94ce-72d570493e52",
#     "to_id":"40d90f52-8646-11e6-9066-549f350fcb0c",
#     "date":"25.01.2025",
#     "adult":"1",
#     "search_by":"cities",
#     "children":"0",
#     "bikes":"0",
#     "currency":"EUR"}
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# res = response.json()
# print(json.dumps(res, indent=4))


################ FULL FLIX-BUS ##########################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
# }
#
# querystring = {"query":input('Station from : ')}
#
# response = requests.get(url, headers=headers, params=querystring)
#
# res = response.json()
# print(response.status_code)
# station_from = res[0]['city']['id']
#
# querystring = {"query":input('Station to : ')}
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.status_code)
# res = response.json()
# station_to = res[0]['city']['id']
#
#
# url = "https://flixbus2.p.rapidapi.com/trips"
#
# querystring = {
#     "from_id": station_from,
#     "to_id": station_to,
#     "date": input('Введіть дату у форматі DD.MM.YYYY : '),
#     "adult":"1",
#     "search_by":"cities",
#     "children":"0",
#     "bikes":"0",
#     "currency":"EUR"}
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# res = response.json()
# print(json.dumps(res, indent=4))
# i = 0
# print('='*80)
# for el in res['journeys']:
#     i+=1
#     if el['changeovers'] == 0:
#         print(i, ')    Прямий рейс наступний:')
#         print(el['segments'][0]['dep_name'])
#         print(el['segments'][0]['arr_name'])
#         print(el['segments'][0]['dep_offset'])
#         print(el['segments'][0]['arr_offset'])
#         print(el['fares'][0]['price'], el['fares'][0]['currency'])
#     else:
#         print(i,')    Рейс не прямий...')
#
#
# print('='*80)


##############################################################

# import requests
#
# url = "https://footapi7.p.rapidapi.com/api/rankings/uefa/clubs"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "footapi7.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
#
# # print(response.json())
# res = response.json()
# # print(json.dumps(res, indent=4))
# i = 0
# country = input('Введіть назву країни англійською (або ALL): ')
# for el in res['rankings']:
#     i+=1
#     if el['team']['country']['name'] == country or country.lower() == 'all':
#         print(i, ':', el['team']['name'], el['team']['country']['name'])
#

##############################################################


#######################################
#### SPORT ############################
# #######################################
# import requests
# import json
#
# url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
#
# querystring = {"page": "1"}
#
# headers = {
#     'x-rapidapi-host': "sportscore1.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.json())
#
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)

#######################################
#### BOOKING  #########################
# import requests
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/map-markers"
#
# querystring = {"locale":"en-gb","hotel_id":"1676161"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# res = response.json()
# print(json.dumps(res, indent=4))

#### BOOKING  #########################
# import requests
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
#
# querystring = {
#                 "locale":"en-gb",
#                "room_number":"1",
#                "checkin_date":"2026-02-19",
#                "checkout_date":"2026-02-20",
#                "filter_by_currency":"EUR",
#                "longitude":"19.7127",
#                "latitude":"41.4206",
#                "adults_number":"2",
#                "order_by":"popularity",
#                "units":"metric",
#                "page_number":"0",
#                "children_number":"0",
#                "include_adjacency":"false",
#                "children_ages":"0,0",
#                "categories_filter_ids":"class::2,class::4,free_cancellation::1"
#                }
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "booking-com.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
#
# print(json.dumps(response.json(), indent=4))




#######################################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
#
# querystring = {"query":"Paris City Centre"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# print(json.dumps(response.json(), indent=4))

#######################################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getRoomList"
#
# querystring = {"hotel_id":"12981264",
#                "arrival_date":"2026-03-10",
#                "departure_date":"2026-03-11",
#                "adults":"1",
#                "room_qty":"1",
#                "units":"metric",
#                "temperature_unit":"c",
#                "languagecode":"en-us",
#                "currency_code":"EUR",
#                "location":"US"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# print(json.dumps(response.json(), indent=4))



#######################################
# import requests
# import json
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotelsByCoordinates"
#
# querystring = {"latitude":"48.85354333883736",
#                "longitude":"2.3377870774203857",
#                "arrival_date":"2026-03-12",
#                "departure_date":"2026-03-13",
#                "adults":"1",
#                "room_qty":"1",
#                "units":"metric",
#                "page_number":"1",
#                "temperature_unit":"c",
#                "languagecode":"en-us",
#                "currency_code":"EUR",
#                "location":"US"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# print(json.dumps(response.json(), indent=4))





#######################################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelPhotos"
#
# querystring = {"hotel_id":"477761"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# print(json.dumps(response.json(), indent=4))


#######################################
import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v1/hotels/searchHotels"

querystring = {"entityId":"27540983","checkin":"2026-02-14","checkout":"2026-02-15","adults":"1","rooms":"1","limit":"30","sorting":"-relevance","currency":"USD","market":"en-US","countryCode":"US"}

headers = {
	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
print(json.dumps(response.json(), indent=4))

#######################################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getAvailability"
#
# querystring = {"hotel_id":"12981264","min_date":"2026-03-10","max_date":"2026-03-11","adults":"1","currency_code":"USD","location":"US"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
#
#
# print(json.dumps(response.json(), indent=4))
# #######################################

# import requests
# import json
#
#
# url = "https://booking-com.p.rapidapi.com/v1/hotels/room-list"
#
# querystring = {
#     "locale": "en-gb",
#     "checkin_date": input('checkin_date (YYYY-MM-DD) = '),
#     "checkout_date": input('checkout_date (YYYY-MM-DD) = '),
#     "currency": "USD",
#     # "hotel_id": "1676161",
#     "hotel_id": "12981264",
#     "adults_number_by_rooms": "1",
#     "units": "metric",
#     "children_number_by_rooms": "0",
#     "children_ages": "1,0"
# }
#
# headers = {
#     'x-rapidapi-host': "booking-com.p.rapidapi.com",
#     'x-rapidapi-key': "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6"
#     }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.text)
# # print(response.json())
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)




#######################################
### POPULATION ########################
#######################################
#
# import requests
# import json
#
# import requests
#
# url = "https://get-population.p.rapidapi.com/population/country"
#
# country = input('Input name of country : ')
# querystring = {"country": country}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "get-population.p.rapidapi.com"
# }
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.status_code)
# print(response.url)
# #
# # print(response.text)
# # print(response.json())
#
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
#
# print(resp_print)
# print('The population in', country, 'is', response.json()['readable_format'], '!')
# # # #





####################################################################
#################### ПРИКЛАД (випадкові "фейкові" дані) #################
# import requests
# import json
#
#
#
# for i in range(5):
#     response = requests.get("https://randomuser.me/api/")
#
#     # print(response.text)
#     # print(response.json())
#     # print(type(response.json()))
#     resp_json = json.dumps(response.json(), indent=4)
#     # print(resp_json)
#     # #
#     # print('response.json() : ', type(response.json()))
#     # print('      resp_json : ', type(resp_json))
#     # print(resp_json)
#     #
#     #
#     # print(response.json()['results'][0]['name'])
#     print('=' * 60)
#     print('     title : ', response.json()['results'][0]['name']['title'])
#     print('first name : ', response.json()['results'][0]['name']['first'])
#     print(' last name : ', response.json()['results'][0]['name']['last'])
#     print(' country   : ', response.json()['results'][0]['location']['country'])
#     print('       age : ', response.json()['results'][0]['dob']['age'])
#     print('Date of bth: ', response.json()['results'][0]['dob']['date'])
#     print('     email : ', response.json()['results'][0]['email'])
#     print('     photo : ', response.json()['results'][0]['picture']['large'])
#     print('=' * 60)


################################################################
########## GOOGLE - TRANSLATOR #########################
################################################################
#
# import requests
#
# url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"
#
# payload = {
# 	"from": input('Choose source language (for example: en, fr, es ...) : '),
# 	"to": input('Choose target language (for example: ru, en, fr, es ...) : '),
# 	"text": input('Input text : ')
# }
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "google-translate113.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# #
# translate_res = response.json()
# # print(json.dumps(translate_res, indent=4))
#
#
#
# translated_text = translate_res["trans"]
#
# #
# print(translated_text)


##########################################
############ coordinats ##################
##########################################
# import requests
# import json
#
#
# response = requests.get('https://ipinfo.io/json')
#
# data = response.json()
# print(type(data))
# # print(data)
#
# print(json.dumps(data, indent=4))
#
# latitude = data['loc'].split(',')[0]
# longitude = data['loc'].split(',')[1]
# print('longitude :', longitude)
# print('latitude  :', latitude)
# print('city      :', data['city'])

####################################################

################################################################

#
# import requests
#
#
# url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"
#
# querystring = {
# 	# "query":"wsgr.com",
# 	"query":input('Input URL : '),
# 	"match_email_domain":"false",
# 	"external_matching":"false"}
#
# headers = {
# 	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
# print(json.dumps(response.json(), indent=4))
#
# # #################### duan.edu.ua
# result = []
# for email in response.json()['data'][0]['emails']:
# 	# print('email :', email['value'])
# 	result.append(email['value'])
# result.sort()
# for i in result:
# 	print('email : ', i)


################################################################
############# PYTHONANYWHERE ###############################
################################################################
# import requests
# import json
#
#
# res = ''
# # url = "http://127.0.0.1:8000/api/v3/book/20/"
# for i in range(1, 5):
#     url = f"http://riv2.pythonanywhere.com/api/v3/book/?page={i}"
#
#     # headers = {
#     # 'Authorization': "Token f21dba2f6a67055deaa3e9b6859964abe124fa4f"
#     # }
#     response = requests.request("GET", url)
#     # response = requests.request("GET", url, headers=headers)
#     resp_print = json.dumps(response.json(), ensure_ascii=False, indent=4)
#     res += resp_print
#
# print(res)




################################### END ################################

















# with open('dictionnaire.txt', 'r') as f:
#     text = f.read()
#
# # print(text)
# lst = text.upper().split('\n')
# print(lst)
# print(len(lst))


# ???????????????????????????????????????????????????????
################### ВАЛЮТЫ С САЙТА www.cbr.ru #################33
# import requests
# import pandas as pd
# import xml.etree.ElementTree as et
# #
# v_date = '17.11.2021'
# # # Адрес api метода для запроса get
# url = 'https://www.cbr.ru/scripts/XML_daily.asp'
# params = {
#     'date_req': v_date
# }
# # # Отправляем get request (запрос GET)
# response = requests.get(url, params)
# print(list(response))
# tree = et.ElementTree(et.fromstring(response.text))
# root = tree.getroot()
# df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
# rows = []
# for node in root:
#     s_numcode = node.find("NumCode").text if node is not None else None
#     s_charcode = node.find("CharCode").text if node is not None else None
#     s_nominal = node.find("Nominal").text if node is not None else None
#     s_name = node.find("Name").text if node is not None else None
#     s_value = node.find("Value").text if node is not None else None
#
#     rows.append({"date": v_date, "numcode": s_numcode,
#                  "charcode": s_charcode, "nominal": s_nominal,
#                  "name": s_name, "value": s_value})
# df = pd.DataFrame(rows, columns=df_cols)
# print(df.head())





############### НЕ РАБОТАЕТ (нужен логин и пароль) ###########
#######################################################################
# # Импортируем библиотеку requests
# import requests
#
# # Адрес api метода для запроса get
# url_param = "https://api-metrika.yandex.net/stat/v1/data"
# # Задаем параметры для API
# api_param = {
#     "ids": "5251515",
#     "metrics": "ym:s:users,ym:s:visits,ym:s:pageviews,ym:s:bounceRate,ym:s:pageDepth,ym:s:avgVisitDurationSeconds",
#     "dimensions": "ym:s:date,ym:s:<attribution>TrafficSource,ym:s:<attribution>SourceEngine,ym:s:gender",
#     "date1": "10daysAgo",
#     "date2": "yesterday",
#     "sort": "ym:s:date",
#     "accuracy": "full",
#     "limit": 5
# }
# header_params = {
#     'GET': '/management/v1/counters HTTP/1.1',
#     'Host': 'api-metrika.yandex.net',
#     'Authorization': 'OAuth AgAAlkjlkjKAa976ZB-rXh-t-ookfJJcMP979ZU0',
#     'Content-Type': 'application/x-yametrika+json'
# }
# # Отправляем get request (запрос GET)
# response = requests.get(
#     url_param,
#     params=api_param,
#     headers=header_params
# )
# result = response.json()
# print(result)
# query = result['query']
# data = result['data']
# print(query)
# print('======================')
# print(data)
#########################################################################

##########################################################################


################## INF ##############
# # Адрес api метода для запроса get
# API_KEY = '5ad2ecb53d794e6885f8de4bfe6f855d'
# url = 'https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely'
# url = 'https://api.weatherbit.io/v2.0/current?key=API_KEY'


#
# import requests
#
#
# r = requests.get('https://riv2.pythonanywhere.com/api/v1/booklist/', timeout=3)
#
# print('status :', r.status_code)
#
# for key, val in r.headers.items():
#     print(key, ':', val)
# print('='*80)
# d1 = json.dumps(r.json(), indent=4)
# print(d1)
# print('='*80)
# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[0]), r.json()[0])
# for key, val in r.json()[1].items():
#     print(key, ':', val)
#=======================================================







