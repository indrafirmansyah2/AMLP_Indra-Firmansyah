import flask
from flask import request
import numpy as np
import pickle

model = pickle.load(open('model/model19.pkl', 'rb'))

app = flask.Flask(__name__, template_folder='templates')

@app.route('/')
def main():
    return(flask.render_template('main.html'))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Sex = int(request.form['Sex'])
    ChestPainType = int(request.form['ChestPainType'])
    MaxHR = int(request.form['MaxHR'])
    ExerciseAngina = int(request.form['ExerciseAngina'])
    Oldpeak = float(request.form['Oldpeak'])
    ST_Slope = int(request.form['ST_Slope'])
    predict_list = [[Sex, ChestPainType, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]]
    prediction = model.predict(predict_list)
    output = {0: 'Tidak Sakit', 1: 'Sakit Jantung'}
    return flask.render_template('main.html', prediction_text='Prediksi pasien dinyatakan:  {}'.format(output[prediction[0]]))

if __name__ == '__main__':
    app.run(debug=True)