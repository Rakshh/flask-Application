# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:39:56 2020
@author: hp
"""

from flask import Flask, render_template, request
from boto3.dynamodb.conditions import Key, Attr
import boto3
import key_config as keys
application = Flask(__name__)
dynamodb = boto3.resource('dynamodb',
                    aws_access_key_id=keys.ACCESS_KEY_ID,
                    aws_secret_access_key=keys.ACCESS_SECRET_KEY,
                    aws_session_token=keys.AWS_SESSION_TOKEN,
                    region_name='us-east-1')

@application.route('/')
def index():
    """
    This is the landing page of the application
    """
    return render_template('index.html')


@application.route('/signup', methods=['post'])
def signup():
    """
    This page will be called when signup is clicked
    """
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        table = dynamodb.Table('userdata')
        table.put_item(
                Item={
        'name': name,
        'email': email,
        'password': password
            }
        )
        msg = "Registration Complete. Please Login to your account !"
        return render_template('login.html',msg = msg)
    return render_template('index.html')
@application.route('/login')
def login():   
    """
    This method is called for login
    """
    return render_template('login.html')
@application.route('/check',methods = ['post'])
def check():
    """
    This methods checks the credentials
    """
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        table = dynamodb.Table('userdata')
        response = table.query(
                KeyConditionExpression=Key('email').eq(email)
        )
        items = response['Items']
        name = items[0]['name']
        print(items[0]['password'])
        if password == items[0]['password']:
            return render_template("home.html",name = name)
    return render_template("login.html")


@application.route('/home')
def home():
    """
    home page called
    """
    return render_template('home.html')
    

