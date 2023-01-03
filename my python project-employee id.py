
a={'priyansh':3454,'shraddha':7676,'uysas':234,'sds':345}
print(a)
print('enter the choice 1: for name or 2: for employee')
z=int(input('enter the choice'))
if(z==1):
    x=input("enter the name")
    x.lower()
    for i in a:
        if(x==i):
            o=a[i]
            print('Employee id = ',o)
            o=str(o)
            o=list(o)
            print(o)
            for j in o:
                print(j)
elif(z==2):
    y=int(input("enter the Employee id"))
    for i in a:
        if(y==a[i]):
            o=i
            print('Name = ',o)

            o=list(o)
            print(o)
            for j in o:
                print(j)
else:
    print('incorrect input')