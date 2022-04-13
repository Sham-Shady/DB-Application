from django.shortcuts import render
from django.urls import path
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token,csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
import mysql.connector

# Create your views here.

# Carter Peets blank push

def students(request):
    return render(results(request), 'studentsView.html')
@csrf_protect
def results(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='your password',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if 'Search' in request.POST:
        search = request.POST.get('search')

        mycursor = mydb.cursor()
        # Still need a where clause for user input
        # WHERE course_id LIKE search
        mycursor.execute('SELECT * FROM section WHERE course_id LIKE search')

        data = '<table style="width:400px">'
        for (course_id, sec_ID, semester, year, building, room, capacity) in mycursor:
            r = ('<tr>' + \
                 '<th>' + str(course_id) + '</th>' + \
                 '<th>' + str(sec_ID) + '</th>' + \
                 '<th>' + str(semester) + '</th>' + \
                 '<th>' + str(year) + '</th>' + \
                 '<th>' + building + '</th>' + \
                 '<th>' + str(room) + '</th>' + \
                 '<th>' + str(capacity) + '</th>' + \
                 '</tr>')
            data += r
        data += '</table>'

        mycursor.close()
        mydb.close()
        return  render(request, data)
