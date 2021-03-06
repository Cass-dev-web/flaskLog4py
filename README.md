
# ![flaskLog4py](https://user-images.githubusercontent.com/60286224/152668279-b086bd03-bfad-415b-b872-becffb4f8c8a.png)

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/ParentProfanities/flaskLog4py/blob/master/LICENSE)
[![Free Cookies](https://img.shields.io/badge/free-cookies-green)](https://letmegooglethat.com/?q=Cookie+Clicker)
  
An easy to use flask-driven python thread logger. Not the best of it's market but useful if nothing else is applicable.

## Authors

- [@ParentProfanities](https://github.com/ParentProfanities)

## Usage/Examples

```python
import threading
import flaskLog4py
import time

def thr():
  console_1 = flaskLog4py.newConsole("Thread1")
  time.sleep(5)
  flaskLog4py.addLine(console_1,"Testing", flaskLog4py.LogType.DEBUG)
  flaskLog4py.changeStatus(console_1,"ended","red") 
x = threading.Thread(target=thr)
x.start()
flaskLog4py.startServer(3000,2500,None) // Starts the server on 127.0.0.1:3000
```
Then, once ran, go on: `localhost:3000`

## Logging types (`flaskLog4py.LogType`)

| Type             | Python Enumeration Reference| Code             |
| ----------------- | ---------- |----------
| Debug | 1 | `flaskLog4py.LogType.DEBUG` |
| Information | 2| `flaskLog4py.LogType.INFORMATION` |
| Error |  3|   `flaskLog4py.LogType.ERROR`|

## Colors (`changeStatus(consoleID, text, color)`)

For the color argument, you can just put a color that would usually be supported by the `color:` style in CSS/HTML.  
We recommend you use [htmlcolorcodes.com](https://htmlcolorcodes.com/).

## Documentation

| Function             | Syntax | Returns | Description
| ----------------- | ---------- |---------- | ----------
|startServer|`startServer(port, delay, ip[SET TO None FOR LOCALHOST],debugMode)`| Null |Starts the server to a dedicated port and with a dedicated delay between refreshes. If IP is set to `None`, it will start the server on 127.0.0.1 (`localhost`).
|newConsole|`newConsole(threadName)`|Console ID|Creates a new logging area using a name and then returns a console ID to be used for functions such as `changeStatus` and `addLine`.
|addLine|`addLine(consoleID, message, type)`| Null | Adds output line to a designated console/logging area. Refer to logging types.
|changeStatus|`changeStatus(consoleID, text, color)`| Null | Changes the text next to the console name, for example: "Verifying request...", "Getting API status..." etc. Refer to the colors section.
|renameConsole|`renameConsole(consoleID, name)`| Null | Changes the name of a designated console.

## Dependencies

| Name                       | PIP command                                          |
|----------------------------|------------------------------------------------------|
| tkinter (Tkinter for py 2) | pip install tk                                       |
| flask                      | [pip install flask](https://pypi.org/project/Flask/) |
| enum                       | [pip install enum](https://pypi.org/project/enum/)                                  |
| DateTime                   | [pip install DateTime](https://pypi.org/project/DateTime/)                           |
| Logging                    | *N/A*                                                |
## How it works

When doing startServer(...), it creates a new flask app and starts running it either locally or on a dedicated and specified IP adress and port. Then, you're able to access that, it will most likely say that it cannot find any consoles to display, to display a console, you need to create one. You can do that by doing newConsole(...), which will return and ID, then, on the website, it's javascript code keeps checking for new consoles dynamically. That means that when stopping your code and restarting it, you won't have to refresh the tab. Then with the console ID, you can add a line or change a threads status and status color. You can find more details in the code.

## Optimisations

If you feel the need to optimise this project, dont be scared to add your own features.
## License

[MIT](https://choosealicense.com/licenses/mit/)

