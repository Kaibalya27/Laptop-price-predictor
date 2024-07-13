from flask import Flask, redirect, request, jsonify,render_template, url_for
import pickle
import pandas as pd
import numpy as np
from sklearn.base import TransformerMixin, BaseEstimator

# Define the custom transformer
class ppi(TransformerMixin, BaseEstimator):
    def fit(self, df, y=None):
        return self

    def transform(self, df, y=None):
        splitdf = df['ScreenResolution'].str.split('x', n=1, expand=True)
        df['X_res'] = splitdf[0]
        df['Y_res'] = splitdf[1]
        df['X_res'] = df['X_res'].str.replace(',', '').str.findall(r'(\d+.?\d+)').apply(lambda x: x[0])
        df['X_res'] = df['X_res'].astype('int')
        df['Y_res'] = df['Y_res'].astype('int')
        df['ppi'] = (((df['X_res']**2) + (df['Y_res']**2))**0.5 / (df['Inches'] + 0.0000001)).astype('float')
        df.drop(columns=['ScreenResolution', 'Inches', 'X_res', 'Y_res'], inplace=True)
        return df

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Initialize the Flask app
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Company=request.form['Company']
    Inches=request.form['Inches']
    ScreenResolution=request.form['ScreenResolution']
    TypeName=request.form['TypeName']
    HDD=request.form['HDD']
    Ram=request.form['RAM']
    Gpu_brand=request.form['GPU_Brand']
    SSD=request.form['SSD']
    Weight=request.form['Weight']
    Touchscreen=request.form['Touchscreen']
    IPS=request.form['IPS']
    Cpu_brand=request.form['CPU_Brand']
    os=request.form['os']

    query_df = pd.DataFrame({'Company':[Company],'TypeName':[TypeName],'Inches':[Inches],'ScreenResolution':[ScreenResolution],'Ram':[Ram],'Weight':[Weight],'Touchscreen':[Touchscreen],'IPS':[IPS],'Cpu_brand':[Cpu_brand],'HDD':[HDD],'SSD':[SSD],'Gpu_brand':[Gpu_brand],'os':[os]})
    print(query_df)
    prediction = pipe.predict(query_df)
    predicted_price = int(np.exp(prediction[0]))
    # return "the result is"+predicted_price
    return render_template('index.html', result=predicted_price)
    

