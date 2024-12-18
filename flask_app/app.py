from flask import Flask,render_template

## WSGI appln
app=Flask(__name__)

## creating home page
@ app.route("/")
def home():
    return render_template("index.html")

@ app.route("/index")
def index():
    return render_template('welcome.html')
@ app.route("/second")
def second_page():
    return "this is the second page our app."

@ app.route("/form",methods=['GET','POST'])
def form():
    return render_template('form.html')



if __name__=="__main__":
    app.run(debug=True)