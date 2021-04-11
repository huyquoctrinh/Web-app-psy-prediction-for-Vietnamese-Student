from flask import Flask, render_template, request, jsonify,Response
import numpy as np
import jsonpickle
from module import predict
app = Flask(__name__)
@app.route('/', methods=['POST'])
def test():
    raw=[]
    r= request.form.to_dict()
    # u=r[0]['1']
    # u=r['1']
    # r = request.form.getlist('1')
    raw=list(r.keys())
    # raw.append(str(r))
    res=predict(raw)

    # encode response using jsonpickle
    print(res)
    # response_pickled = jsonpickle.encode(response)
    response = Response("{}".format(res), content_type='text/plain')
    return response
app.run(host="0.0.0.0", port=80, debug=True)