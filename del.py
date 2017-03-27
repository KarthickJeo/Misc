from flask import *
import sqlite3


app = Flask(__name__)

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE email_addresses1 ( email TEXT );")

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")

@app.teardown_request
def teardown_request(exception):
     if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')

@app.route('/emails.html')
def emails():
    email_addresses = g.db.execute("SELECT email FROM  email_addresses").fetchall()
    return email_addresses

if __name__ == "__main__":
    app.run(debug=True) 
