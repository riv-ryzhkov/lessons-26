

# GET - отримання
# POST - створення (отримання авторизованої інформації)
# PUT - оновлення
# DELETE - видалення


#       pip install requests
#
import requests
import json
import matplotlib.pyplot as plt


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# r = requests.get('https://api.github.com/events', timeout=3)
#
#
# print(r, type(r))
#
# # print(*dir(r), sep='\n')
#
# print(r.status_code, type(r.status_code))
# print(type(r.text), r.text)
# print(type(r.json()), r.json())
# print(type(r.json()[0]), r.json()[0])
# print(type(r.json()[0].get('repo')), r.json()[0]['repo']['name'])

# r_json = r.json()
# r_text = json.dumps(r_json, indent=4)
# print(r_text)
# print("r_text :", type(r_text))
# print("r_json :", type(r_json))
# print("r_json[0] :", type(r_json[0]))


# print('status :', r.status_code)
# print('headers :', r.headers)
# print('type-headers :', type(r.headers))

# print(*dir(r.headers), sep='\n')
# print(isinstance(r.headers, dict))


# for key, val in r.headers.items():
#     print(key, ':', val)


# print('Server :', r.headers['Server'])
# print('Date', r.headers['Date'])
# print('Date', r.headers.get('Date'))


# print(type(r.json()))

# print('get_json :', type(r.json()), *r.json(), sep='\n\n')
# print('get_json :', type(r.json()[3]), r.json()[3])

# d1 = r.json()[5]

# print(type(d1))
# print(d1)
# print(*d1)
# print('keys', d1.keys())

# for key, vol in d1.items():
#     print(key, ':', vol)


# w = json.dumps(r.json()[3], indent=4)
# print(w)


###################################################
# payload = {
#     'key1': 'value1',
#     'key2': ['value2', 'value3']
# }

# r = requests.get('https://httpbin.org/get')
# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.get('https://httpbin.org/get?name=Vasya&Surname=Koval&country=Ukraine&country=France')
#
# print(r.text)
# print(r)


# print(r.json(), type(r.json()))
# print(r.json().get('args').get('country'))
# print(isinstance(r.json(), dict))
# print(type(r.json())==dict)
# print(type(r.json()))



# print(r.url)
# print(type(r.url))
#
# r = requests.get("https://httpbin.org/get?key1=value1&key2=value2&key2=value3")
# print('url :', r.url)
# print(type(r.json()))
# print(type(r.text))
# print(r.text)

# print(*dir(r.text), sep='\n')
# print(r.text[27:33])
# print(r.json()['args']['key2'])
# print('='*80)




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# r = requests.get('https://api.github.com/events')
# print(type(r))
# print(*dir(r), sep='\n')
# print('encodind :', r.encoding)
# print('content :', r.content)
# print(type(r.json()))
# print(r.json())
# print('json :', type(r.json()[0]), r.json()[0])
# for key, vol in r.json()[0].items():
#     print(key, ':', vol)

#
# r = requests.get('https://api.github.com/events')
# print(*dir(r), sep='\n')
# r = requests.get('https://api.github.com/events', stream=True)
# print(r.raw)
# print(r.raw.read(7))


#############################################################
# https://openweathermap.org/api
import json
import time

# print(*dir(time), sep='\n')


# url = 'http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90'
# response = requests.get(url)
# #
# print(response.status_code)
# print(response.json())
# res = json.dumps(response.json(), indent=4)
# print(res)
#
#
# town = input('Введіть назву міста : ')

#
# data = {
# 	# 'q': town,
# 	'q': 'Dnipro',
# 	'units': 'metric',
# 	'APPID':'b18eeec4ac22e23cfd6a45375dd0cf90'
# }
#
# response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=data)
#
#
# print(response.status_code)
# res_text = response.text
# print(res_text)
#
# res_json = response.json()
# print(json.dumps(res_json, indent=4))


#
# city = res_json['name']
# ceil = res_json['weather'][0]['main']
# ceil1 = res_json['weather'][0]['description']
# temp = res_json['main']['temp']
# sunrise = res_json['sys']['sunrise']
# sunset = res_json['sys']['sunset']


# print('=' * 80)
# print('Погода в місті', city)
# print('Небо :', ceil)
# print('Небо додатково :', ceil1)
# print('Температура :', temp)
# print('Схід сонця :',  sunrise)
# # print('Схід сонця :', time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(sunrise)))
# print('Захід сонця :', sunset)
# # print('Захід сонця :', time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(sunset)))
# print('=' * 80)

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

# for i in response.json():
#     w = json.dumps(i, indent=4)
#     print(w)

# print(response.url)
# inx = response.url.find('?')
# print(inx)
# host_url = response.url[:inx]
# short_url = response.url[inx+1:]
# print(host_url)
# print(short_url)
# # breakpoint()
# res = response.url.split('?')
# print(res[0])
# print(res[1])


############################################



# ======================== POST ===================

# data = {
#     'login': 'value',
#     'password': 'value1'
# }

# r = requests.post('https://httpbin.org/post', data=data)

# r = requests.post('https://httpbin.org/post?page=page21', data=data)
# r = requests.post('https://httpbin.org/post?page=page21', params={'key1':4354}, data=data)
#
# print(r.url)
# print('type :', type(r.text))
# print('post_text :', r.text)
#
# print('type-json', type(r.json()))
# print('json', r.json())
# print(json.dumps(r.json(), indent=4))
#############################################
# print('get_json :', r.json())
# # print('type :', type(r.json()))
# print('inst :', isinstance(r.json(), dict))
# print('get_json_form :', r.json()['form'])
# print('get_json_headers :', r.json()['headers'])
# print('get_json_headers_Accept :', r.json()['headers']['Accept-Encoding'])
#


# ==================== PUT =========================

# d = {
# 	'login': 'my_login',
# 	'password': 'my_password'
# }
#
# # r = requests.put('https://httpbin.org/put', data=d)
#
# r = requests.put('https://httpbin.org/put?page=page1', params={'key': 'value', 'key1': 'value2'}, data=d)
# # print('put_text :', r.text)
# print(json.dumps(r.json(), indent=4))
# print('url :', r.url)
# print('get_json :', r.json())
# print('get_json_form :', r.json()['form'])




# ==================== DELETE ===================

# r = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
# r = requests.delete('https://httpbin.org/delete?page=page1', data={'login': 'my_login'})
# r = requests.delete('https://httpbin.org/delete', params={'page': 'page31'}, data={'login': 'my_login'})

# params = {
#     'key': "u2JnV5UpCmumAYaETsLxLUc7ctHM84bjazoehWO8HiwM"
# }
# r = requests.delete('https://httpbin.org/delete', params=params, data={'login': 'my_login'})
# print('delete_text :', r.text)
# print('url :', r.url)
# print(r.json())


###############################################################

########################################################
#        https://api.dictionaryapi.dev/api/v2/entries/en/
########################################################

# import requests
#
#
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
#######################################################


import requests

# for i in range(10):
#
#     url = "https://api.thecatapi.com/v1/images/search"
#
#     response = requests.get(url)
#     res_print = json.dumps(response.json(), indent=4)
#     # print(res_print)
# 	print(response.json()[0]["url"])
# url = "https://api.thecatapi.com/v1/images/search"
#
# response = requests.get(url)
# print(response.json()[0]["url"])


####################################################################
#### OIL PRICE #####################################################
####################################################################

# import requests
# import json
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
#


# # ####################### MONOBANK ###################

import requests
import datetime


# url = 'https://api.monobank.ua/bank/currency'
#
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
# print(r.json())
# print('продаж доллар США:', r.json()[0]['rateSell'])
# print('купівля доллар США:', r.json()[0]['rateBuy'])
# print('продаж EURO:', r.json()[1]['rateSell'])
# print('купівля EURO:', r.json()[1]['rateBuy'])


# res = r.json()
# for i in range(len(res)):
#     for key, vol in res[i].items():
#         print(key, ':', vol)
#     print('.'*80)

# # # -----------------------------------------------------
# response = r
# # print(*dir(response), sep='\n')
# # print(response.text)
#
# print(response.status_code)
# # print(response.json())
# # print('response.text      : ', type(response.text))
# # print('response.json()[0] : ', type(response.json()[0]))
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
# import requests
#
#
# url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#
# response = requests.get(url)
#
# print(response.status_code)
# res = response.json()
# print(type(res))
# # print(res)
# print(json.dumps(res, indent=4))

# print(res[0]['sale'])

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
# #     if res[i]['cc'] == 'PLN':
# #     if res[i]['cc'] == 'USD':
#     if res[i]['cc'] == 'GBP':
#         print(i)
# print('Курс  EUR:', res[38]['rate'])
# print('Курс  USD:', res[32]['rate'])
# print('Курс  Платина:', res[40]['rate'])
# print('Курс  Фунти стерлінгу:', res[31]['rate'])



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
#           # "q": input('Input city and country with "," : '),
#           "q": input('Input city : '),
#           }
#
# response = requests.get(url, params=params)
#
# print(response.url)
# print(response.status_code)
# # print(response.json())
# res = response.json()
# print('.'*80)
# res_print = json.dumps(res, indent=4)
# print(res_print)
# for key, vol in res.items():
#     print(key, '\t:', vol)
# print(f"The weather in {res['name']} :")
# w = res['weather'][0]
# t = res['main']
# print('main        :', w['main'])
# print('temperature :', int((t['temp']-273.15)*100)/100, chr(176)+'C')
# print('feels_like  :', int((t['feels_like']-273.15)*100)/100, chr(176)+'C')
# print('temp_min    :', int((t['temp_min']-273.15)*100)/100, chr(176)+'C')
# print('temp_max    :', int((t['temp_max']-273.15)*100)/100, chr(176)+'C')
# print('pressure    :', t['pressure'], 'MPa')
# print('description :', w['description'])
# print('visibility  :', str(res['visibility']/100) + '%')
# print('clouds      :', res['clouds']['all'], '%')
# print('wind :')
# print('\t', 'speed :', res['wind']['speed'])
# print('\t', 'deg   :', res['wind']['deg'])
# print('time      :', datetime.fromtimestamp(res['dt']))
# print('sunrise   :', datetime.fromtimestamp(res['sys']['sunrise']))
# print('sunset    :', datetime.fromtimestamp(res['sys']['sunset']))
# print('')


##################################### Ryanair #####################

import requests
import json
from datetime import datetime

# url = "https://ryanair2.p.rapidapi.com/api/v1/getActiveAirports"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "ryanair2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers)
#
# res = response.json()
# # print(json.dumps(response.json(), indent=4))
#
# print("date time :", res["timestamp"])
# # print(datetime.fromtimestamp(res["timestamp"]))
# data = res["data"]
# for d in data:
# 	print("code : ", d["code"])
# 	print("name : ", d["name"])
# 	print("city : ", d["city"]["name"])
# 	print("country : ", d["country"]["name"])
# 	print("schengen : ", d["country"]["schengen"])
# 	print('='*60)

##################################### Ryanair #####################
# Stockholm ARN
# Berlin Brandenburg BER
# Prague PRG

# import requests
#
# url = "https://ryanair2.p.rapidapi.com/api/v1/searchFlights"
#
# querystring = {"origin":"BER","destination":"PRG","outboundDate":"2026-06-23","adults":"1","teens":"0","children":"0","infants":"0"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "ryanair2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))

##################################### Ryanair #####################

#
# import requests
#
# url = "https://ryanair2.p.rapidapi.com/api/v1/getActiveAirports"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "ryanair2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers)
#
# res  = response.json()

# print(json.dumps(response.json(), indent=4))

# for air in res["data"]:
# 	print("code :", air["code"])
# 	print("name :", air["name"])
# 	print("country :", air["country"]["name"])
# 	print("schengen :", air["country"]["schengen"])
# 	print('='*80)

######################################################################

# import requests
#
# url = "https://ryanair2.p.rapidapi.com/api/v1/availabilityCalendar"
#
# querystring = {"origin":"ZAG","destination":"WAW","date":"2026-05-16","returnDate":"2026-05-23"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "ryanair2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
#
# print(json.dumps(response.json(), indent=4))



######################################################################

# import requests
#
# url = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/scheduled-events/2026-05-14"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "sportapi7.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers)
#
# # print(response.json())
#
#
# res = response.json()
# print('.'*80)
# res_print = json.dumps(res, indent=4)
# print(res_print)





################################################################

# import requests
#
# url = "https://meteostat.p.rapidapi.com/stations/normals"
#
# querystring = {"station":"10637","start":"1961","end":"1990"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "meteostat.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))
#
# res = response.json()
# y = []
# for i in res['data']:
#     y.append((i['tmax'] + i['tmin'])/2)
#
# plt.plot(y)
# plt.show()
################################################################

# import requests
#
# url = "https://meteostat.p.rapidapi.com/stations/hourly"
#
# querystring = {
#     "station":"10637",
#     "start":"2026-04-24",
#     "end":"2026-04-30",
#     "tz":"Europe/Berlin"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "meteostat.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
#
#
# res = response.json()
# result = json.dumps(res, indent=4)
# print(result)


# y = []
# for i in res['data']:
#     y.append(i['temp'])
#
# plt.plot(y)
# plt.show()

################################################################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
# querystring = {"query": input("City name :") ,"locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# res = response.json()
# # print(json.dumps(response.json(), indent=4))
# print()
# for id in res:
# 	print("id :", id["city"]["name"])
# 	print("id :", id["city"]["id"])
# 	print("="*60)

# Lviv 40e2d079-8646-11e6-9066-549f350fcb0c
# Strasbourg 40d90f52-8646-11e6-9066-549f350fcb0c
# id : Lviv
# id : 40e2d079-8646-11e6-9066-549f350fcb0c
# ============================================================
# id : Sokilnyky
# id : 2f397bf8-8208-45bf-8df7-d14b61fc8ee6
# id : Berlin Airport
# id : 42d5ccaf-d0dc-4381-bd1f-9b5b38862cca
# ============================================================
# id : Berlin
# id : 40d8f682-8646-11e6-9066-549f350fcb0c
############################  FLIXBUS  ####################################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/trips"
#
# querystring = {"from_id":"40e2d079-8646-11e6-9066-549f350fcb0c","to_id":"40d8f682-8646-11e6-9066-549f350fcb0c","date":"12.07.2026","adult":"1","search_by":"cities","children":"0","bikes":"0","currency":"EUR","locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))

############################  FLIXBUS  ####################################
# autocomplete
# import requests
#
# url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
# querystring = {"query": input("City : "),"locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
#
# print(json.dumps(response.json(), indent=4))


############################  FLIXBUS  ####################################
# import requests
#
# url = "https://flixbus2.p.rapidapi.com/schedule"
#
# querystring = {"station_id":"dcbac843-9603-11e6-9066-549f350fcb0c","date":"15.05.2026"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))

############################  FLIXBUS  ####################################

# import requests
#
# url = "https://flixbus2.p.rapidapi.com/trips"
#
# querystring = {"from_id":"40e2d079-8646-11e6-9066-549f350fcb0c","to_id":"40de1ad1-8646-11e6-9066-549f350fcb0c","date":"18.06.2026","adult":"1","search_by":"cities","children":"0","bikes":"0","currency":"EUR","locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))

############################  FLIXBUS  ####################################
import requests
#
# url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
# querystring = {
#     "query":input("Input city (en) :"),
#     "locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
#
# res = response.json()
# print(json.dumps(res, indent=4))
#
# length = len(res)
#
# for st in res:
#     print('=' * 60)
#     print(st["country"]["name"])
#     print(st["address"])
#     print(st["city"]["name"])
#     print(st["id"])



# ============================================================
# Ukraine
# Stryiska St 109
# Lviv
# dcc4c90f-9603-11e6-9066-549f350fcb0c
# ============================================================
# Ukraine
# Dvirtseva Sq. 1
# Lviv
# dcc4c815-9603-11e6-9066-549f350fcb0c
# ============================================================
# Ukraine
# 10 Sknylivska St.
# Sokilnyky
# bcac001a-665f-4324-934a-329839b2267d
# # ============================================================
# France
# Place de l'Étoile
# Strasbourg
# dcbac843-9603-11e6-9066-549f350fcb0c

# ============================================================
# France
# Gare Routière Roissypole
# Paris CDG Airport
# dcc05c30-9603-11e6-9066-549f350fcb0c
# ============================================================
# France
# Avenue du Général Leclerc (D910)
# Paris
# 7f6214cd-95d7-4bbf-8283-55af226fa33a
# ============================================================
# France
# Gare Routière de Saint-Denis - Université
# Paris
# 9dc244f1-63d4-4db1-afbd-a10cc0377464
# ============================================================
# France
# 210 Quai de Bercy
# Paris
# dcc5426b-9603-11e6-9066-549f350fcb0c
# ============================================================
# France
# 22 Boulevard Pershing
# Paris
# dcbd8ba2-9603-11e6-9066-549f350fcb0c
# ============================================================
# France
# 1 Rond-Point de la Défense
# Paris
# dcc19631-9603-11e6-9066-549f350fcb0c
# ============================================================
# France
# 66 Avenue des Grands Godets
# Paris
# 20fcedfd-e08f-4eef-8430-5d46431f473c
# ============================================================
# France
# Gare Routière Vilmorin
# Paris
# dcc0b0b8-9603-11e6-9066-549f350fcb0c
# ============================================================
# France
# Parking Cars de Groupe 4
# Paris Orly Airport
# bb8595cd-a014-44f8-a636-79c4eee67290
# ============================================================
# France
# Gare de Marne-la-Vallée Chessy Sud
# Disneyland Paris
# 4aee50c3-ad4b-4c61-8572-896e31e78b5f

#############################################
# import requests
#
# url = "https://flixbus2.p.rapidapi.com/schedule"
#
# querystring = {"station_id":"dcc4c90f-9603-11e6-9066-549f350fcb0c","date":"28.04.2026"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
#
# res = response.json()
# print(json.dumps(res, indent=4))

########################################################################
# import requests
#
# def get_id():
#     name_city = input("Input name of city (en) :")
#
#     url = "https://flixbus2.p.rapidapi.com/autocomplete"
#
#     querystring = {
#         "query": name_city,
#         "locale":"en"}
#
#     headers = {
#     	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
#     	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
#     	"Content-Type": "application/json"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)
#     res = response.json()
#     return res[0]["city"]["id"]
#
#
# url = "https://flixbus2.p.rapidapi.com/trips"
#
# querystring = {"from_id": get_id(),
#     "to_id": get_id(),
#     "date": input("Date (DD.MM.YYYY) :"),
#     "adult":"1",
#     "search_by":"cities",
#     "children":"0",
#     "bikes":"0",
#     "currency":"EUR",
#     "locale":"en"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "flixbus2.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
#
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
# # print(json.dumps(res, indent=4))
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
# ##############################################

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
# .............................
# import requests
#
# url = "https://footapi7.p.rapidapi.com/api/rankings/fifa"
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "footapi7.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers)
#
# # print(response.json())
#
# res = response.json()
# i = 0
# country = input('Введіть назву країни англійською (або ALL): ').lower()
# for el in res['rankings']:
#     i+=1
#     if el['team']['country']['name'].lower() == country or country == 'all':
#         print(i, ':', el['team']['name'], el['team']['country']['name'])


###########################################

#######################################
#### SPORT ############################
# #######################################
# import requests
#
# url = "https://sportscore1.p.rapidapi.com/sports/1/teams"
#
# querystring = {"page":"1"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "sportscore1.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())
#
# resp_print = json.dumps(response.json(), indent=4)
# print('resp_print : ', type(resp_print))
# print(resp_print)

#######################################
######################### BOOKING  #########################




# res = response.json()
# print(json.dumps(res, indent=4))


######################### BOOKING  #########################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
#
# querystring = {"query":"Strasbourg"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
#
# res = response.json()
# print(json.dumps(res, indent=4))
#


# -1471697  Strasbourg

######################### BOOKING  #########################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"
#
# querystring = {"dest_id":"-1471697","search_type":"CITY","arrival_date":"2026-05-22","departure_date":"2026-05-23","adults":"1","children_age":"0,17","room_qty":"1","page_number":"1","units":"metric","temperature_unit":"c","languagecode":"en-us","currency_code":"EUR","location":"US"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))

######################### BOOKING  #########################
# import requests
#
# url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/getHotelPhotos"
#
# querystring = {"hotel_id":"361449"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "booking-com15.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# #
# print(json.dumps(response.json(), indent=4))

######################### BOOKING  #########################

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
#                "checkin_date":"2026-06-19",
#                "checkout_date":"2026-06-20",
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
#



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
#                "arrival_date":"2026-06-10",
#                "departure_date":"2026-06-11",
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
#                "arrival_date":"2026-05-22",
#                "departure_date":"2026-05-23",
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
#

#######################################
#


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

#
# import requests
#
# url = "https://sky-scrapper.p.rapidapi.com/api/v1/hotels/searchHotels"
#
# querystring = {
#     "entityId":"27540983",
#     "checkin":"2026-05-29",
#     "checkout":"2026-05-30",
#     "adults":"1",
#     "rooms":"1",
#     "limit":"30",
#     "sorting":"-relevance",
#     "currency":"USD",
#     "market":"en-US",
#     "countryCode":"US"}
#
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# # print(response.json())
# print(json.dumps(response.json(), indent=4))
#



#######################################
### POPULATION ########################
#######################################

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
# # # # #
#




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
# import requests
#
#
# def detect(text):
# 	url = "https://google-translator9.p.rapidapi.com/v2/detect"
#
# 	payload = {"q": text}
# 	headers = {
# 		"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 		"x-rapidapi-host": "google-translator9.p.rapidapi.com",
# 		"Content-Type": "application/json"
# 	}
#
# 	response = requests.post(url, json=payload, headers=headers)
#
# 	print(response.json())
# 	return  response.json()["data"]["detections"][0][0]["language"]
#
#
#
# with open('source.txt', 'r', encoding='utf-8-sig') as f1:
#     source = f1.read()
#
# s = detect(source)
#
# url = "https://google-translator9.p.rapidapi.com/v2"
#
# payload = {
# 	"source": s,
# 	"target": "en",
#     "q": source,
# 	"format": "text"
# }
# headers = {
# 	"x-rapidapi-key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
# 	"x-rapidapi-host": "google-translator9.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# # print(response.json())
# # print(json.dumps(response.json(), indent=4))
# # print()
# print(response.json()["data"]["translations"][0]["translatedText"])
# target = response.json()["data"]["translations"][0]["translatedText"]
#
# with open('target.txt', 'w') as f2:
#     f2.write(target)

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
# # print(json.dumps(data, indent=4))
#
# latitude = data['loc'].split(',')[0]
# longitude = data['loc'].split(',')[1]
# print('longitude :', longitude)
# print('latitude  :', latitude)
# print('city      :', data['city'])

####################################################

################################################################


import requests


url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"

querystring = {
	# "query":"wsgr.com",
	"query":"duan.edu.ua",
	# "query":"lpnu.ua",
	# "query":input('Input URL : '),
	"match_email_domain":"false",
	"external_matching":"false"}

headers = {
	"X-RapidAPI-Key": "36eb7185f9msh45f7c7652f43036p1fc15fjsn3383c6123fe6",
	"X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# print(response.json())
# print(json.dumps(response.json(), indent=4))
#
# # # # #################### duan.edu.ua
result = []
for email in response.json()['data'][0]['emails']:
	# print('email :', email['value'])
	result.append(email['value'])
result.sort()
for i in result:
	print('email : ', i)


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
#     url = f"http://riv3.pythonanywhere.com/api/v3/book/?page={i}"
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







