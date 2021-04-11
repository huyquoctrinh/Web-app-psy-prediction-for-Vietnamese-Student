from flask import Flask, render_template,request,redirect, url_for, send_from_directory,Response
import os
import numpy as np
# from module import predict
import matplotlib.pyplot as plt
import datetime
import csv
# from test_txt import plot_graph
import json
import pandas as pd

import tensorflow as tf
import numpy as np
import os
import time
import datetime
import data_helpers
import re
# from token_tv import no_accent_vietnamese
import os
import shutil
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text
from official.nlp import optimization 
from tensorflow.keras.models import load_model
path_model="italk.h5"
reloaded_model=load_model(path_model,custom_objects={'KerasLayer':hub.KerasLayer})
def kq(reloaded_model,examples):
    reloaded_results = tf.sigmoid(reloaded_model(tf.constant(examples)))
    return reloaded_results
def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    return s
app = Flask(__name__)             
@app.route('/', methods=['POST'])   
def test():
	# global res
	now = datetime.datetime.now()   
	r= request.form.to_dict()		
	print(r)
	u=list(r.keys())				
	tudien = json.loads(u[0])		
	uw = tudien["1"]
	ps_id=tudien["2"]   
	res=kq(reloaded_model,[no_accent_vietnamese(uw)])
	save=[int(res),str(uw),now.year, now.month, now.day, now.hour, now.minute, now.second]
	filename='database/info/'+str(ps_id)+'.csv'
	f = open(filename,"a",encoding='utf-8')
	luu = csv.writer(f, delimiter=',',lineterminator = '\n')
	luu.writerow(save)
	response = Response("{}".format(res[0][0]), content_type='text/plain')
	return response
@app.route('/signin', methods=['GET', 'POST'])
# Signin
def get_signin():
	tk =pd.read_csv('tk.csv')
	check =1
	if request.method == 'POST':
		username = request.form['fname']
		password = request.form['fpass']
	else:
		return render_template('signin.html')
	for i in range(len(tk)):
		if username == tk['tk'][i] and password == str(tk['pass'][i]):
			check=1
			break
		else:
			check=0
	if check==1:
		return redirect('https://fb-rec.herokuapp.com/')
	else:
		return redirect('/signin')
@app.route('/register', methods=['GET', 'POST'])
# Register
def get_register():
    return render_template('register.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('index.html')
app.run(host="0.0.0.0", port=80, debug=True)
