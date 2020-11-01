import datetime

members = {
    'first': ('2020/11/01', '2020/11/03', 1000),
    'second': ('2020/11/02', '2020/11/04', 1200),
    'third': ('2020/11/05', '2020/11/07', 1300),
    'fourth': ('2020/11/07', '2020/11/09', 800),
    'fifth': ('2020/11/08', '2020/11/10', 2000),
    'sixth': ('2020/11/11', '2020/11/13', 1700),
    'seventh': ('2020/11/14', '2020/11/16', 1600),
    'eighth': ('2020/11/17', '2020/11/20', 1500),
    'ninth': ('2020/11/19', '2020/11/23', 1250),
    'tenth': ('2020/11/24', '2020/11/27', 1900)
}


def date_diff(first, second):
    first = first.split('/')
    second = second.split('/')
    first = datetime.date(int(first[0]), int(first[1]), int(first[2]))
    second = datetime.date(int(second[0]), int(second[1]), int(second[2]))
    diff = first - second

    return diff.days


def get_days_and_money(members):
    days = [date_diff(members[item][1], members[item][0]) for item in members]
    money = [members[item][2] for item in members]
    return days, money


print(get_days_and_money(members))
