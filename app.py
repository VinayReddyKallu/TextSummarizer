import model
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('Home.html')

@app.route('/aboutus/')
def about_us():
    return render_template('aboutus.html')
    
@app.route('/hello',methods=['POST','GET'])
def output():
   if(request.method=="GET"):
       return render_template("Home.html")
      
   if(request.method=="POST"):
      document2=request.form.get('text')
      s=model.text_summarizer(document2)
      if(len(s)!=0):
         return render_template("output.html",name=s)
      else:
         return render_template("output2.html",name=s)
if __name__ == '__main__':
   app.run(debug = True)   
