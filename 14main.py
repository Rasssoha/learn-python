from operator import index
from xml.dom.minidom import Element

def accum(s):
    letter_list = list(s)
    index_number = 0
    for letter in letter_list:
        index_number = index_number + 1
        for i in range(index_number):
            print(letter)

accum("teueu")

