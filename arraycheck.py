def sortcheck(a):
    l = len.a
    j=1
    for j in range(0,l):
        if a[j]==a[j-1]+1==a[j-2]+2:
            print("FOUND IT!")
        else:
            print("No chance buddy")
print("Enter elements of the arrray")
b = input("Enter the size of the list")
a = int(b)
i=0
ar = []
while i<a:
    p= input("Enter element{}".format(i))
    ar.append(p)
    i=i+1
sortcheck(ar)
