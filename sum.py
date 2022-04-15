t= int(input())
c=1
while t:
    print()
    n=int(input())


    a=list(map(int,input().split()))

    print(f"Case {c}: {sum(a)}")
    c+=1
    t=t-1