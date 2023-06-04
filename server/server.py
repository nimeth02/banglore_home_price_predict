from flask import Flask,request,jsonify
from flask_cors import CORS, cross_origin
import util
import pandas as pd

app=Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/hell')
@cross_origin()
def hell():
    return "hell"
@app.route('/get_location_names')
@cross_origin()
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access Control Allow Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
@cross_origin()
def predict_home_price():
    print(type(request.data))
    print(request.data)
    output = request.data.decode()
    print(output)
    j=output.replace(":",",")
    j = j.replace("}", ",")
    j=j.split('"')
    print(j)

    # df = pd.read_json('{"Courses":{"r1":"Spark"},"Fee":{"r1":"25000"},"Duration":{"r1":"50 Days"}}')
    # print(df)
    location = j[3]
    total_sqft=float(j[11])
    bhk=int(j[7])
    bath=int(j[15])
    print(util.get_estimated_price(location,total_sqft,bhk,bath))
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    # print(response.estimated_price)
    response.headers.add('Access Control Allow Origin', '*')
    return response



if __name__ == "__main__":
    print("starting python flask server")
    app.run(debug=True, port=5000)