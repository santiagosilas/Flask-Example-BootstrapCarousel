# exemplo
from flask import Flask, request, render_template,redirect, url_for
from app import app 

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
