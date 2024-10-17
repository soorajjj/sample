import pickle
bfile=open("empfile","wb")
n=int(input("enter the number of employees"))
print("enter the records of employees")
i=1
while i<=n:
    print("record no.",i)
    ename=input("employee name :")
    ebasic=int(input("basic salary :"))
    ns=int(input("enter the number of nightshits"))
    hra=ebasic*.15
    pf=ebasic*.05
    da=ebasic*.08
    totalsal=ebasic+hra+da-pf+(ns*300)
    print("net salary :",totalsal)
    edata={'no':i,'name':ename,'basicsalary':ebasic,'total salary':totalsal}
    pickle.dump(edata,bfile)
    i=i+1
bfile.close()
print("reading the employee records from the file")
empno=1
bfile=open("empfile","rb")
while empno<n+1:
    edata=pickle.load(bfile)
    print("recod number :",empno)
    print(edata)
    empno=empno+1
    print("End of file reached.")
    bfile.close()