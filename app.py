from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import datetime
# Initialize the Flask application
app = Flask(__name__)
# =================================  all the bang-bang happens here =================================

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.debug = False
    app.run()
