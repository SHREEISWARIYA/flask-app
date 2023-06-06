
from flask import Flask ,render_template,request
app= Flask(__name__)
import pymysql

def connector():
    conn=pymysql.connect(db='project',host='localhost',user='root',password='Pr@th!k$h@2')
    c=conn.cursor()
    return conn,c

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/home')
def home2():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/tour')
def tour():
    return render_template("tour.html")
@app.route('/destination')
def destination():
    return render_template("destination.html")
@app.route('/blog')
def blog():
    return render_template("blog.html")
@app.route('/form',methods=['POST','GET'])
def form():
    if request.method=='POST':
        name=request.form.get('name')
        phone=request.form.get('phone')
        fr=request.form.get('from')
        to=request.form.get('to')
        date=request.form.get('date')
        count=request.form.get('count')
    #     date_obj = date.strptime(date, '%Y-%m-%d')

    # # Convert datetime object to SQL date format
    #     sql_date = date_obj.strftime('%Y-%m-%d')
        conn, c = connector()
        c.execute("INSERT INTO booking VALUES ('{}','{}','{}','{}','{}',{})".format(
           name,phone,fr,to,date,count))
        conn.commit()
        conn.close()
        c.close()
        print(name,phone,fr,to,date,count)
    return render_template('form.html')   
if __name__=="__main__":
    app.debug=True
    app.run()
