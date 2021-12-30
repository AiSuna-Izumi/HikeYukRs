import sqlite3 as sql
#from flask_login import user_loaded_from_header
from modelstu import *  
#from user_authentication import *
from flask import Flask,render_template,request,redirect,jsonify
import os 
from os.path import join, dirname, realpath
from userFilter import *
from placeFilter import *
import pandas as pd
# create the application object


app = Flask(__name__)

# PIC_UPLOAD='static/pic'
# app.config['PIC_UPLOAD']=PIC_UPLOAD
#only 3 files - controller, model, view(html files)

@app.route('/')
def home():
    N11=filterNegeri1("Terengganu")
    N06=filterNegeri1("Pahang")
    N08=filterNegeri1("Perak")
    return render_template('index.html',CN11=N11.columns.values,RN11=N11.values.tolist(),CN06=N06.columns.values,RN06=N06.values.tolist(),CN08=N08.columns.values,RN08=N08.values.tolist())
    # return render_template('index.html')

@app.route('/getData', methods=['POST'])
def RecommenderInterface():
    nama=request.form['nama']
    age=float(request.form['umur'])
    tinggi=float(request.form['tinggi'])
    berat=float(request.form['berat'])
    negeri=request.form['negeri']
    
    daerahDisplay=listDaerah(negeri)
    
    bmi=berat/pow(tinggi/100,2)
    user=recommenderUser(age,bmi)
    tempat=filterPlace(user,negeri)
    session['nama']=nama
    session['age']=age
    session['negeri']=negeri
    session['bmi']=berat/pow(tinggi/100,2)
    return render_template('hikeYukRs.html',nama=nama,CN11=tempat.columns.values,RN11=tempat.values.tolist(),daerah=daerahDisplay.values.tolist())
    
@app.route('/getDaerah', methods=['POST'])
def daerahGet():
    daerah=request.form['daerah']
    jarak=request.form['jarak']
    tahap=request.form['tahap']
    khemah=request.form['khemah']
    
    user=recommenderUser(session['age'],session['bmi'])
    v=filterPlace(user,session['negeri'])
    
    if daerah !='All':
        da1=filterDaerah(v,daerah)
    else:
        da1=v
        
    if jarak !='All':
        ja=filterJarak(da1,jarak)
    else:
        ja=da1
        
    if tahap !='All':
        ta=filterTahap(ja,tahap)
    else:
        ta=ja
    
    if khemah !='All':
        khe=filterKhemah(ta,khemah)
    else:
        khe=ta
        

    daerahDisplay=listDaerah(session['negeri'])
    
    return render_template('hikeYukRs.html',CN11=khe.columns.values,RN11=khe.values.tolist(),daerah=daerahDisplay.values.tolist())
    
@app.route('/logout')
def logout():
    session['nama']=False
    session['age']=False
    session['negeri']=False
    session['bmi']=False
   
    return home()


# start the server using the run() method
if __name__ == "__main__":
     app.secret_key = "!mzo53678912489"
     app.run(debug=True,host='0.0.0.0', port=3000)
