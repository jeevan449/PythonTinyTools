from flask import Flask, url_for, jsonify
from flask import Response,request
import random
import requests
import threading,time


app = Flask(__name__)
def answer(url):
	time.sleep(2)
	# url.replace('CallStatus=in-progress','CallStatus=in-progress')
	# res = requests.get(url)
	print ('executed api')
def ringingapi(url):
	time.sleep(2)
	res = requests.get(url)
	
def hangup(url):
	time.sleep(10)
	res = requests.get(url)

def getRandom_number():
	return str(random.randint(10000000,90000000))+"-"+str(random.randint(1000,9000))+"-"+str(random.randint(1000,9000))+"-"+str(random.randint(1000,9000))+"-"+str(random.randint(100000000000,900000000000))


@app.route('/v1/Account/<authid>/Call/', methods = ['POST'])
def api_call(authid):
	try:
		print (request.headers)
		answer_url = request.form['answer_urls']	
		responsedata={"message": "call fired","request_uuid": getRandom_number(),"api_id": "97ceeb52-58b6-11e1-86da-77300b68f8bb"}
		res = jsonify(responsedata)
		res.status_code = 200
		# t = threading.Thread(target = ringingapi , args=(ringing_url,))
		t = threading.Thread(target = answer , args=(answer_url,))
		# t = threading.Thread(target = hangup , args=(hangup_url,))
		t.start()
		return res
	except Exception as e:
		raise e


@app.route('/v1/Account/<auth_id>/Conference/<conference_name>/', methods = ['GET','POST','DELETE'])
def api_conference(auth_id,conference_name):
	try:
	    if request.method == 'GET':
	    	conf_details = {"conference_name": "My Conf Room","conference_run_time": "590","conference_member_count": "1","members": [{"muted" : 'false',"member_id" : "17","deaf" : 'false',"from" : "1456789903","to" : "1677889900","caller_name" : "John","direction" : "inbound","call_uuid" : "acfbf0b5-12e0-4d74-85f7-fce15f8f07ec","join_time" : "590"}],"api_id": "816e903e-58c4-11e1-86da-adf28403fe48"}
	    	res = jsonify(conf_details)
	    	res.status_code = 200
	    	return res

	    elif request.method == 'POST':
	    	pass
	    elif request.method == 'DELETE':
	    	dele_conf = {"message":"conference hung up", "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"}
	    	res = jsonify(dele_conf)
	    	# print (dele_conf)
	    	res.status_code = 204
	    	print (res)
	    	return res
	except Exception as e:
		raise e
# @app.route('/Account/<authid>/Call', methods = ['POST'])
# def api_call(authid):
#     try:
#         return res
#     except Exception as e:
#         raise e



@app.route('/Account/<auth_id>/Call/<call_uuid>', methods = ['DELETE'])
def api_hangup(auth_id,call_uuid):
	try:
		print (request.form)
		return 
	except Exception as e:
		raise e


@app.route('/getusername/<username>')
def api_getuser(username):
	dt = {'username':username}
	return jsonify(dt)

if __name__ == '__main__':
    # app.debug = True
    app.run(host = '0.0.0.0')
