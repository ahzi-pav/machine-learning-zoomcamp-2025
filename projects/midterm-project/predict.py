import pickle
import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model/model_lr=0.1_md=7'

with open(model_file, 'rb') as f_in:

    model = pickle.load(f_in)

app = Flask('credit_score')

@app.route('/predict', methods=['POST'])
def predict():
    borrower = request.get_json()

    X = pd.DataFrame([borrower])
    score = model.predict_proba(X)[:,1]
    default = model.predict(X)

    result = {
        'default_probability': float(score),
        'default': bool(default)
    }

    return jsonify(result)

if __name__ == "__main__":
    
    app.run(debug=True, host='0.0.0.0', port=9696)
