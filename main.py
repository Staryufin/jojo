#print (2 ** 3)
#user_name = "Настя"
#user_age = 20
#print (f"Имя:{user_name},возраст: {user_age})")
#print("при" + "вет")
##сюда писать пометки для прочтения кода
#number = 56
#string = "Строка"
#boolean = True
#print(type(number)) #<class `int`>
#print(type(string)) #<class `str`>
#print(type(boolean)) #<clacc `bool`>
import random

import message
#print(a,'+', b, '=', a+b)
#print(a,'-', b, '=', a-b)
#print(a,'/',b, '=', 6/2)
#print(a,'**',b, '=', 6**2)
#print(a,'//',b,'=',6//2)
#print(-a,'+',b,'=', -6+2)


# pass1 = input()
#pass2 = input()
#if pass1 == pass2:
#    print("пароль совпадает")
#print("End")
#z = int(input())
#if -1<z<17:
#    print("попадает")
#else:
#    print("не попадает")
#print("End")

#a=int(input())
#if 0!=a:
    #if a<10:
        #print("одна цифра")
    #elif a<100:
        #print("две цифры")
    #elif a<1000:
        #print("три цифры")
    #elif a<10000:
        #print("четыре цифры")
#else:
    #print("число равно нолю")

##адача про существующий треуг. или несуществующий треуг.
#a=int(input())
#b=int(input())
#c=int(input())
#if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    #print("Yes")
#else:
    #print("No")

#language = "russian"
#daytime = "morning"
#if language == "english":
    #if daytime == "morning":
        #print("Good morning")
    #else:
        #print("Good evening")
#else:
    #if daytime == "morning":
        #print("Доброе утро")
    #else:
        #print("Добрый вечер")




#z = int(input())
#x = int(input())
#c = int(input())
#sum=0
#if(z<0):
    #z=0
#if(x<0):
    #x=0
#if(c<0):
    #c=0
#sum = z+x+c
#print(sum)




#city = input("В каком городе вы живете?: ")
#if city == "Москва" or city == "Ростов" or city == "Сочи":
    #print("Доступ разрешен")
#else:
    #print("Доступ запрещен")

#age = int(input("Сколько вам лет?: "))
#grade = int(input("В каком классе вы учитесь?: "))
#if age >= 12 and grade >= 7:
    #print("Доступ разрешен")
#else:
    #print("Доступ запрещен")

#age = int(input("Сколько вам лет?: "))
#if age >= 12:
    #print("Доступ разрешен")
#else:
    #print("Доступ запрещен")

#Задача1
#a, b, c, = int(input()), int(input()), int(input())
#if a == b:
    #if b == c:
        #print(3)
    #else:
        #print(2)
#else:
    #if a == c:
        #print(2)
    #else:
        #if b == c:
            #print(2)
        #else:
            #print(0)
#2ой способ решения
#a, b, c, = int(input()), int(input()), int(input())
#if a == b == c:
    #print(3)
#elif a == b != c:
    #print(2)
#elif a != b == c:
    #print(2)
#elif a == c != b:
    #print(2)
#else:
    #print(0)

#3 способ
#a, b, c, = int(input()), int(input()), int(input())
#if a == b == c:
    #print(3)
#elif a == b != c or a != b ==c or a == c != b:
    #print(2)
#else:
    #print(0)


#2я задача
#x = int(input())
#y = int(input())
#if x>0 and y>0:
    #print("Первая координатная четверть")
#if x<0 and y>0:
    #print("Вторая координатная четверть")
#if x<0 and y<0:
    #print("Третья координатная четверть")
#if x>0 and y<0:
    #print("Четвертая координатная четверть")

#3я задача
#a = int(input())
#if a%100==0:
    #print("Yes")

#4я задача
#a = int(input())
#if a==0 or a<1 or a>10:
    #print('Eror')
#elif a==1:
    #print("I")
#elif a==2:
    #print('II')
#elif a==3:
    #print('III')
#elif a==4:
    #print('IV')
#elif a==5:
    #print('V')
#elif a==6:
    #print('VI')
#elif a==7:
    #print('VII')
#elif a==8:
    #print('VIII')
#elif a==9:
    #print('IX')
#elif a==10:
    #print('X')
#else:
    #print('End')

#5я задача
#a = int(input())
#if 2<=a<=5 or a%2==0:
    #print("No")
#elif 6<a<20 or a%3!=1:
    #print("Yes")

#6я задача
#a = int(input('a =: '))
#b = int(input('b =: '))
#c = int(input('c =: '))
#if a<b<c or c<b<a:
    #print('b')
#elif a<c<b or b<a<c:
    #print('c')
#elif b<a<c or c<a<b:
    #print('a')


#№
#a = 1
#while a < 5:
    #print(f"Число{str(a)}")
    #a += 1
    #print(f"Результат:{str(a)}")

#№
#a = 1
#while a < 7:
    #if a%3==0:
        #print(f"Делится:{str(a)}")
    #else:
        #print(f"Не делится:{str(a)}")
    #a += 1

#№3
#i = 3
#while i>=0:
    #print(i)
    #i-=1

#Continue
#z = 0
#while z <5:
    #z+=1
    #if z == 3:
        #continue
    #print(f"Число:{str(z)}")

#Break
#x = 0
#while x <5:
    #x += 1
    #if x == 3:
        #break
    #print(f"Число:{str(x)}")

#num = 0
#while True:
    #num += 1
    #print(num)

#№1.1
#a = 0
#while a<100:
    #a+=1
    #print(a)

#№1.2
#a = 0
#while a<=100:      #или a<101
    #if a%5==0:
        #print(f"Число:*{str(a)}*")
    #else:
        #print(a,end=" ")
    #a+=1

#№2
#a = str(input())
#while a!="Конец":
    #print(a)
    #a=input()

#№3
#a = int(input())
#while 2 % 2 == 0 and a % 7 == 0:
    #print(f"Число{str(a)}")
    #a=int(input())
#else:
    #print("Ошибка")

#Total = 0
#a = int(input())
#while a>=0:
   #Total += a
   #print(a)
   #a=int(input())
#print(Total)



#Списки в Pyton

#values = ["A",2,True,None,[],-99.45]

#values = [
#    "a",2,True,-999,
#    None,"\n\t","",
#    -42,"Список",False
#]
#print(values)

#['A',2,True,-999,None,'\n\t',"",-42,'Список',False]

#number = [1,2,3,4,5,6]
#people = ["Tom","Sam","Bob"]
#to_buy = ["хлеб","кабачки","масло","молоко",]
#num = number[3]#4
#print(people[-2])#Sam
#print(to_buy[5])#ошибка

#values = [
#    [1,2,3],
#    ["a","b","c"],
#    [True,False,True]
#]
#print(values[0][1])
#print(values[-2][2])


#items = ["яблоки","кабачки","груши","апельсины"]
#items[1] = "бананы"
#items[-1] = "мандарины"
#print("груши" in items)


#items = ["яблоки","кабачки","груши","апельсины"]
#new_item = "бананы"
#if new_item not in items:
    #items.append(new_item)
#items.pop(1)
#i = 0
#while i < len(items) - 1:
    #item = items[i]
    #print(item)
    #i += 1

#№1
#a = [5,3,4,8,7,6]
#sum(a)//len(a)
#print(sum(a)//len(a))

#№2
#a = input().split()
#print(f"До сортировки:{(a)}")
#a.sort()
#print(f"После сортировки:{(a)}")
#print(max(a))

#№3
#a = input().split()
#print(f"До сортировки:{(a)}")
#a.reverse()
#print(f"После сортировки:{(a)}")

#№6
#a = [4,2,5,9,6,9,7,0,3]
#print(f"До сортировки:{(a)}")
#max(a)
#print(f"Максимальная цифра:{(max(a))}")

#№4
#a = [6,5,2,9,7,0]
#print(f"До сортировки:{(a)}")
#len(a)
#print(f"Размер списка:{(len(a))}")
#a.count(2)
#print(f"Кол-во повторяющихся цифр 2: {(a.count(2))}")



#Повторение
#items = [1,3,2,7,5,8,35,6,24,3]
#a = items.index(35)
#items[a] = 200
#print(items)

#items = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#index=0
#while index<len(items):
    #if items[index]%2==0:
        #print(items[index])
    #index+=1

#from random import randint
#n = randint(1,10)
#items = []
#q = 1
#a = int(input())
#while q <= a:
    #items.append(randint(1,10))
    #q+=1
#print(items)


#Процедуры и функции. Lambda function.*args,**kwargs
#def calc(a,b):
    #c = a + b
    #print(f"{a}+{b}={c}")
#calc(5,4)

#def main():
    #say_hello()  #вызов функции say_hallo
    #say_goodbye()    #вызов функции say_goodbye
#def say_hello():
    #print("Привет")
#def say_goodbye():
    #print("Пока")
#main() #вызов функции maie

#def print_persone(name,age=18):
    #print(f"Имя:{name},возраст:{age}")
#print_persone("Bob")  #Имя:Bob,возраст18
#print_persone("Tom",37)    #Имя:Tom:,возраст:37

#a = [1,2,3]
#b = [a,4,5,6]
#print(b)     #b = [[1,2,3]4,5,6]
#c = [*a,4,5,6]
#print(c)   #c = [1,2,3,4,5,6]

##speed = [100,95,88,92,99]
##student = input()
#def printScores(student,scores):    #def printScores(student,*scores)
    #print(f"Имя студента:{student}")
    #for score in scores:
        #print(score)
##printScores("Михаил",100,95,88,92,99)
#printScores(student,speed)

#def printPetNames(ower,**pets):
    #print(f"Имя владельца:{ower}")
    #for pet,name in pets.items():
        #print(f"{pet}:{name}")
#printPetNames("Михаил",dog="Брок",fish=["Ларри","Дорри","Мо"], turtle="Шелдон")

#возращение результата
#def get_massage():
    #text = "Привет!"
    #return text

#massage = lambda: print("hello")
#massage()   #hello

#square = lambda n: n * n
#for i in range(1,10):
    #print(square(i))

#№1
#def main():
    #say_hello()  #вызов функции say_hallo
    #say_goodbye()    #вызов функции say_goodbye
#def say_hello():
    #print("Hello")
    #print("hello")
#def say_goodbye():
    #print("Bye")
#main() #вызов функции maie

#№2
#def main():
    #name = input("Ведите имя:")
    #print("Hallo",name)
#def say_HelloUser():
    #print("hallo",input())
#def say_ByeUser():
    #print("Bye",input())
#main()
#main()

#№3
#def main():
    #name = input("Ведите имя:")
    #if name == "":
        #print("Hallo Гость")
    #else:
        #print("Hello",name)
#main()

#№4
#def printMax():
    #a = int(input())
    #b = int(input())
    #if a>b:
        #print("Большее число:",a)
    #else:
        #print("Большее число:",b)
#printMax()
#printMax()




#figura = input("Введите фигуру: ")
#def printSqear1():
    #a = int(input("Ведите длинну прямоугольника: "))
    #h = int(input("Введите ширину прямоуголиника: "))
    #W = a*h
    #print("Площадь прямоугольника: " ,W)
#def printSqear2():
    #b = int(input("Ведите высоту треугольника: "))
    #q = int(input("Введите ширину треугольника: "))
    #I = (b*q)/2
    #print("Площадь треугольника:" ,I)
#def printSqear3():
    #a = int(input("Ведите длинну: "))
    #r = int(input("Введите радиус: "))
    #S = a*(r**2)
    #print("Площадь круга:" ,S)
#if figura =="1":
    #printSqear1()
#if figura =="2":
    #printSqear2()
#if figura == "3":
    #printSqear3()


#def sum_range(start,end):
    #if start>end:
        #start,end=end,start
    #s = 0
    #for i in range(start,end+1):
        #s+=i
    #return s
#print(sum_range(5,10))

#def printSqear3(r):
    #a = int(input("Ведите длинну: "))
    #S = a*(r**2)
    #print("Площадь круга:" ,S)
#printSqear3(32)

#def max1(a):
    #maxx=a[0]
    #for i in a:
        #if i>maxx:
            #maxx=i
    #return maxx
#b = [1,2,3]
#print(max1(b))


#numbers = [1,2,4,5,6,7,8,6,7,43,64,14,64,2,0]
#def spisok(numbers):
    #a = []
    #for number in numbers:
        #if number in a:
            #continue
        #else:
            #a.append(number)
    #return a
#print(spisok(numbers))

#def squere(a):
    #P = a*4
    #print("Периметр квадрата:",P)
    #S = a**2
    #print("Площадь квадрата:",S)
    #D = (a**2)*2
    #print("Диагональ квадрата:",D)
    #k=(P,S,D)
    #return k
#print(squere(5))



#Словари в питоне
#user_list = [
    #["Tom","+111123455"],
    #["Bob","+385563295"],
    #["Alise","+956831256"],
#]
#user_dict = dict(user_list)
#print(user_dict)        #{'Tom'+111123455,'Bob',+385563259}

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#print(users["Alise"])       #+956.....
#users["Bob"] = "+33333333333"
#print(users["Bob"])         #+33333333

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#print(users)
#users["Sam"] = "+65464546"
#print(users)

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#key = "Bob"
#if key in users:
    #user = users[key]
    #print(user)
#else:
    #print("Элемент не найден")

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#del users["Alise"]
#print(users)

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#key = "Bob"
#if key in users:
    #del users[key]
    #print(f"Элемент с ключем {key} удален")
#else:
    #print("Элемент не найден")

#users = {
    #"Tom":"+111123455",
    #"Bob":"+385563295",
    #"Alise":"+956831256",
#}
#for key in users:
    #print(f"User:{key},Phone:{users[key]}")
#for key, value in users.items():
    #print(f"User:{key},Phone:{value}")

#users = {
    #"Tom":{
        #"phone":"+87369044",
        #"email":"tom12@gmail.com"
    #},
    #"Bob":{
        #"phone":"+873690444",
        #"email":"bob@gmail.com",
        #"skype":"bob123"
    #}
#}
#print(users["Tom"]["email"])

#users = {
    #"Tom":{
        #"phone":"+87369044",
        #"email":"tom12@gmail.com"
    #},
    #"Bob":{
        #"phone":"+873690444",
        #"email":"bob@gmail.com",
        #"skype":"bob123"
    #}
#}
#key = "skype"
#if key in users["Bob"]:
    #print(users["Bob"]["skype"])
#else:
    #print("skype не найден")

#№1
#users = {
    #"Tom":"123456",
    #"Bob":"654321",
    #"Mike":"09876"
#}
#key = "Bob"
#if key in users:
    #user = users[key]
    #print(user)
#else:
    #print("Элемент не найден")

#users = {
    #1:{
        #"Понедельник",
        #"Monday"
    #},
    #2:{
        #"Вторник",
        #"Tuesday"
    #},
    #3:{
        #"Среда",
        #"Wednesday"
    #},
    #4:{
        #"Четверг",
        #"Thusday"
    #},
    #5:{
        #"Пятница",
        #"Friday"
    #},
    #6:{
        #"Суббота",
        #"Saturday"
    #},
    #7:{
        #"Воскресенье",
        #"Sunday"
    #},
#}
#key =int(input("Введите число от 1 до 7: "))
#if key in users:
    #user=users[key]
    #print(user)
#else:
    #print("Элемент не найден")



#Повторение
#x=1
#while x!=0:
    #print("Введите 2 числа: ")
    #a = int(input())
    #b = int(input())
    #print(a,'+',b,'=',(a+b))
    #print("Ecли хотите закончить операцию напишите 0: ")
    #h = int(input())
    #if h==0:
        #break

#animals = input().split()
#numbers = map(int, input().split())
#s1=dict(zip(animals,numbers))
#animals2 = input().split()
#numbers2 = map(int, input().split())
#s2=dict(zip(animals2,numbers2))
#s3 = s1.copy()
#s3.update(s2)
#print(s1)
#print('+')
#print(s2)
#print('=')
#print(s3)

#Tovar = {
    #"Молоко":{
        #"Категория":"Молочный продукт",
        #"Описание":"ВКУСНОЕ МОЛОЧКО",
        #"Цена":"1000000 рублей"
    #},
    #"Апильсин":{
        #"Категория":"Фрукты",
        #"Описание":"СОЧНЕЙШИЙ АПЕЛЬСИН",
        #"Цена":"150 рублей/кг"
    #},
    #"Ручка":{
        #"Категория": "Канстовары",
        #"Описание": "ЛУЧШАЯ В МИРЕ РУЧКА",
        #"Цена": "10 рублей"
    #}
#}
#key =input("Введите нужный товар: Молоко, Апельсин, Ручка: ")
#print(Tovar[key])

#def create_dictionary():
    #dictionary = {}
    #while True:
        #print("Меню:")
        #print("1. Добавить элемент в словарь")
        #print("2. Вывести все ключи")
        #print("3. Вывести все значения")
        #print("4. Перезаписать словарь")
        #print("5. Выход")
        #choice = int(input("Введите номер пункта из меню: "))
        #if choice == 1:
            #key = input("Введите ключ: ")
            #value = input("Введите значение: ")
            #dictionary[key] = value
            #print("Элемент успешно добавлен в словарь.")
        #elif choice == 2:
            #print("Ключи в словаре: ", list(dictionary.keys()))
        #elif choice == 3:
            #print("Значения в словаре: ", list(dictionary.values()))
        #elif choice == 4:
            #dictionary.clear()
            #print("Словарь успешно перезаписан.")
        #elif choice == 5:
            #break
        #else:
            #print("Неверный ввод. Попробуйте снова.")
#create_dictionary()

#s1 = [1,2,3,4,5,6]
#s2 = ["a","b","c","d","i","f"]
#s3=dict(zip(s1,s2))
#print(s3)

#a = int(input())
#s1 = {}
#for i in range(1,(a+1)):
    #s1[i]=i**3
#print(s1)

#a = "SledusheeZanyatieSamostoyatelnay"
#s1 = {}
#for i in a:
    #if i in a:
        #a[i]+=1
#else:
    #a[i]=1
#print(s1)


#1
#str1 = input()
#len(str1)
#print(f"Длинна строки равна:{len(str1)}")

#2
#=input()
#or char in a:
   #print(char)

#def spisok():
    #a = [2,3,4,5,6,7,8,9,17,3]
    #len(a)
    #print(len(a))
    #max(a)
    #min(a)
    #print(max(a))
    #print(min(a))
    #min(a)*max(a)
    #print(min(a)*max(a))
#spisok()

#a = {
    #"1":{
        #"numbers":"2,3,4,5,6,7,8,9,17,3",
    #}
#}
#key = input()
#print(a[key])


#import random
#l = []
#m = int(input())
#y=1
#index=0
#summ=0
#sumc=0
#while y<=m:
    #l.append(random.randint(1,10))
    #y+=1
#print(l)
#while index<len(l):
    #if l[index]%2==0:
        #sumc+=l[index]
    #if l[index]%2!=0:
        #summ+=l[index]
        #print(l [index])
    #index+=1



#Модули. Import модулей. Разделение кода

#import message
#print(message.hello)
#message.print_message("Hello Work")

#from message import print_message
#print_message("Hello work")    #Message:Hello work


#from message import *
#print_message("Hello work")
#print(hello)

#import message as mes
#print(mes.hello)
#mes.print_message("Hello work")

#from message import print_message as display
#from message import hello as welcome
#print(welcome)
#display("Hello work")

#import calc
#print(calc.print_figura())

#import calc
#print(calc.print_shislo())

#import calc
#print(calc.print_Treygolnik())
#print(calc.print_figura())

import calc
print(calc.print_1())

