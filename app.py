from flask import Flask, flash, redirect, render_template, request, session, abort
import pprint
p = pprint.PrettyPrinter()

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template('index.html')
 
if __name__ == "__main__":
    app.run()
