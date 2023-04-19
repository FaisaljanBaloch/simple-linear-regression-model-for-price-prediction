from flask import Flask
from flask import render_template, request, jsonify

# import linear regression model
from models import LinearRegression

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you will definately guess me'
model = LinearRegression()  # create instance of linear model


@app.route('/')
def index():
    """ Render the index view """
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict_price():
    """ Predict the price of a house"""
    if request.method == 'GET' and request.args.get('sizeOfHouse'):
        size_of_house = int(request.args.get('sizeOfHouse'))
        predicted_price = model.predict(size_of_house)
        return jsonify(price=predicted_price), 200

    else:
        return jsonify(error='Invalid request'), 400


if __name__ == '__main__':
    app.run()
