n=int(input("enter the number:"))
def armstrong(n):
    temp=n
    sum=0

    while (n>0):
        rem=n%10
        sum=sum+(rem*rem*rem)
        n=n//10

    if temp==sum:
        print("Armstrong")
    else:
        print("Not Armstrong")

if __name__=="__main__":
    print(armstrong(n))