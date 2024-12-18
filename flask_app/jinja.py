from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to the course of flask."

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@ app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"    
    return render_template('result.html',results=res)

@ app.route('/successres/<int:score>')
def successfun(score):
    res=''
    if(score)>=50:
        res='Passed'
    else: res='Failed'    

    exp={'score':score,res:'res'}
    return render_template('index1.html',expression=exp)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success',score=total_score))

if __name__==('__main__'):
    app.run(debug=True)
