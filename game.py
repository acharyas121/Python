import random
print("Hello and welcome to my number game!!")
a =random.randint(100,999)
print(a)
gg1 = input("Enter your first guess")
g1 = int(gg1)
while g1!=a:
    s1 = g1%10
    s2 = (g1//10)%10
    s3 = (g1//10)//10
    ss1 = a%10
    ss2 = (a//10)%10
    ss3 = (a//10)//10
    l1 = [s1,s2,s3]
    l2 = [ss1,ss2,ss3]
    i = 0
    j=0
    for i in range(0,3):
        for j in range(0,3):
            if l1[i]==l2[j]:
                print("Match {}!!".format(i+j))
            else:
                print("No match at all")
    gg1 = input("Enter another  guess")
    g1 = int(gg1)
if g1==a:
    print("Bingo!!!")
