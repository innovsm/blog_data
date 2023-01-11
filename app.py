from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import mysql.connector
import datetime
# Initialize the Flask application
app = Flask(__name__)
# =================================  all the bang-bang happens here =================================


@app.route('/')  # main blog site

def blog_data():  # giving all the  blogs

    conn = mysql.connector.connect( 
        host="sql6.freesqldatabase.com",
        user="sql6589077",
        password="BEK9Q8jdGE",
        database="sql6589077" 
        )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_data")
    data = cursor.fetchall()
    return render_template("index.html",data_list = data[::-1])
    


@app.route('/superuser_1', methods = ['GET', 'POST'])
def superuser_1():
    if request.method == 'POST':   #  cheching for particular username and password , only avilable for admin
        username = request.form['username']
        password = request.form['password']
        if((username == "admin") and (password == "admin")):
            conn = mysql.connector.connect( 
                host="sql6.freesqldatabase.com",
                user="sql6589077",
                password="BEK9Q8jdGE",
                database="sql6589077" 
                )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM blog_data")
            data = cursor.fetchall()
            data_1 = pd.DataFrame(data,columns = ['text','topice','date'])
            data_1.to_csv('blog_data.csv')
            return render_template("blogger_main.html")
    else:
        return "fatal error had occurred !"
        

@app.route('/insert',methods = ['POST','GET'])

def insert():
    if request.method == 'POST':
        data_1 = request.form.get('category')
        data_2 = request.form['blog_data']
        date_index = str(datetime.datetime.today().date())
        # connecting to mysql server
        conn = mysql.connector.connect( 

            host="sql6.freesqldatabase.com",
            user="sql6589077",
            password="BEK9Q8jdGE",
            database="sql6589077"
            
            )
        cursor = conn.cursor()
        query = "INSERT INTO blog_data (text,topice,date_1) VALUES (%s,%s,%s)"
        values  = (data_2,data_1,date_index)
        try:
            cursor.execute(query,values)
            conn.commit()
            cursor.close()
            return "data successfully inserted, hurray!!"
        except:
            return "data was not inserted , sorry!"





@app.route('/edit',methods = ['GET', 'POST'])

def edit():

    if request.method == 'POST':
        target_blog = request.form.get('date')
        new_text = request.form['new_text']  # acutually this is blog text
        try:
            delete_boolean = request.form['delete']
        except:
            delete_boolean = "no"
        new_topice = request.form['topice']
        # core logic for editing will come here
        conn = mysql.connector.connect(

            host="sql6.freesqldatabase.com",
            user="sql6589077",
            password="BEK9Q8jdGE",
            database="sql6589077"

        )
        if(delete_boolean == "yes"):
            cursor = conn.cursor()
            query = "DELETE FROM blog_data WHERE text = %s"
            values = (target_blog,)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            return "DELETION SUCCESSFULL"

        else:
            cursor = conn.cursor()
            query = "UPDATE blog_data SET text = %s ,topice = %s WHERE text =  %s "
            values = (new_text, new_topice,target_blog)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            return "Article updated successfully !!"

    else:
        data_1 = pd.read_csv("blog_data.csv")
        data = list(data_1['text'])
        return render_template('edit.html',date_list = data)

@app.route('/superuser', methods = ['GET', 'POST'])
def user():
    return render_template('alfa.html')



if __name__ == "__main__":
    app.debug = False
    app.run()