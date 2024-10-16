class employee:
    def __init__(self,ename,ecode,ebs):
        self.emp_name=ename
        self.emp_code=ecode
        self.emp_basic=ebs
    def calculate(self):
        if self.emp_basic<10000:
            self.emp_da=self.emp_basic*0.2
            self.emp_hra=self.emp_basic*0.25
            self.emp_pf=self.emp_basic*0.05
        else:
            self.emp_da=self.emp_basic*0.01
            self.emp_hra=self.emp_basic*0.15
            self.emp_pf=self.emp_basic*0.03
        self.emp_ns=self.emp_basic+self.emp_da+self.emp_hra-self.emp_pf
    def display(self):
        print("name :",self.emp_name)
        print("empcode :",self.emp_code)
        print("basic salary :",self.emp_basic)
        print("da :",self.emp_da)
        print("hra :",self.emp_hra)
        print("pf :",self.emp_pf)
        print("netsalary :",self.emp_ns)
class teacher(employee):
    def __init__(self,ename,ecode,ebs,dept):
        employee. __init__(self,enm,ecd,ebs,dept)
        self.department=dept
        self.student=[]
    def mark_attendence(self,n)
        self.count=n
        print("Enter the attendance rollno wise(p-present/a-absent)")
        for i in range(0,n):
            att=input()
            self.student.append(att)
    def display_attendance(self):
        c=0
        print("Count of present students ")
        for i in range(0, self.count):
            if self.student[i].lower()=='p':
                c=c+1
        print(c)
    def display(self):
        print("Name : ", self.emp_name)
        print("Emp code:",self.emp_code)
        print("Department:",self.department)
        print("Basic salary : ", self.emp_basic)
        print("DA : ", self.emp_da)
        print("HRA : ",self.emp_hra)
        print("PF print:", self.emp_pf)
        print("Net Salary:",self.emp_ns)
teacher_list=[]
m=int(input("Enter the number of teachers:"))
for i in range(0,m):
    nme=input("Enter the name of teacher:")
    c=input("Enter the code of a teacher:")
    bs=int(input("Enter the basic salary of a teacher:"))
    dept=input("Enter the department of the teacher: ")
    no=int(input("Enter the number of students: "))
    tchr=teacher (nme,c,bs, dept)
    tchr.mark_attendance (no)
    tchr.calculate()
    teacher_list.append(tchr)
for i in range(0,m):
    print("----")
    teacher_list[i].display()
    teacher_list[i].display_attendance()
print(teacher_list)

