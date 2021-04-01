from flask.templating import render_template
from flask import Flask, render_template, redirect,url_for,request,flash,session,sessions
from app import app
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import pymysql
import re
from pymysql import cursors
from werkzeug.utils import format_string
import json

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_DB'] = 'cts'
# mysql = MySQL(app) 


# Function LOGOUT
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/mission')
def mission():
    with open("dummydataTask.json", "r",encoding="utf8") as fin:
        data = json.load(fin)
    Task = data
    return render_template("missionsystemadmin.html",Task=Task)

@app.route('/logout')
def logout():
    return render_template("login.html")
@app.route('/logi',methods=['GET','POST'])
def login():
    loi = ""
    if request.method == 'POST':
        user = request.form['idname']
        psw = request.form['password']
        if user=="abc" and psw=="123":
            session['idname'] = request.form['idname']  
            return render_template('home.html')
        if user=="abcd" and psw =="123":
            session['idname'] = request.form['idname']     
            return render_template('home.html')
        else:
                loi = 'Tài khoản hoặc mật khẩu sai'
    return render_template("login.html",loi=loi)
