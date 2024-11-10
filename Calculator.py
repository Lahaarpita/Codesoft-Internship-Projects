n1=int(input("enter 1st no.:"))
n2=int(input("enter 2nd no.:"))
print(n1,n2)
print("press 1 for add\n,press 2 for sub\n,press 3 for mul\n,press 4 for div\n")
ch=int(input("press any no. between 1-4"))
if ch==1:
    print(n1+n2)
elif ch==2:
    print(n1-n2)
elif ch==3:
    print(n1*n2)
elif ch==4:
    print(n1/n2)
else:
    print("invalid")
