n = int(input())
flag = 0
if n == 2:
    print("prime")
    flag = 1
elif n == 1:
    print("not prime")
    flag = 1
else:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            flag = 1
            break
if flag == 0:
    print("prime")
