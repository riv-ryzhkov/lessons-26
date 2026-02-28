
# GET - получение
# POST - создание(получение авторизированной информации)
# PUT - обновление
# DELETE - удаление


#       pip install requests
#
import requests
import json


# response = requests.get('http://127.0.0.1:8000/api/url/')
# response = requests.get('http://127.0.0.1:8000/users/')

# town = input('Введите город : ')
# data = {'q': town, 'units': 'metric', 'APPID':'b18eeec4ac22e23cfd6a45375dd0cf90'}
# # response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90')
# response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=data)


# print(response.status_code)
# # res_text = response.text
# # print(res_text)
#
# res_json = response.json()
# # print(json.dumps(res_json, indent=4))
# city = res_json['name']
# ceil = res_json['weather'][0]['main']
# temp = res_json['main']['temp']
#
#
# print('=' * 80)
# print('Погода в городе', city)
# print('Небо :', ceil)
# print('Температура :', temp)
# print('=' * 80)

# print(res_json['weather'][0]['main'])
# print(type(res_json['weather'][0]['main']))
# print(*dir(response), sep='\n')



# print(response.text)
# print(response.json())
# text = json.dumps(response.json(), indent=4)
# # text = json.dumps(response.json())
# print(text)
# print('=' * 80)
# print(response.json()['weather'])
# print(response.json()['weather'][0]['main'])
# print(response.json()['weather'][0]['description'])
# print(response.json()['main']["feels_like"])

# for i in response.json():
#     w = json.dumps(i, indent=4)
#     print(w)


# print(*dir(response), sep='\n')
# inx = response.url.find('/', 8)
# print(inx)
# host_url = response.url[:inx+1]
# short_url = response.url[inx+1:]
# print(host_url)
# print(short_url)
# breakpoint()


# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Rome&units=metric&APPID=b18eeec4ac22e23cfd6a45375dd0cf90', timeout=3)
# #
# # print(r)
# #
# # # print(*dir(r))
# # # print(*dir(r), sep='\n')
# print(r.url)
# # print(r.status_code)
# print('status :', r.status_code)
# print(r.text)
# # print(type(r))
# print(type(r.text))
# # print(r.text[68:73])
# # # print(type(r.text))
# # # print(r.text[90:99])
# print(type(r.json()), r.json())
# print(r.json()['weather'][0]['main'])
# print(r.json()['weather'][0]['description'])

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# r = requests.get('https://api.github.com/events', timeout=3)


# print('status :', r.status_code)
# print('headers :', r.headers)
# print('type-headers :', type(r.headers))
# # print(*dir(r.headers), sep='\n')
# print('Server :', r.headers['Server'])
# print('Date', r.headers['Date'])
#
# for key, val in r.headers.items():
#     print(key, ':', val)


# for key, val in r.headers.items():
#     print(key, ':', val)

# print(*dir(r), sep='\n')
# print(type(r.text))
# print(r.text)
# print(r.text[54:62])

# print('get_text :', r.text[8:19]) # 19255650776
# print(type(r.json()))

# print('get_json :', type(r.json()), *r.json(), sep='\n')
# print('get_json :', type(r.json()[3]), r.json()[3])
#
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
# print('get_json :', r.json()[0])
# print(r.json()[0]['type'])
# print('get_json :', r.json()[0]['id'])
# print('get_json :', r.json()[0]['type'])



# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
#
# r = requests.get('https://httpbin.org/get', params=payload)
#
# # print(isinstance(r.json(), dict))
# # print(type(r.json())==dict)
#
# print(r.url)

# r = requests.get("https://httpbin.org/get?key1=value1&key2=value2&key2=value3")
# print('url :', r.url)
# print(type(r.json()))
# print(type(r.text))
# print(r.text)
#
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




# ======================== POST ===================
# data = {'key': 'value', 'key1': 'value1'}
# r = requests.post('https://httpbin.org/post', data=data)
#
# # r = requests.post('https://httpbin.org/post?page=page1', data=data)
# # #
# print(r.url)
# print('type :', type(r.text))
# print('post_text :', r.text)
# #
# print('type-json', type(r.json()))
# print('json', r.json())
# print(json.dumps(r.json(), indent=4))
# # # # #
# # #
# print('get_json :', r.json())
# # print('type :', type(r.json()))
# # print('inst :', isinstance(response.json(), dict))
# print('get_json_form :', r.json()['form'])
# print('get_json_headers :', r.json()['headers'])
# print('get_json_headers_Accept :', r.json()['headers']['Accept-Encoding'])



# ==================== PUT =========================
# d = {'key': 'value', 'key1': 'value2'}
# r = requests.put('https://httpbin.org/put', data=d)
# # r = requests.put('https://httpbin.org/put?page=page1', data={'key': 'value', 'key1': 'value2'})
# # print('put_text :', r.text)
# print(json.dumps(r.json(), indent=4))
# print('url :', r.url)
# print('get_json :', r.json())
# print('get_json_form :', r.json()['form'])

# ==================== DELETE ===================
# r = requests.delete('https://httpbin.org/delete', data={'key': 'value'})
# # r = requests.delete('https://httpbin.org/delete?page=page1', data={'key': 'value'})
# print('delete_text :', r.text)
# print('url :', r.url)
# print(r.json())
# breakpoint()

# params = {
#     'key': "u2JnV5UpCmumAYaETsLxLUc7ctHM84bjazoehWO8HiwM"
# }

####################################################################
#### OIL PRICE #####################################################
####################################################################

# import requests
# import json
#
#
# url = 'https://api.oilpriceapi.com/v1/prices/latest'
# headers = {
#   'Authorization': 'Token 96b90c2a2bf598680d40989ab38d54ea',
#   'Content-Type': 'application/json'
# }
#
# response = requests.get(url=url, headers=headers)
# print('url :', response.url)
# # print(*dir(response), sep='\n')
# # print('type-headers :', type(response.headers))
# # for key, vol in response.headers.items():
# #     print(key, ':', vol)
# # print('.'*80)
# print('type-json :', type(response.json()))
# # print('json :', response.json())
# res = response.json()
# print(json.dumps(res, indent=4))
# print('Price of oil is :', res['data']['price']*1.02, '$USA')

#

# # ####################### MONOBANK ###################
import requests
import datetime


# url = 'https://api.monobank.ua/bank/currency'
#
# response = requests.get(url)
# # # response = requests.get('https://api.monobank.ua/bank/currency')
# res = response.json()
# print(json.dumps(res, indent=4))
# print(response.json())

# currencyCodeA	980  гривня
# currencyCodeB	840  долл США
# currencyCodeA	978  євро



# response = requests.get(url)
# print(response.json())

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
#
# #
# response = requests.get(url)
# # print(*dir(response), sep='\n')
# print(response.text)
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


#!!!!!!!!!!!!!!!!!!!!!!
##########################################################
################### PRIVAT BANK#####################
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
# # print(res[0]['sale'])
# # for i in res:
# #     print(json.dumps(i, indent=4))
# for i in res:
#     print('.'*80)
#     for key, vol in i.items():
#         print(key, ':', vol)
# print('='*80)

########################################################
#                             NBU
# import requests
#
#
# url_nbu = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
#
# responce = requests.get(url_nbu)
#
# res = responce.json()
# # result = json.dumps(res, indent=4)
# # print(result)
# # for i in range(len(res)):
# # #     # print(res[i])
# # #     # breakpoint()
# #     if res[i]['cc'] == 'USD':
# #         print(i)
# print('Курс  EUR:', res[31]['rate'])
# print('Курс  USD:', res[24]['rate'])


########################################################



# ++++++++++++++++ VERONIKA ++++++++++++++++++++++++
