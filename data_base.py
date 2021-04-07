
from flask import Flask,redirect,url_for,render_template,request,session,flash

from datetime import timedelta
import sqlalchemy 

app=Flask(__name__)

app.secret_key="hello"

app.permanent_session_lifetime = timedelta(minutes=5)           


@app.route("/")
def home():
	return render_template("inherited.html",content="name")

	
	
@app.route("/login",methods=["POST","GET"])
def login():
	if request.method=="POST":
		session.permanent=True
		user=request.form["nm"]
		session["user"]=user
		flash("you have successfully logged in,","info")
		return redirect(url_for("user"))
	else : 
		if "user"in session:
			flash("you have already logged in","info")
			return redirect(url_for("user"))
		else:	
			return render_template("login.html")	
	
	
	
@app.route("/user",methods=["POST","GET"])
def user(): 
	email=None
	if "user"in session:
		user=session["user"]
		
		if request.method =="POST":
			email=request.form["email"]
			session["email"]=email
			flash("your email is saved")
		else:
			if "email" in session:
				email=session["email"]
		return render_template("user2.html",email=email) 	
	else :
		flash("you are not logged in")
		return redirect(url_for("login"))
	

	
@app.route("/logout")		
def logout():

	flash("you have successfully logged out")
		
	session.pop("user",None)
	session.pop("email",None)
	return redirect(url_for("login"))

		
if __name__=='__main__':
		app.run(debug=True)