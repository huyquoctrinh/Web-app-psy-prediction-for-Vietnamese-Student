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
from text_cnn import TextCNN
from tensorflow.contrib import learn
import re
# from token_tv import no_accent_vietnamese

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
def kqua_predict(x_raw):
    y_test=[1,0]
    vocab_path = os.path.join("../tfc/runs/1614581460/",  "vocab")
    vocab_processor = learn.preprocessing.VocabularyProcessor.restore(vocab_path)
    x_test = np.array(list(vocab_processor.transform(x_raw)))

    print("\nEvaluating...\n")

    # Evaluation
    # ==================================================
    checkpoint_file = tf.train.latest_checkpoint("../tfc/runs/1571067668/checkpoints/model-30000")
    graph = tf.Graph()
    with graph.as_default():
        session_conf = tf.ConfigProto(
          allow_soft_placement=True,
          log_device_placement=False)
        sess = tf.Session(config=session_conf)
        with sess.as_default():
            # Load the saved meta graph and restore variables
            # saver = tf.train.import_meta_graph("{}.meta".format(checkpoint_file))
            # saver.restore(sess, checkpoint_file)
            saver = tf.compat.v1.train.import_meta_graph("{}.meta".format("./runs/1614581460/checkpoints/model-6000"))
            saver.restore(sess, "./runs/1614581460/checkpoints/model-6000")
            # Get the placeholders from the graph by name
            input_x = graph.get_operation_by_name("input_x").outputs[0]
            # input_y = graph.get_operation_by_name("input_y").outputs[0]
            dropout_keep_prob = graph.get_operation_by_name("dropout_keep_prob").outputs[0]

            # Tensors we want to evaluate
            predictions = graph.get_operation_by_name("output/predictions").outputs[0]

            # Generate batches for one epoch
            batches = data_helpers.batch_iter(list(x_test), 8, 1, shuffle=False)

            # Collect the predictions here
            all_predictions = []

            for x_test_batch in batches:
                batch_predictions = sess.run(predictions, {input_x: x_test_batch, dropout_keep_prob: 1.0})
                all_predictions = np.concatenate([all_predictions, batch_predictions])

    # Print accuracy if y_test is defined
    if y_test is not None:
        correct_predictions = float(sum(all_predictions == y_test))
        print("Total number of test examples: {}".format(len(y_test)))
        print("Accuracy: {:g}".format(correct_predictions/float(len(y_test))))

    # Save the evaluation to a csv
    predictions_human_readable = np.column_stack((np.array(x_raw), all_predictions))
    print(predictions_human_readable)
    return all_predictions[0]
# from dominate import document
# from dominate.tags import *
# USERNAME = 'admin'	# define username
# PASSWORD = 'admin' #define password
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
	res=kqua_predict([no_accent_vietnamese(uw)])
	# print(raw)				
	# ps_id=tudien["2"]				
	# filename='database/info/'+str(ps_id)+'.csv'
	# fileanh='static/'+str(ps_id)+'.png'
	# f = open(filename,"a")
	# luu = csv.writer(f, delimiter=',',lineterminator = '\n')
	# print(res)
	# save=[int(res),str(uw),now.year, now.month, now.day, now.hour, now.minute, now.second]		
	# luu.writerow(save)
	# f=open(filename,'r')
	# a = []
	# b = []
	# kq = csv.reader(f, delimiter=',')
	# for rows in kq:
	# 	a.append(int(rows[0]))
	# 	b.append(str(rows[4])+'/'+str(rows[3])+','+str(rows[5])+':'+str(rows[6])+':'+str(rows[7]))
	# print(a)
	# print(b)
	# #create graph and save
	# kq="nguoi dung id: "+str(ps_id)
	# plt.figure(figsize=(30,10))
	# plt.plot(b,a)

	# plt.xlabel('ngay')
	# plt.ylabel('danh gia')
	# # print(a)
	# plt.title(kq) 
	# plt.savefig(fileanh)
	response = Response("{}".format(res), content_type='text/plain')
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
		return redirect('https://chat-fb-bot.herokuapp.com/?fbclid=IwAR2VRvg_jfVuML-0VNLPJUeFST-OqoyS7xrMTYlwP-nt_Xm3FZPdfkVkiEc')
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