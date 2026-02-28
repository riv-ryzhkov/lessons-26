##############################################################
############ Лінійний пошук ##################################
from requests.packages import target


# Часова складність: O(n),
# де n - кількість елементів у списку.

# def linear_search1(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
#
# def linear_search2(arr, target):
#     counter = 1
#     for i, num in enumerate(arr):
#         if num == target:
#             return i, counter
#         counter += 1
#     return -1, counter
#
#
#
# arr = [i for i in range(1000)]
# target = 523
# print(linear_search1(arr, target))


##############################################################
###################### Бінарний пошук
##############################################################


# Бінарний пошук працює з відсортованим масивом,
# ділить його навпіл та порівнює шуканий елемент з серединою.
# Часова складність: O(log n), де n - кількість елементів у відсортованому масиві.


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     count = 0
#     while left <= right:
#         count += 1
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid, count
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1, count
#
#
#
# arr = [i for i in range(300)]
# target = 53
# print(binary_search(arr, target))
#


#
# import random
#
#
# l1 = [i for i in range(800000, 2)]
#
# # print(l1)
# print(binary_search(l1, 399999))
#
#

##########################################################
##########################################################
