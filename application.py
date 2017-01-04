from flask import Flask, request, json
from CommandClassifier import decode_command, init


application            = Flask(__name__)
application.secret_key = "Automata#secure#Key"


#-----------------------------------------------------------------------------
# This function loads the classifier data and configures the system to
# be ready to use.
#-----------------------------------------------------------------------------
def _run_on_start():
    print " * Loding files..."
    init()


#-----------------------------------------------------------------------------
# This route is accessed when the application starts. 
#-----------------------------------------------------------------------------
@application.route('/')
def index():
	return "Working"


#-----------------------------------------------------------------------------
# Commands are sent to this route via POST 
#-----------------------------------------------------------------------------
@application.route('/decode_command', methods=['POST'])
def decode_command_post():
	command = request.json['command']
	return decode_command(command) 


if __name__=='__main__':
	_run_on_start()
	application.run(debug=True, use_reloader=False)