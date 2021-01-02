from flask import Flask, render_template, request, redirect, url_for, make_response
import time
from motion.motion_functions import RaspiMotion
move = RaspiMotion()
app = Flask(__name__) #set up flask server
#when the root IP is selected, return index.html page
@app.route('/')
def index():
    return render_template('index.html')
#recieve which pin to change from the button press on index.html
#each button returns a number that triggers a command in this function
#
#Uses methods from motors.py to send commands to the GPIO to operate the motors
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):
    changePin = int(changepin) #cast changepin to an int
    if changePin == 1:
        print("Left")
        move.left_move(3)
    elif changePin == 2:
        print("Forward")
        move.forward_move(3)
    elif changePin == 3:
        print("Right")
        move.right_move(3)
    elif changePin == 4:
        print("Reverse")
        move.backward_move(3)
    response = make_response(redirect(url_for('index')))
    return(response)
app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
