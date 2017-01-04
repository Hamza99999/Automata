from flask import Flask, render_template, request
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
    print decode_command("what is the time?")


#-----------------------------------------------------------------------------
# This route is accessed when the application starts. 
#-----------------------------------------------------------------------------
@application.route('/')
def index():
	return "Working"


if __name__=='__main__':
	_run_on_start()
	application.run(debug=True, use_reloader=False)