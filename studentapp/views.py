from django.shortcuts import render
import pymysql
# Create your views here.

def home(request):
    return render(request,'studentapp/index.html')

def stulogin(request):
    return render(request,'studentapp/student.html')  

def register(request):
    return render(request,'studentapp/register.html')  

def liblogin(request):
    return render(request,'studentapp/library.html')

def registeraction(request):
    f=request.POST['fname']
    m=request.POST['Mobileno']
    r=request.POST['rollno']
    p=request.POST['password']
    con=pymysql.connect(host="localhost",user="root",password="Aizen",database="test")
    cur=con.cursor()
    cur.execute("select * from lib where rollno='"+r+"'")
    d=cur.fetchone()
    # print(d)
    if d is not None:
        context={'data':'rollno already exists'}
        return render(request,'studentapp/register.html',context)
    else:
        i=cur.execute("insert into lib values('"+f+"','"+m+"','"+r+"','"+p+"')")
        con.commit()
        if i>0:                 
            context={'data':'Data entered successfully'}
            return render(request,'studentapp/register.html',context)
        else:
            context={'data':'Data enter failed'}
            return render(request,'studentapp/register.html',context)
    cur.close()
    con.close()

def loginaction(request):
    r=request.POST['rollno']
    p=request.POST['pwd']
    con=pymysql.connect(host="localhost",user="root",password="Aizen",database="test")
    cur=con.cursor()
    i=cur.execute("select * from lib where rollno='"+r+"' and pwd='"+p+"'")
    a=cur.fetchone()
    if i>0:
        context={'data':a[0]}
        return render(request,"studentapp/lhome.html",context)
    else:
        context={'data':'login unsuccessful'}
        return render(request,"studentapp/student.html",context)
    cur.close()
    con.close()

def shome(request): 
    return render(request,'studentapp/lhome.html')

def libhome(request):
    r=request.POST['rollno']
    p=request.POST['pwd']
    con=pymysql.connect(host="localhost",user="root",password="Aizen",database="test")
    cur=con.cursor()
    i=cur.execute("select * from lacc where rollno='"+r+"' and password='"+p+"'")
    if i>0:
        return render(request,"librarianapp/libhome.html")
    else:
        context={'data':'login unsuccessful'}
        return render(request,"librarianapp/library.html",context)
    cur.close()
    con.close()

def lhome(request):
    return render(request,"librarianapp/home.html")

def browse(request):
    return render(request,)

def addbook(request):
    return render(request,"librarianapp/addbook.html")


def AddBookAction(request):
    f=request.POST['rno']
    m=request.POST['bname']
    r=request.POST['author']
    
    con=pymysql.connect(host="localhost",user="root",password="Aizen",database="test")
    cur=con.cursor()
    cur.execute("select * from books where rno='"+r+"'")
    d=cur.fetchone()
    # print(d)
    if d is not None:
        context={'data':'rno already exists'}
        return render(request,'librarianapp/addbook.html',context)
    else:
        i=cur.execute("insert into books values('"+f+"','"+m+"','"+r+"')")
        con.commit()
        if i>0:                 
            context={'data':'Book entered successfully'}
            return render(request,'librarianapp/addbook.html',context)
        else:
            context={'data':'Book enter failed'}
            return render(request,'librarianapp/addbook.html',context)

def Searchbooks(request):
    return render(request,'studentapp/Searchbooks.html')

def Searchbooksaction(request):
    f=request.POST['bname']
    con=pymysql.connect(host="localhost",user="root",password="Aizen",database="test")
    cur=con.cursor()
    cur.execute("select * from books where bname='"+f+"'")
    d=cur.fetchone()
    if d is not None:
        



   


