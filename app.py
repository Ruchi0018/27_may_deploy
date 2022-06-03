# import a lib
from flask import Flask,render_template,request
import joblib

#instance of an app
app=Flask(__name__)

#load the model
model=joblib.load('diabetic_79.pkl')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data',methods=['POST'])
def data():

    preg=request.form.get('preg')
    plas=request.form.get('plas')
    pres=request.form.get('pres')
    skin=request.form.get('skin')
    test=request.form.get('test')
    mass=request.form.get('mass')
    pedi=request.form.get('pedi')
    age=request.form.get('age')

    print(preg)
    print(plas)
    print(pres)
    print(skin)
    print(test)
    print(mass)
    print(pedi)
    print(age)

    result=model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if result[0]==1:
      output='person is diabetic'
    else:
      output='person is not diabetic'

    return render_template('result.html',predict=output)


if __name__ == '__main__':
    app.run(debug=True)