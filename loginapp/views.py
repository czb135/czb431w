from django.shortcuts import render
import sqlite3
import hashlib


def login(request):
    flag = False
    result = "user error"
    if request.method == "POST":
        username = request.POST.get("user",None)
        password = request.POST.get("password",None)
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        md5password = md5.hexdigest()
        conn = sqlite3.connect("NittanyMarket.db")
        c = conn.cursor()
        select_password_sql = "SELECT PASSWORD FROM USERS WHERE EMAIL ='{}'".format(username)
        cursor = c.execute(select_password_sql)
        for row in cursor:
            if row[0] == md5password:
                flag = True
            else:
                result = "password error"
    if flag == True:
        return render(request,'result.html',{"data":flag})
    else:
        return render(request, 'login.html', {"data":result})
