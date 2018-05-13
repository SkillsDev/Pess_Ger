#!usr/bin/python
import random

def startrand(l,l2,n):
    return l + l2 + n

def radermize():
    arq = open('worlist', 'r')
    text = arq.read()
    lr = random.choices(text)
    lr2 = random.choices(text)
    lr3 = random.choices(text)
    cc = arq.close()
    return str(lr + lr2 + lr3)



