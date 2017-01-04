import os, requests, json


POST_COMMAND_URL = "http://localhost:5000/decode_command"
POST_MODULE_URL  = "http://localhost:5000/execute_func"

while True:
	input_query = raw_input("Query : ")

	headers     = {"Content-type": "application/json"}

	data        = json.dumps({"command":input_query})
	request_obj = requests.post(POST_COMMAND_URL, data=data, headers=headers)

	data        = json.dumps({"module":request_obj.text})
	request_obj = requests.post(POST_MODULE_URL, data=data, headers=headers)