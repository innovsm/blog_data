from flask import Flask, redirect, url_for, render_template, request
from spare_parts import *

# Initialize the Flask application

# app further configuration
app = Flask(__name__)
# =================================  all the bang-bang happens here =================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/admin")

def admin():
    return render_template("admin.html")
# all admin sites
@app.route("/admin/projects", methods = ['GET', 'POST'])

def projects():
    if(request.method == "POST"):
        
        project_name = request.form.get('project_name')
        project_link = request.form.get('project_link')
        image_link = request.form.get('image_link')
        description = request.form.get('description')

        print(description)
        data = add_project(description,project_name, image_link, project_link)
        return list(data)
  
    else:
        return render_template("projects.html")

@app.route("/project") # by default it is GET request
def project_getter():
    data_1 = get_projects()
    return render_template("my_projects.html",data_1 = data_1)



@app.route("/about")
def about_section():
    return render_template("about.html")

# ----------------------------------------[BLOG AREA] ----------------------------------------------------
@app.route("/thoughts",methods = ['GET', 'POST'])

def form():
    if request.method == 'POST':
        try:
            text_data = request.form.get('thought')
            text_data = str(text_data)
            text_data = text_data.lower()
            add_thought(text_data)
            return text_data
        except:
            return "error"
    else:
        return render_template("thoughts.html")


@app.route("/admin/blog_delete", methods=["POST"])
def delete_blog():
    if(request.method == "POST"):
        blog_id = request.form.get('blog')
        print(blog_id)
        #blog_id = int(blog_id)
        #delete_blog_1(blog_id)
        return redirect(url_for("admin"))
    else:
        return "error"
    
@app.route("/blogs")

def blog_data():
    final_list = get_blogs()
    return render_template("blogs.html",final_list = final_list)






if __name__ == "__main__":
    app.run(debug=True)
