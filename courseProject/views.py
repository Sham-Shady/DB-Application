from django.http import HttpResponse
import mysql.connector
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(requests):
    if 'Studlog' in requests.POST:
        return redirect('studentlogin')
    if 'Proflog' in requests.POST:
        return redirect('professorlogin')
    if 'Adlog' in requests.POST:
        return redirect('adminlogin')

    return render(requests, 'home.html')

def admin(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KazumaK1ryu!',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )
    return HttpResponse("Hello Student")


def professors(request):
    return HttpResponse("Hello World")

def professors_search(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='enter your password',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM instructor WHERE current_salary>90000')

    data = '<table style="width:400px">'

    data += '</table>'

    mycursor.close()
    mydb.close()


def professors_salaries(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='enter your password',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM instructor WHERE current_salary>90000')

    data = '<table style="width:400px">'

    data += '</table>'

    mycursor.close()
    mydb.close()


def professors_studenst(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='enter your password',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM instructor WHERE current_salary>90000')

    data = '<table style="width:400px">'

    data += '</table>'

    mycursor.close()
    mydb.close()