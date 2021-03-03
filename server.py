from flask import Flask,render_template, request, flash,redirect,url_for
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from passlib.hash import sha256_crypt
import os
import shutil
import time

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blogsite'
app.config['SECRET_KEY'] = 'mysecret'

bcrypt = Bcrypt(app)
mysql = MySQL(app)

global user
global msg
global path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/error')
def error():
    global msg
    return render_template('error.html',msg=msg)

@app.route('/logout')
def logout():
    global user
    user = "none"
    return redirect(url_for('index'))

@app.route('/home')
def home():
    global user
    if(user is None or user == "none"):
        #flash('You need to be logged in to view home page!')
        global msg
        msg = "Authentication Error: You need to be Logged in to View this Page"
        return redirect(url_for('error'))

    img1 = os.path.join(app.config['UPLOAD_FOLDER'], "1.jpg")
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], "2.jpg")
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], "3.jpg")
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], "4.jpg")
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], "5.jpg")
    img6 = os.path.join(app.config['UPLOAD_FOLDER'], "6.jpg")
    return render_template('home.html', user=user,image1=img1,image2=img2,image3=img3,image4=img4,image5=img5,image6=img6)

@app.route('/search')
def search():
    global path
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    images = []
    for i in onlyfiles:
        if(i.endswith('.jpg')):
            images.append(i)
    target = os.path.join(app.config['UPLOAD_FOLDER'], images[0])
    img1 = os.path.join(path,images[0])
    shutil.copyfile(img1, target)
    target = os.path.join(app.config['UPLOAD_FOLDER'], images[1])
    img2 = os.path.join(path,images[1])
    shutil.copyfile(img2, target)
    target = os.path.join(app.config['UPLOAD_FOLDER'], images[2])
    img3 =os.path.join(path,images[2])
    shutil.copyfile(img3, target)
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], images[0])
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], images[1])
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], images[2])
    return render_template('search.html', user=user,image1=img1,image2=img2,image3=img3)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        query = "SELECT * from users where  user_name='{}'".format(username,password)
        cursor.execute(query)
        data = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()

        if(len(data)==0):
            #flash('No such user exists. Try again!')
            return redirect(url_for('index'))

        data = data[0]
        if(not sha256_crypt.verify(password, data[3])):
            #flash('Incorrect password!')
            return redirect(url_for('index'))

        global user
        user = {
            "user_name":data[0],
            "first_name":data[1],
            "last_name":data[2],
        }
        #flash('Successfully logged in')
        return redirect(url_for('home'))

@app.route('/register', methods = ['POST', 'GET'])
def reg():
    if request.method == 'GET':
        return "Register via the login Form"
     
    if request.method == 'POST':
        try:
            username = request.form['username']
            fname = request.form['fname']
            lname = request.form['lname']
            password = sha256_crypt.encrypt(request.form['password'])
            cursor = mysql.connection.cursor()
            query = "INSERT INTO users(user_name,first_name,last_name,password) VALUES('{}','{}','{}','{}')".format(username,fname,lname,password)
            cursor.execute(query)
            mysql.connection.commit()
            cursor.close()
            #flash('User Registered!')
            return redirect(url_for('index'))
        except Exception as e:
            #flash('Error Occured. Try again!')
            return redirect(url_for('signup'))

@app.route('/search',methods = ['POST', 'GET'])
def search_item():
    username = request.form['search-item']
    if(len(username)==0):
        return redirect(url_for('home'))
    file_path = os.path.join(os.getcwd(),'instagram-scraper','instagram_scraper','app.py')
    os.system("python {} {}".format(file_path,username))
    file_path = os.path.join(os.getcwd(),'instagram-scraper','instagram_scraper','result.txt')
    f = open(file_path)
    global msg
    lines = f.readlines()
    if(len(lines)==0):
        global path
        path = os.path.join(os.getcwd(),'instagram-scraper','data',username)
        return redirect(url_for('search'))
    else:
        lines = lines[0]
        if(lines=="private"):
            msg = "User account is private. Try another!"
        elif(lines=="non-existent"):
            msg="Account does not Exist. Try another!"
        return redirect(url_for('error'))
if __name__ == '__main__':
    global user
    global msg
    global path
    user = "none"
    msg = ""
    path = ""
    app.run(host='localhost', port=5000)
    