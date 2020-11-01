members = {
    'first': ('01/11/2020', '05/11/2020', 1000),
    'second': ('03/11/2020', '07/11/2020', 1200),
    'third': ('08/11/2020', '11/11/2020', 1300),
    'fourth': ('12/11/2020', '15/11/2020', 800),
    'fifth': ('16/11/2020', '19/11/2020', 2000),
    'sixth': ('20/11/2020', '22/11/2020', 1700),
    'seventh': ('23/11/2020', '26/11/2020', 1600),
    'eighth': ('25/11/2020', '28/11/2020', 1500),
    'ninth': ('26/11/2020', '30/11/2020', 1250),
    'tenth': ('27/11/2020', '31/11/2020', 1900)
}


def get_days_and_money(part):
    days = [part[item][1] - part[item][0] for item in part]
    money = [part[item][2] for item in part]
    print("days")
    return days, money


get_days_and_money(members)
