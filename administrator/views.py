import mysql
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt
from mysql.connector import ProgrammingError


@csrf_exempt
def administrator(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd='KazumaK1ryu!',  # "mypassword",
        auth_plugin='mysql_native_password',
        database="university",
    )

    # These are all different redirects for Return buttons. Way to make this cleaner?

    if 'Go Home' in request.POST:
        return redirect('home')

    if 'Go Back to Order' in request.POST:
        return render(request, 'adminsOrderView.html')

    if 'Go Back More' in request.POST:
        return render(request, 'adminsSelect.html')

    if 'Go Back to Login' in request.POST:
        return redirect('adminlogin')

    if 'Salaries' in request.POST:
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute('use university')  # Select database

        mycursor.execute("SHOW TABLES LIKE 'DeptSalaries'")  # Search for tables with name matching criteria
        tableexistcheck = mycursor.rowcount  # Get the rowcount of the query

        if tableexistcheck == 0:
            mycursor.execute("CREATE TABLE DeptSalaries (Dept varchar(200), Min int, Max int, Average int);")

        mycursor.execute("SELECT * FROM DeptSalaries;")
        datacheck = mycursor.rowcount

        if datacheck == 0:
            mycursor.execute("DELETE FROM DeptSalaries;")

        mycursor.execute("INSERT INTO DeptSalaries (SELECT dept, min(salary), max(salary), avg(salary) FROM instructor GROUP BY dept);")
        mydb.commit()
        mycursor.execute("SELECT dept, min(salary), max(salary), avg(salary) FROM instructor GROUP BY dept;")

        data = '<table style="width:400px; border: 1px solid black; border-collapse: collapse"><tr><th>Department</th><th>Min Salary</th><th>Max Salary</th><th>Average Salary</th></tr>'
        for (dept, min, max, avg) in mycursor:
            r = ('<tr>' + \
                 '<td style="border: 1px solid black; border-collapse: collapse">' + str(dept) + '</td>' + \
                 '<td style="border: 1px solid black; border-collapse: collapse">$' + str(min) + '</td>' + \
                 '<td style="border: 1px solid black; border-collapse: collapse">$' + str(max) + '</td>' + \
                 '<td style="border: 1px solid black; border-collapse: collapse">$' + str(avg) + '</td>' + \
                 '</tr>')
            data += r
        data += '</table>'

        dataworking = {'data': data}

        mycursor.close()
        mydb.close()

        return render(request, 'adminsSalaryResults.html', dataworking)

    if 'OrderBy' in request.POST:
        return render(request, 'adminsOrderView.html')

    if 'Create Table' in request.POST:
        # Do stuff
        namesort = request.POST.get('sort')

        if namesort == 'name':
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('use university')  # Select database

            mycursor.execute("SHOW TABLES LIKE 'ProfNameSort'")  # Search for tables with name matching criteria
            tableexistcheck = mycursor.rowcount  # Get the rowcount of the query

            if tableexistcheck == 0:
                mycursor.execute("CREATE TABLE ProfNameSort (ID int, Name varchar(200), Dept varchar(200), Salary int);")

            mycursor.execute("SELECT * FROM ProfNameSort;")
            datacheck = mycursor.rowcount

            if datacheck == 0:
                mycursor.execute("DELETE FROM ProfNameSort;")

            mycursor.execute("INSERT INTO ProfNameSort (SELECT * FROM instructor ORDER BY name);")
            mydb.commit()
            mycursor.execute("SELECT * FROM instructor ORDER BY name;")

            data = '<table style="width:400px; border: 1px solid black; border-collapse: collapse"><tr><th>ID</th><th>Name</th><th>Department</th><th>Salary</th></tr>'
            for (ID, name, dept, salary) in mycursor:
                r = ('<tr>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(ID) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(name) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(dept) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(salary) + '</td>' + \
                     '</tr>')
                data += r
            data += '</table>'

            dataworking = {'data': data}

            mycursor.close()
            mydb.close()
            return render(request, 'adminsOrderResult.html', dataworking)

        if namesort == 'dept':
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('use university')  # Select database

            mycursor.execute("SHOW TABLES LIKE 'ProfDeptSort'")  # Search for tables with name matching criteria
            tableexistcheck = mycursor.rowcount  # Get the rowcount of the query

            if tableexistcheck == 0:
                mycursor.execute(
                    "CREATE TABLE ProfDeptSort (ID int, Name varchar(200), Dept varchar(200), Salary int);")

            mycursor.execute("SELECT * FROM ProfDeptSort;")
            datacheck = mycursor.rowcount

            if datacheck == 0:
                mycursor.execute("DELETE FROM ProfDeptSort;")

            mycursor.execute("INSERT INTO ProfDeptSort (SELECT * FROM instructor ORDER BY name);")
            mydb.commit()

            mycursor.execute("SELECT * FROM instructor ORDER BY dept;")

            data = '<table style="width:400px; border: 1px solid black; border-collapse: collapse"><tr><th>ID</th><th>Name</th><th>Department</th><th>Salary</th></tr>'
            for (ID, name, dept, salary) in mycursor:
                r = ('<tr>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(ID) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(name) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(dept) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(salary) + '</td>' + \
                     '</tr>')
                data += r
            data += '</table>'

            dataworking = {'data': data}

            mycursor.close()
            mydb.close()
            return render(request, 'adminsOrderResult.html', dataworking)

        if namesort == 'salary':
            mycursor = mydb.cursor(buffered=True)
            mycursor.execute('use university')  # Select database

            mycursor.execute("SHOW TABLES LIKE 'ProfSalarySort'")  # Search for tables with name matching criteria
            tableexistcheck = mycursor.rowcount  # Get the rowcount of the query

            if tableexistcheck == 0:
                mycursor.execute(
                    "CREATE TABLE ProfSalarySort (ID int, Name varchar(200), Dept varchar(200), Salary int);")

            mycursor.execute("SELECT * FROM ProfSalarySort;")
            datacheck = mycursor.rowcount

            if datacheck == 0:
                mycursor.execute("DELETE FROM ProfSalarySort;")

            mycursor.execute("INSERT INTO ProfSalarySort (SELECT * FROM instructor ORDER BY name);")
            mydb.commit()

            mycursor.execute("SELECT * FROM instructor ORDER BY salary;")

            data = '<table style="width:400px; border: 1px solid black; border-collapse: collapse"><tr><th>ID</th><th>Name</th><th>Department</th><th>Salary</th></tr>'
            for (ID, name, dept, salary) in mycursor:
                r = ('<tr>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(ID) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(name) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(dept) + '</td>' + \
                     '<td style="border: 1px solid black; border-collapse: collapse">' + str(salary) + '</td>' + \
                     '</tr>')
                data += r
            data += '</table>'

            dataworking = {'data': data}

            mycursor.close()
            mydb.close()
            return render(request, 'adminsOrderResult.html', dataworking)





    return render(request, 'adminsSelect.html')

@requires_csrf_token
def adminlogin(request):
    global user
    global pwd

    if 'Login' in request.POST: # If login button is pressed
        # Get user input
        user = request.POST.get('username')
        pwd = request.POST.get('password')

        try: # Try to sign in with given credentials
            mydb = mysql.connector.connect(
                host="localhost",
                user=str(user),
                passwd=str(pwd),  # "mypassword",
                auth_plugin='mysql_native_password',
                database="university",
            )
            return redirect('administrator')

        except ProgrammingError: # Exception raised if credentials are invalid, so display an error message
            error = "<h1>Invalid Credentials.</h1>"
            return render(request, 'adminLogin.html', {'error': error})
    if 'Go Home' in request.POST:
        return redirect('home')

    return render(request, 'adminLogin.html')