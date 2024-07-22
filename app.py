from flask import Flask, redirect, request, jsonify,render_template, url_for
import pickle
import pandas as pd
import numpy as np

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
    Inches=float(request.form['Inches'])
    ScreenResolution=request.form['ScreenResolution']
    TypeName=request.form['TypeName']
    HDD=int(request.form['HDD'])
    Ram=int(request.form['RAM'])
    Gpu_brand=request.form['GPU_Brand']
    SSD=int(request.form['SSD'])
    Weight=float(request.form['Weight'])
    Touchscreen=request.form['Touchscreen']
    IPS=request.form['IPS']
    Cpu_brand=request.form['CPU_Brand']
    os=request.form['os']
    
    splitdf = ScreenResolution.split('x')
    X_res = int(splitdf[0])
    Y_res = int(splitdf[1])
    ppi = float(((X_res**2) + (Y_res**2))**0.5 / (Inches + 0.0000001))
    query_df = pd.DataFrame({'Company':[Company],'TypeName':[TypeName],'ppi':[ppi],'Ram':[Ram],'Weight':[Weight],'Touchscreen':[Touchscreen],'IPS':[IPS],'Cpu_brand':[Cpu_brand],'HDD':[HDD],'SSD':[SSD],'Gpu_brand':[Gpu_brand],'os':[os]})
    prediction = pipe.predict(query_df)
    predicted_price = int(np.exp(prediction[0]))
    return render_template('index.html', result=predicted_price)
    
if __name__ == '__main__':
    app.run(debug=True)

