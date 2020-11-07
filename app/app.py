import datetime
import pandas as pd

members = {
    0: ('laser', '2020/11/01', '2020/11/03', 1000),
    1: ('snatch', '2020/11/02', '2020/11/04', 1200),
    2: ('figure', '2020/11/05', '2020/11/07', 1300),
    3: ('vegetation', '2020/11/07', '2020/11/09', 800),
    4: ('smell', '2020/11/08', '2020/11/10', 2000),
    5: ('energy', '2020/11/11', '2020/11/13', 1700),
    6: ('spray', '2020/11/14', '2020/11/16', 1600),
    7: ('meadow', '2020/11/17', '2020/11/20', 1500),
    8: ('sensation', '2020/11/19', '2020/11/23', 1250),
    9: ('slime', '2020/11/24', '2020/11/27', 1900)
}


def date_diff(first, second):
    first = first.split('/')
    second = second.split('/')
    first = datetime.date(int(first[1]), int(first[2]), int(first[3]))
    second = datetime.date(int(second[1]), int(second[2]), int(second[3]))
    diff = first - second

    return diff.days


def get_days_and_money(members):
    days = [date_diff(members[item][2], members[item][1]) for item in members]
    money = [members[item][3] for item in members]
    return days, money


def get_sort_price(members):
    N = len(members)
    # for i in range(0, N - 1):
    #     print(members[i])
    for i in range(0, N):
        for j in range(0, N - i-1):
            if members[j][3] < members[j + 1][3]:
                members[j], members[j + 1] = members[j + 1], members[j]


def sort_ar(members):
    check = True
    N = len(members)
    arr = []
    arrOfDate = []
    arr.append(members[0])
    for i in range(0, len(if_in_date(members[0]))):
        arrOfDate.append((if_in_date(members[0]))[i])

    for i in range(1, N):
        for j in range(0, len(if_in_date(members[i]))):
            if (if_in_date(members[i]))[j] in arrOfDate:
                check = False
        if check:
            for k in range(0, len(if_in_date(members[i]))):
                arrOfDate.append((if_in_date(members[i]))[k])
            arr.append(members[i])
        check = True

    for k in range(0, len(arr)):
        print(arr[k])
    # print(arrOfDate)


def if_in_date(el):
    temp = [list((pd.date_range(el[1], el[2], freq="D")).date)]
    return temp[0]

def add_new(members, key, array):
    members[key] = array

def edit(members, key, val):
   for i in range(0, len(members)):
       if i == key:
           members[i][3] = val
           return

def delete(members, key):
    members.pop(key)

#
# get_sort_price(members)
# for k in range(0, len(members)):
#     print(members[k])
#
#
# print("*********************************")
# sort_ar(members)

print(type(members))

print(members)
