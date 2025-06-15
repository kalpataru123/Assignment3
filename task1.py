n=int(input("Enter number:"));
def cal_fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*cal_fact(n-1);
result=cal_fact(n);
print("factorial of",n,"is:",result);