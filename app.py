from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("website.html")


@app.route('/predict',methods=['POST'])
def predict():    
    feature =[int(float(x)) for x in request.form.values()]
    final=[np.array(feature)]


    prediction=model.predict(final)
    ans = prediction[0]
    print(ans)

    return render_template('website.html', ans=int(ans))


if __name__ == '__main__':
    app.run()