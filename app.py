from flask import Flask, request, jsonify
import pickle
import pandas as pd
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

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    query_df = pd.DataFrame(data)
    prediction = pipe.predict(query_df)
    predicted_price = int(np.exp(prediction[0]))
    return jsonify({'predicted_price': predicted_price})

if __name__ == '__main__':
    app.run(debug=True)
