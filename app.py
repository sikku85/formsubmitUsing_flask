from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/manjitForm'
db = SQLAlchemy(app)

class form(db.Model):
   sno= db.Column( db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))  
   pin = db.Column(db.String(10))

@app.route('/',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):

        name=request.form.get('name')
        city=request.form.get('city')
        pin=request.form.get('pin')
        entry= form(name=name,city=city,pin=pin)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')

if __name__== "__main__":
    app.run(debug=True)