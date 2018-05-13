#!usr/bin/python
import wordlisser

def inicio():

    print('''
            
            |0000000|                      |0000000000|    |0000000000|
            |00000000|       ____          |0000|          |0000|
            |00000000/      /0000\         |0000|          |0000|
            |0000000/      /000000\        |0000000000|    |0000000000|
            |000|         /00|  |00\             |0000|          |0000|
            |000|        /0000000000\            |0000|          |0000|
            |000|       /0000|   |000\     |0000000000|     |000000000|   ____  G E R 
        
        M A X   S  E C U R I T Y
        
        
            By : #Root$
            
        ''')

    l = str(input('Type any caracter : '))
    l2 = (str(input('Type Special caracter : ')))
    n = (input('Type Natural number : '))
    ler = [l]
    ler2 = [l2]
    ler3 = [n]
    ran1 = wordlisser.startrand(ler,ler2,ler3)
    rand2 = wordlisser.radermize()
    f = str(ran1)
    f2 = str(rand2)
    rr = f + f2
    fnrr = '!'.join(rr).strip('[]')
    print('\nYour password -> {}'.format(str(fnrr)))
    print('\nyou can discard the (''), (,) and the ([]) or just use all of them in passwords !')
    print('\nYou can personalize your Password !')
    print('\nYou can use the five first caracters or all caracters\nthe choice is your')


inicio()








