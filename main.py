from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import validators
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
    pub_date = db.Column(db.DateTime)
    deleted = db.Column(db.Boolean)

    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.deleted = False

    def __repr__(self):
        return '<Blog %r>' % self.title



@app.route('/', methods=['GET'])
def index():
    return redirect('/blog')



@app.route('/blog', methods=['GET'])
def blog():
    blogs = Blog.query.filter_by(deleted=False).all()
    blogs_ordered_most_recent = Blog.query.filter_by(deleted=False).order_by(desc(Blog.pub_date)).all()
    deleted_blogs = Blog.query.filter_by(deleted=True).all()

    blog_id = request.args.get('id')

    if blog_id:
        indv_blog = Blog.query.get(blog_id)
        return render_template('individualblog.html',title="Build a Blog!", blogs=blogs, blog=indv_blog)
    else:
        #return render_template('blog.html',title="Build a Blog!", blogs=blogs, deleted_blogs=deleted_blogs)
        return render_template('blog.html',title="Build a Blog!", blogs=blogs_ordered_most_recent, deleted_blogs=deleted_blogs)




@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blog_title = request.form['blogTitle']
        blog_body = request.form['blogBody']
       
        titleError = validators.validateTitle(blog_title)
        bodyError = validators.validateBody(blog_body)

        if not titleError and not bodyError:
            new_blog = Blog(blog_title,blog_body)
            db.session.add(new_blog)
            db.session.commit()
            #return redirect('/blog')
            return redirect('./blog?id={0}'.format(new_blog.id))

        else:
            return render_template('newpost.html',title="Build a Blog! | New entry", blogTitle= blog_title, blogBody= blog_body, titleError= titleError, bodyError= bodyError)

    else:
        return render_template('newpost.html',title="Build a Blog! | New entry")
     
     

@app.route('/delete-entry', methods=['POST'])
def delete_entry():

    #task_id = int(request.form['task-id'])
    #task = Task.query.get(task_id)
    #task.completed = True
    #db.session.add(task)
    #db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()