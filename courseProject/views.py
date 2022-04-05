from django.http import HttpResponse
import mysql.connector

def home(requests):
    return HttpResponse("Welcome to the Home page")

def admin(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
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
        passwd='PKSFall2021!*',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    mycursor = mydb.cursor()

    mycursor.execute('SELECT * FROM instructor WHERE current_salary>90000')

    data = '<table style="width:400px">'

    data += '</table>'

    mycursor.close()
    mydb.close()