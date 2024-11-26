from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi koneksi ke database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Ganti dengan username MySQL Anda
app.config['MYSQL_PASSWORD'] = ''  # Ganti dengan password MySQL Anda
app.config['MYSQL_DB'] = 'futsal_club'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM clubs")
    clubs = cur.fetchall()
    return render_template('index.html', clubs=clubs)

@app.route('/add', methods=['GET', 'POST'])
def add_club():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        capacity = request.form['capacity']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO clubs (name, location, capacity) VALUES (%s, %s, %s)", (name, location, capacity))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('index'))
    return render_template('add_club.html')

if __name__ == '__main__':
    app.run(debug=True)
