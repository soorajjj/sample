def factorial(n):
    if n==1:
        return 
    f=n*factorial(n-1)
    return f
no=int(input("enter the number :"))
fact=factorial(no)
print("factorial is : ",fact)
