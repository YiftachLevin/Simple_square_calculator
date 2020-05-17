from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['Select Integer']
      try:
         squared_result = int(result)*int(result)
         results = (f"Number:  {result} , Squared Number:  {squared_result}")
         return render_template("result.html",result = results)

      except ValueError:
         return render_template('student.html')

@app.route('/',methods = ['POST', 'GET'])
def select_int():
   if request.method == 'POST':
      return render_template('student.html')

if __name__ == '__main__':
   app.run(debug = True)