import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():

    df = pd.read_csv("data.csv")

    X = df[["Units_Used"]]
    y = df["Bill_Amount"]

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict_bill(units):

    model = train_model()

    prediction = model.predict([[units]])

    return round(prediction[0], 2)