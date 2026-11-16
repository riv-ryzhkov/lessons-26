# import requests
#
#
# url_pr = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
# url_mono = 'https://api.monobank.ua/bank/currency'
#
# privat = requests.get(url_pr)
# mono = requests.get(url_mono)
#
# print('*'*50)
# print('|                   | МОНОБАНК \t| ПРИВАТБАНК   \t|')
# print('-'*50)
# print('| EURO      продаж  |', mono.json()[1]['rateSell'], '\t|', privat.json()[1]['sale'], '\t    |')
# print('| EURO     купівля  |', mono.json()[1]['rateBuy'], '\t|', privat.json()[1]['buy'], '\t    |')
# print('.'*50)
# print('| DOLL USA  продаж  |', mono.json()[0]['rateSell'], '\t|', privat.json()[0]['sale'], '\t    |')
# print('| DOLL USA купівля  |', mono.json()[0]['rateBuy'], '\t|', privat.json()[0]['buy'], '\t    |')
#
# print('*'*50)














