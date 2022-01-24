#file name app.py = don't need to set up FLASK_APP enviorment variable

import os
import argparse
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#create instane of Flask class
#__name__ needed do Flask knows where to look for resources (templates & static files)
# invalid import name: FLASK_APP enviorment = name of module to import at flask run
#here it is app
app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    """A dummy doctring."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    
    def pub1(self):
        """A dummy docstring."""
        print("")
        
    def pub2(self):
        """A dummy docstring."""
        print("")
   

#route() binds a function to a URL     
@app.route("/edit")
def home1():
    """A dummy docstring."""
    #query attribute, with methods like filter() all() first() get()4
    #query all to do list entries
    todo_list = Todo.query.all()
    #render_template is used to generate output from a template file 
    
    #renders base.html for /edit
    return render_template("base.html", todo_list=todo_list)
    
@app.route('/')
def list1():
    todo_list = Todo.query.all()
    
    #renders list.html for /
    return render_template('list.html', todo_list = todo_list)

 
 #on edit page, 3 buttons for add, update and delete 
 #functions for these 3 are defined below 
    
@app.route("/add", methods=["POST"])
def add():
    """A dummy docstring."""
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    #everything function returns is applied to the url associated with home1 function
    #which is /edit
    return redirect(url_for("home1"))
    
@app.route("/update/<int:todo_id>")
def update(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home1"))
    
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    """A dummy docstring."""
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home1"))

@app.route("/")
def returnHome():
    """A dummy docstring."""
   

    return  redirect(url_for("home1"))

        
if __name__ == "__main__":
    db.create_all()
    port = int(os.environ.get('PORT',500))
    app.run(host='0.0.0.0', port=port, debug=True) 
        
    app.run(debug=True) 
