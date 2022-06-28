import pickle
from flask import Flask, render_template
from flask import request
import numpy as np
import mysql.connector

app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))



@app.route('/check', methods = ['GET'])
def checker():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'Task'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM predict')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", data = data)

@app.route('/predict', methods = ['POST'])
def predict():
    test = np.array(request.json['data'])
    predictions = model.predict(test)
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'Task'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    
    cursor.execute("""INSERT INTO predict (features, predictions) VALUES ('["1","2"]', '["3", "4"]');""")
    cursor.execute('INSERT INTO predict (features, predictions) VALUES (%s, %s);', (str(test.tolist()), str(predictions.tolist())))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Prediction" :predictions.tolist()}

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
    

    