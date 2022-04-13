from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token,csrf_protect
from django.http import HttpResponse
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from string import Template
import mysql.connector

# Create your views here.


@csrf_exempt
def students(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KazumaK1ryu!',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if 'Search' in request.POST:
        search = request.POST.get('department')

        mycursor = mydb.cursor()
        # Still need a where clause for user input
        # WHERE course_id LIKE search
        mycursor.execute('use university')
        mycursor.execute("SELECT * FROM section WHERE course_id LIKE '" + str(search) + "%'")

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

        dataworking = {'data': data}
        mycursor.close()
        mydb.close()
        return render(request, 'studentsResult.html', dataworking)

        if 'Go Back' in request.POST:
            return render(request, 'studentsView.html')
    return render(request, 'studentsView.html')


@requires_csrf_token
def results(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KazumaK1ryu!',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    if 'Search' in request.POST:
        search = request.POST.get('department')

        mycursor = mydb.cursor()
        # Still need a where clause for user input
        # WHERE course_id LIKE search
        mycursor.execute('use university')
        mycursor.execute("SELECT * FROM section WHERE course_id LIKE '"+ str(search)+"%'")

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

        dataworking = {'data':data}
        mycursor.close()
        mydb.close()
        return redirect('results',dataworking)
    return render(request, 'studentsResult.html')
