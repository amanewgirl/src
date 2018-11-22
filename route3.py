import os
from flask import Flask, redirect, url_for, abort,render_template, send_from_directory, request, session
from flask_socketio import SocketIO, send
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)



#socketio room test
@app.route('/tes')
def tes():
	socketio.emit('server originated', 'server stuf')
	return 'sent'



@socketio.on('join')
def on_join(msg):
    #username = data['username']
    #room = msg['room']
    
    room = "toom"
    print(room)
    #print('msg '+ msg)
    join_room(room)
    print("success")
    send('has entered the room.', room=room)
    #emit('status', {'msg'+' has entered the room.'}, room=room)
    


@socketio.on('leave')
def on_leave(msg):
    username = msg['username']
    room = msg['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


#socketio code to handle messages
@socketio.on('message')
def handleMessage(msg):
   print('Message:' +msg)
   send(msg, broadcast=True)


#this is the base Design across the web app
def design():
    return render_template ('design.html')

#Chat
@app.route("/")
def index():
	return render_template('debateInstructions.html')

@app.route('/debate')
@app.route('/debate/<player>')
def debate(player=None):
	return render_template ('boardFinal.html', player=player) 

#error pages	
@app.errorhandler (404)
def page_not_found (error):
	return render_template ('tryagain.html')



if __name__ =="__main__":
     app.run(host='0.0.0.0')
     socketio.run(app, host='0.0.0.0')