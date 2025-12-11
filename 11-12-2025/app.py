#Imports
from flask import Flask, render_template, request, redirect
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#My app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class MyTask(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100),nullable=False)
    completed = db.Column(db.Boolean,default=False)
    created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return f"Task {self.id}"

#Routes to webpages

#Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
#Add Tasks
    if request.method == 'POST':
        current_task = request.form['content']
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
#See current tasks
    else:
        tasks= MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)

#Delete tasks
@app.route('/delete/<int:id>')
def delete(id:int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f"ERROR: {e}")
        return f"ERROR: {e}"

#Update tasks
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"
    else:
        return render_template('update.html', task=task)


#Runner and Debugger
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)