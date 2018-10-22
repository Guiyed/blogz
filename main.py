from flask import Flask, request, redirect, render_template, session, flash
from sqlalchemy import desc
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import desc
import validators
from app import app, db
from models import Blog, User

@app.route('/', methods=['GET'])
def index():
    #users = Blog.query.order_by(User.username).all()
    users = User.query.order_by(User.username).all()
    return render_template('index.html',title="Blogz | Home ", users=users)  



@app.route('/blog', methods=['GET'])
def blog():
    
    username = request.args.get('user')
    #print('username : ',username)
    
    if username:
        currentUser = User.query.filter_by(username=username).first()
        user_id = currentUser.id
        #print("........id........: ",user_id)
        blogs = Blog.query.filter_by(deleted=False,owner_id = user_id).all()
        blogs_ordered_most_recent = Blog.query.filter_by(deleted=False,owner_id = user_id).order_by(desc(Blog.pub_date)).all()
        deleted_blogs = Blog.query.filter_by(deleted=True,owner_id = user_id).all()

        return render_template('userposts.html',title="Blogz | Posts", blogs=blogs_ordered_most_recent, deleted_blogs=deleted_blogs, user=currentUser)

    else:
        username=''
        blogs = Blog.query.filter_by(deleted=False).all()
        blogs_ordered_most_recent = Blog.query.filter_by(deleted=False).order_by(desc(Blog.pub_date)).all()
        deleted_blogs = Blog.query.filter_by(deleted=True).all()

    blog_id = request.args.get('id')

    if blog_id:
        indv_blog = Blog.query.get(blog_id)
        return render_template('individualblog.html',title="Blogz | Post", blogs=blogs, blog=indv_blog)
    else:
        #return render_template('blog.html',title="Build a Blog!", blogs=blogs, deleted_blogs=deleted_blogs)
        return render_template('blog.html',title="Blogz | Posts", blogs=blogs_ordered_most_recent, deleted_blogs=deleted_blogs)



@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blog_title = request.form['blogTitle']
        blog_body = request.form['blogBody']
       
        titleError = validators.validateTitle(blog_title)
        bodyError = validators.validateBody(blog_body)

        if not titleError and not bodyError:
            #add owner to blog
            owner = User.query.filter_by(username=session['user']).first()    

            new_blog = Blog(owner, blog_title,blog_body)
            db.session.add(new_blog)
            db.session.commit()
            #return redirect('/blog')
            return redirect('./blog?id={0}'.format(new_blog.id))

        else:
            return render_template('newpost.html',title="Blogz | New post", blogTitle= blog_title, blogBody= blog_body, titleError= titleError, bodyError= bodyError)

    else:
        return render_template('newpost.html',title="Blogz | New post")
     
     

@app.route('/delete-entry', methods=['POST'])
def delete_entry():

    #task_id = int(request.form['task-id'])
    #task = Task.query.get(task_id)
    #task.completed = True
    #db.session.add(task)
    #db.session.commit()

    return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user'] = user.username
            flash("Logged in",'success')
            return redirect('/newpost')
        elif not user:
            flash('User does not exist', 'warning')
            return redirect('/login')
        else:
            flash('User / password combination is incorrect', 'warning')
            return redirect('/login')
    return render_template('login.html',title='Blogz | Login')


@app.route('/signup', methods = ['POST', 'GET'])
def signup():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        retypepass = request.form['retypepass']

        # Validate user's data
        usernameError = validators.validateUsername(username)
        passwordError = validators.validatePassword(password)
        retypeError = validators.validateRetype(password,retypepass)
        emailError = validators.validateEmail(email)


        if not usernameError and not passwordError and not retypeError and not emailError:
            
            existing_user = User.query.filter_by(username=username).first()

            if not existing_user:
                new_user = User(username,password,email)
                db.session.add(new_user)
                db.session.commit()
                # "Remember" the user
                session['user'] = new_user.username
                flash("Signed in",'success')
                return redirect('/newpost')
            else:               
                flash("Duplicated User, please try again",'error')
                return redirect('/signup')

        else:
            flash("One or more Fields are invalid, please try again",'warning')
            return render_template('signup.html',title='Blogz | Signup', username= username, email= email, usernameError= usernameError, passwordError= passwordError, retypeError= retypeError, emailError= emailError)
        
    return render_template('signup.html', title='Blogz | Signup')


@app.route('/logout')
def logout():
    if session:
        del session['user']
        flash("Logged Out",'success')
    return redirect('/blog')


@app.before_request
def require_login():
  allowed_routes = ['login','blog', 'index', 'signup','static']
  if request.endpoint not in allowed_routes and 'user' not in session:
    return redirect('/login')



if __name__ == '__main__':
    app.run()