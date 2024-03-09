def shuu(N):
    sum=0
    if (N>=0):
        for i in range(N,(2*N)+1):
            sum+=(i)
    else:
        if(N<=0):
            for i in range((2*N),N+1):
                sum+=(i)
    print("the summation: ",sum)
def main():
    N=int(input("enter the number: "))
    shuu(N)
main()   
