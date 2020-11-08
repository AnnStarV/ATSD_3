import datetime
import pandas as pd
import eel
import heapq
from collections import Counter
from collections import namedtuple

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

    def add_new(self, array):
        self.members[self.ItKey] = array
        self.ItKey += 1

    def edit(self, key, val):
        upd = {key: (self.members[key][0], self.members[key][1], self.members[key][2], val)}
        for i in range(0, len(self.members)):
            if i == int(key):
                self.members.update(upd)
                return

    def delete(self, key):
        self.members.pop(key)

    def print(self):
        arr = ""
        for key, value in self.members.items():
            arr += (str(key) + ' is key of' + str(value) + '\n')
        return arr


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


class Haffman:
    def huffman_decode(self, encoded, code):
        sx = []
        enc_ch = ""
        for ch in encoded:
            enc_ch += ch
            for dec_ch in code:
                if code.get(dec_ch) == enc_ch:
                    sx.append(dec_ch)
                    enc_ch = ""
                    break
        return "".join(sx)

    def huffman_encode(self, s):
        h = []
        for ch, freq in Counter(s).items():
            h.append((freq, len(h), Leaf(ch)))
        heapq.heapify(h)
        count = len(h)
        while len(h) > 1:
            freq1, _count1, left = heapq.heappop(h)
            freq2, _count2, right = heapq.heappop(h)
            heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

            count += 1
        code = {}
        if h:
            [(_freq, _count, root)] = h
            root.walk(code, "")
        return code



new = GreedyAlg()
for i in range(len(members)):
    new.add_new(members[i])

text = open("1.txt")
data = text.read()
newHaff = Haffman()


@eel.expose
def print_members():
    return new.print()


@eel.expose
def haff_text():
    return data


@eel.expose
def add_el(name, start, end, money):
    new.add_new((str(name), str(start), str(end), money))
    return new.print()


@eel.expose
def change_el(key, val):
    new.edit(int(key), int(val))
    return new.print()


@eel.expose
def del_el(del_el_key):
    new.delete(int(del_el_key))
    return new.print()


@eel.expose
def greedy():
    new.get_sort_price()
    result = ""
    arr = new.sort_ar()
    for i in range(len(arr)):
        result += str(arr[i]) + "\n"
    return result

@eel.expose
def encoding():
    code = newHaff.huffman_encode(data)
    encoded = "".join(code[ch] for ch in data)
    return encoded

@eel.expose
def decoding():
    code = newHaff.huffman_encode(data)
    encoded = "".join(code[ch] for ch in data)
    return newHaff.huffman_decode(encoded, code)

eel.init("web")
eel.start("index.html", size=(1000, 900))
