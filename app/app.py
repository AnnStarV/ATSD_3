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


class GreedyAlg:
    ItKey = 0;
    members = {}

    def get_sort_price(self):
        N = len(self.members)

        for i in range(0, N):
            for j in range(0, N - i - 1):
                if self.members[j][3] < self.members[j + 1][3]:
                    self.members[j], self.members[j + 1] = self.members[j + 1], self.members[j]

    def sort_ar(self):
        check = True
        N = len(self.members)
        arr = []
        arrOfDate = []
        arr.append(self.members[0])
        for i in range(0, len(self.if_in_date(self.members[0]))):
            arrOfDate.append((self.if_in_date(self.members[0]))[i])

        for i in range(1, N):
            for j in range(0, len(self.if_in_date(self.members[i]))):
                if (self.if_in_date(self.members[i]))[j] in arrOfDate:
                    check = False
            if check:
                for k in range(0, len(self.if_in_date(self.members[i]))):
                    arrOfDate.append((self.if_in_date(self.members[i]))[k])
                arr.append(self.members[i])
            check = True
        return arr

    def if_in_date(self, el):
        temp = [list((pd.date_range(el[1], el[2], freq="D")).date)]
        return temp[0]

    def add_new(self, key, array):
        self.members[key] = array

    def edit(self, key, val):
        for i in range(0, len(self.members)):
            if i == key:
                self.members[i][3] = val
                return

    def delete(self, key):
        self.members.pop(key, None)


#
# get_sort_price(members)
# for k in range(0, len(members)):
#     print(members[k])
#
#
# print("*********************************")
# sort_ar(members)

new = GreedyAlg()

for i in range(len(members)):
    new.add_new(i, members[i])



new.get_sort_price()

print(new.members)
print("***************************")
print(new.sort_ar())