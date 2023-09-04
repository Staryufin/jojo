q=[16, 44 ,68 ,72,94,52 ,61 ,85 ,28, 67 ,31, 32, 81, 50, 80, 11, 39, 54,
   32 ,20 ,61 ,73 ,57, 83 ,73, 99, 26, 56, 27, 95, 79, 65, 96, 5, 76, 78, 99, 66, 98, 15 ,84, 46]
r=int(input())
for t in q :
    if t%r==0:
        with open("riba.txt\n","a") as era :

            era.write(str(t))

        print(t)
        with open("riba.txt\n","a") as era :

            era.write(str(t))