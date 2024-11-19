from flask import Flask, render_template, request
import pickle
from matplotlib.pylab import f
import numpy as np

model = pickle.load(open('BbP_model.pkl', 'rb'))
model_w = pickle.load(open('BbP_model_w.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = int(request.form['b'])
    data3 = request.form['c']
    data4 = request.form['d']

    arr = np.array([[data1, data2, data3]])

    if data3 == 'None':
        return

    if data4 == 'Optional':
        print('Optional')
        arr = np.array([[data1, data2, data3]])
        pred = model.predict(arr)
    else :
        print(data4)
        arr = np.array([[data1, data2, data3, data4]])
        pred = model_w.predict(arr)

    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















