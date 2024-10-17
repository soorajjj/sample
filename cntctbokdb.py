import mysql.connector
try:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="751030")
        cursor=mydb.cursor()
        cursor.execute("Create database contactbook1")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="contactbook1"
        )
        cursor-mydb.cursor()
        cursor.execute("Create table phonebook(name varchar(25), phoneno bigint)")
except Exception as e:
        print(e)
        print("DB already exists!!!")
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="contactbook1"
        )
cursor=mydb.cursor()
def insert(name,phno): 
    cursor.execute("select name from phonebook") #[(name1,), (name2,), (name3,)] 
    names=cursor.fetchall()
    print(names)
    f=0
    for i in names:
            if name==i[0]:
                f=1
    if f==0:
            #sql="Insert into phonebook (name, phoneno) values(%s,%s)" #val=(name, phno)
            #cursor.execute(sql, val)
            cursor.execute("Insert into phonebook (name, phoneno) values (%s, %s)", (name, phno)) 
            mydb.commit()
    else:
            print("Name already exists!!")
def update(data):
            oldname=data
            cursor.execute("Select name from phonebook where name=%s", (oldname,)) 
                            #select name from phonebook where name="aman" selname=cursor.fetchall()#[()]
            print(selname)
            newname=input("Enter new name:")
def update(data):
            oldname=data
            cursor.execute("Select name from phonebook where name=%s", (oldname,))
                            # select name from phonebook where name="aman" 
            selname=cursor.fetchall()#[()]
            print(selname)
            newname=input("Enter new name:") 
            if newname in selname[0]: 
                    print("Name exists!!")
            else:
                    cursor.execute("Update phonebook set name=%s where name=%s", (newname, oldname)) #UPDATE PHONEBOOK SET NAME="NEWNAME" WHERE NAME="OLDNAME"; mydb.commit() print("Updated successfully")
def delete(item):
    cursor.execute("Select name from phonebook")
    itemlis=cursor.fetchall()# [(name,), (name2,)]
    # print(itemlis)
    f=True
    for i in itemlis:
         if item in i[0]: 
            cursor.execute("delete from phonebook where name=%s", (item,))
            mydb.commit() 
            f=False
    if f:
            print("Contact not found")
def display():
        cursor.execute("select from phonebook")
        cntcts=cursor.fetchall()
        print(cntcts)
while(True):
    print("-----Menu")
    print(" 1. Insertion\n 2.Updation\n 3.Deletion\n 4. Display\n 5.Exit") 
    ch=int(input("Enter ur choice:"))
    if(ch==1):
            print("Insert new contact")
            name=input("Enter name:")
            phno=input("Enter no:") 
            insert(name, phno)
    elif(ch==2):
            print("Updation")
            data=input("Update name??Enter the old name") #name
            update(data)
    elif(ch==3):
            print("Deletion")
            item=input("Enter name:")
            delete(item)
            #print("Deleted Contact", item)
    elif(ch==4):
            display()
    elif(ch==5):
            break
    else:
        print("Wrong choice")
       