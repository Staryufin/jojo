#import random


#def print_Treygolnik():
    #from random import randint
    #a=random.randint(0,100)
    #b=random.randint(0,100)
    #c=random.randint(0,100)
    #if c<(a+b) and a<(c+b) and b<(a+c):
        #print("Треугольник существует")
    #else:
        #print("Треугольник не существует")


#print_Treygolnik()


def print_figura():
    figura = input("Введите фигуру: ")
    def print_Rectangle():
        a = int(input("Ведите длинну прямоугольника: "))
        h = int(input("Введите ширину прямоуголиника: "))
        W = a*h
        print("Площадь прямоугольника: " ,W)
    def print_Traingle():
        b = int(input("Ведите высоту треугольника: "))
        q = int(input("Введите ширину треугольника: "))
        I = (b*q)/2
        print("Площадь треугольника:" ,I)
    def print_Cicle():
        a = int(input("Ведите длинну: "))
        r = int(input("Введите радиус: "))
        S = a*(r**2)
        print("Площадь круга:" ,S)
    if figura =="1":
        print_Rectangle()
    if figura =="2":
        print_Traingle()
    if figura == "3":
        print_Cicle()



def print_1():
    a = [1,1,2,3,4,5,8,13,21,34,55,89]
    i = 0
    while i<5:
        item = a[i]
        print(item)
        i +=1

def print_2():
    a = [1,1,2,3,4,5,8,13,21,34,55,89]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c = []
