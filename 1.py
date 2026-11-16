# pb = requests.get(     "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5" ).json()  # Монобанк mb = requests.get(     "https://api.monobank.ua/bank/currency" ).json()  usd_buy_pb = usd_sale_pb = eur_buy_pb = eur_sale_pb = "" for item in pb:     if item["ccy"] == "USD":         usd_buy_pb = item["buy"]         usd_sale_pb = item["sale"]     if item["ccy"] == "EUR":         eur_buy_pb = item["buy"]         eur_sale_pb = item["sale"]  usd_buy_mb = usd_sale_mb = eur_buy_mb = eur_sale_mb = "" for item in mb:     if item.get("currencyCodeA") == 840 and item.get("currencyCodeB") == 980:         usd_buy_mb = item.get("rateBuy", "-")         usd_sale_mb = item.get("rateSell", "-")     if item.get("currencyCodeA") == 978 and item.get("currencyCodeB") == 980:         eur_buy_mb = item.get("rateBuy", "-")         eur_sale_mb = item.get("rateSell", "-")  print("-" * 55) print("| Валюта    | ПриватБанк | Монобанк |") print("-" * 55) print(f"| USD sale  | {usd_sale_pb} | {usd_sale_mb} |") print(f"| USD buy   | {usd_buy_pb} | {usd_buy_mb} |") print(f"| EUR sale  | {eur_sale_pb} | {eur_sale_mb} |") print(f"| EUR buy   | {eur_buy_pb} | {eur_buy_mb} |") print("-" * 55)


# print("Hello".center(40))

# res = [1, 0, 1, 1, 0]
# v2 = [0,0,0,0,0]
# for i in range(2) :
#     for j in range(len(res)) :
#         p = j-1
#         if p < 0 :
#             p = len(res)-1
#         s = j+1
#         if s >= len(res) :
#             s = 0
#         v2[j] = (res[p] + res[s]) % 2
#         print(j, v2[j])
#         print("res=", res, "v2=", v2)
#     res,v2 = v2,res
#     print("+res=", res, "v2=", v2)
# print(res)

# n = int(input("n="))
# for a in range(1, n + 1):
#     for b in range(a + 1, n + 1):
#         c2 = a * a + b * b
#         c = 1
#         while c * c < c2:
#             c += 1
#         if c * c == c2 and c <= n:
#             print(a, b, c)


# n = int(input("Donnez la borne maximale : "))
# for a in range(1, n + 1):
#     for b in range(a + 1, n + 1):
#         c2 = a * a + b * b
#         c = 1
#         while c * c < c2:
#             c = c + 1
#         if c * c == c2 and c <= n:
#             print(a, b, c)

# nbrs = [7, 3, 4]
# tot = 0
# for i in range(0, len(nbrs)):
#     tot = tot + nbrs[i]
#
# si = 0
# i = 0
# while si < tot - si:
#     si = si + nbrs[i]
#     i = i + 1
#
# print(i - 1)

# def find_smallest_index(nbrs):
#     # Если список пуст, по условию возвращаем -1
#     if not nbrs:
#         return -1
#
#     total_sum = sum(nbrs)
#     left_sum = 0
#
#     # Перебираем возможные индексы i от 0 до len(nbrs) - 1
#     for i in range(len(nbrs)):
#         right_sum = total_sum - left_sum
#
#         # Если левая сумма строго меньше правой суммы
#         if left_sum < right_sum:
#             return i
#
#         left_sum += nbrs[i]
#
#     return -1
#
#
# # Пример из условия:
# nbrs = [7, 3, 4]
# print("Индекс i:", find_smallest_index(nbrs))

#############################################
# n = 40
# res = 0
# while n != 8 and n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
#     res = res + 1
# print(res)

############
# n = int(input("Donnez la borne maximale : "))
# for a in range(1, n + 1):
#     for b in range(a + 1, n + 1):
#         c2 = a * a + b * b
#         c = 1
#         while c * c < c2:
#             c = c + 1
#         if c * c == c2 and c <= n:
#             print(a, b, c)

############
# def find_split_index(nbrs):
#     if not nbrs:
#         return -1
#
#     tot = 0
#     for i in range(0, len(nbrs)):
#         tot = tot + nbrs[i]
#
#     s1 = 0
#     i = 0
#     while s1 < tot - s1:
#         s1 = s1 + nbrs[i]
#         i = i + 1
#
#     return i - 1
#
#
# # Проверка для примера nbrs = [7, 3, 4]
# nbrs = [7, 3, 4]
# print("Индекс i:", find_split_index(nbrs))  # Выведет 0


import random

res = [i*3 + random.randint(0,3) for i in range(10)]
print(res)