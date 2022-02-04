# imports
from tkinter import *
from tracemalloc import start
from turtle import delay
from flask import Flask
import flask
from datetime import datetime
import logging
from enum import Enum
#############
#vars 
class LogType(Enum):
    DEBUG = 1
    INFORMATION =2
    ERROR =3 
consoles = []
templateDiv = '''
<div><p style="text-align:left;">[dt]<span style="float:right; padding-right: 10px; color:[cl]">[st]</span></p><hr><textarea readonly>[da]</textarea></div><br>
'''
########## fun
def newConsole(threadName):
  consoles.append([threadName,[f"Started {threadName}."],["Starting...","orange"]])
  return len(consoles)-1
def addLine(consoleNum, line, type):
  time= datetime.now().strftime("%H:%M.%S")
  consoles[consoleNum][1].append(f"[{time}] [{type.name}]: {line}")
def changeStatus(consoleNum,text,color):
  consoles[consoleNum][2][0]=text
  consoles[consoleNum][2][1]=color
##########################################################################################################################################################################\
def calculateConsolesHTML():
    consoles_parsed =""
    for consoleElement in consoles:
        consoleline = ""
        for line in consoleElement[1]:
            consoleline=consoleline+line+"\n"
        consoles_parsed=consoles_parsed+(templateDiv.replace("[dt]",consoleElement[0]).replace("[da]",consoleline).replace("[st]",consoleElement[2][0]).replace("[cl]",consoleElement[2][1]))
    return consoles_parsed
def startServer(port,delay,ip,debugMode):
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app = Flask(__name__)
    @app.route('/')
    def home():
        return flask.render_template("startupHTML.HTML").replace("[tm]",str(delay))
    @app.route('/consoles')
    def getConsoles():
        return calculateConsolesHTML()
    if ip == None:
        ip="127.0.0.1"
    app.run(host=ip, port=port, debug=False)
