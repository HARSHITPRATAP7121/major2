# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 17:41:23 2022

@author: prata
"""




import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app = Flask(__name__)
 

@app.route('/')
def Home():
  
    return render_template("index.html")

@app.route('/Home')
def Hom():
  
    return render_template("index.html")

@app.route('/Description')
def Description():
  
    return render_template("Description.html")


@app.route('/Mini_Project')
def Mini_Project():
  
    return render_template("Mini_Project.html")

@app.route('/About_Us')
def About_Us():
  
    return render_template("About_Us.html")

@app.route('/Form')
def Form():
  
    return render_template("Form.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    Type = (request.args.get('Type'))
     
    if Type== [0]:
      Type= 'Academic'
    elif Type ==[1]:
      Type= 'Vocational'

    Accreditation= (request.args.get('Accreditation'))
    if Accreditation == [0]:
      Accreditation = 'A'
    elif Accreditation ==[1]:
      Accreditation = 'B'

    Interest = (request.args.get('Interest'))

    if Interest == [0]:
      Interest = 'Interested'
    elif Interest ==[1]:
      Interest = ' Less Interested'
    elif Interest ==[2]:
      Interest = 'Not Interested'
    elif Interest ==[3]:
      Interest = 'Uncertain'
    elif Interest ==[4]:
      Interest = 'Very Interested'

    Residence = (request.args.get('Residence'))

    if Residence == [0]:
       Residence = 'Rural'
    elif Residence ==[1]:
       Residence = 'Urban'

    parents = float(request.args.get('parents'))
    grades = float(request.args.get('grades'))
    models=float(request.args.get('models'))
    if models==0:
        model=pickle.load(open('Major_college_DT_2.pkl','rb'))
        
    elif models==1:
        model=pickle.load(open('Major_college_RF_2.pkl','rb'))
        
    elif models==2:
        model=pickle.load(open('Major_college_DT_2.pkl.pkl','rb'))
       
    elif models==3:
        model=pickle.load(open('Major_college_log_3.pkl','rb'))
        
    elif models==4:
        model=pickle.load(open('Major_college_SVM_2.pkl','rb'))

    prediction = model.predict([[Type,Accreditation,Interest,Residence,parents,grades]])
    if prediction==1:

      message="Congrats ,Student are able to go college"
    else:
        
      message="Student are not able to go college"

    return render_template('Form.html', prediction_text= 'Model has predicted  : {}'.format(message))

if __name__ == "__main__":
    app.run(debug=True)