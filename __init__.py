# credentials
api_key = ""

#############
# imports
from concurrent.futures import thread
from tkinter import *
from flask import Flask
from subprocess import Popen
from datetime import datetime
from enum import Enum
#############
#vars 
class LogType(Enum):
    DEBUG = 1
    INFORMATION =2
    ERROR =3 
consoles = []
startupHTML="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            .container {
                width: 90em;
                overflow-x: auto;
                white-space: nowrap;
                height: 50em;
            }
            textarea{
                height: 500px;
                width: 95%;
                
            }
            p {
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <table>
                <thead>
                    THREQAD_CONTAIN
                </thead>
                
            </table>
        </div>
    </body>
</html>
"""
templateDiv = '''
<div>
  <p style="text-align:left;">[dt]
    <span style="float:right; padding-right: 10px; color:[cl]">
        [st]
    </span>
  </p>
  <hr>
  <textarea readonly>[da]</textarea>
</div><br>
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
##########################################################################################################################################################################
def startServer(port):
    app = Flask(__name__)
    @app.route('/')
    def home():
        consoles_parsed =""
        for consoleElement in consoles:
            consoleline = ""
            for line in consoleElement[1]:
                consoleline=consoleline+line+"\n"
            consoles_parsed=consoles_parsed+(templateDiv.replace("[dt]",consoleElement[0]).replace("[da]",consoleline).replace("[st]",consoleElement[2][0]).replace("[cl]",consoleElement[2][1]))
        return startupHTML.replace("THREQAD_CONTAIN",consoles_parsed)
    app.run(port=port)