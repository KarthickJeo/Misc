from flask import Flask , render_template , request , redirect , url_for , session , flash , g
import sqlite3

app =  Flask(__name__)
app.secret_key = 'hhkhg'
app.database = 'sample.db'
app.database2 = 'sales.db'


def connect_db():
    return sqlite3.connect(app.database)

def connect_sales_db():
    return sqlite3.connect(app.database2)

@app.route('/')
def home():
    g.db = connect_db()
    cursor = g.db.execute('select * from posts')
    posts = [dict (title=row[0], description=row[1]) for row in cursor.fetchall()]
    g.db.close()
    return render_template('index.html' , posts = posts)

@app.route('/sales')
def sales():
    g.db = connect_sales_db()
    cursor = g.db.execute('select * from sales')
    sales_db = [dict(Company_name=row[0],Engagement_type=row[1], Current_Stage=row[2],Sales_Person_Name=row[3] , Closing_Date=row[4]) for row in cursor.fetchall()]
    g.db.close()
    return render_template('sales.html', sales = sales_db)


@app.route('/welcome')
def welcome ():

    return render_template('welcome.html')

@app.route ('/login', methods=['GET' , 'POST'])
def login ():
    error = None
    if request.method == 'POST':
        if request.form ['username'] != 'admin' or request.form ['password'] != 'admin' :
            error  = 'invalid'

        else :
            session['logged_in'] = True
            flash('You have loggedin')
            return redirect (url_for('home'))
    return render_template('login.html', error = error)

@app.route('/logout')
def logout ():
    session.pop('logged_in' , None)
    flash('You have loggedout')
    return redirect(url_for('welcome'))


def init_db():
    with app.app_context():
        db = get_db()
    with app.open_resource('new.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()


if __name__ == ("__main__"):
    app.run(debug=True)
