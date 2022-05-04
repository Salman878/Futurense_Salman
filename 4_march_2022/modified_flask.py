import webbrowser

from modified_tkinter import *
import flask
app=flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    app = tkinterApp()
    app.mainloop()




app.run()