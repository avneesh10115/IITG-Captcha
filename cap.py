import numpy as np
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import Dense, Input
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import img

def evaluate_prediction(pred):
    """
    Evaluate the prediction and return the answer.
    """
    if pred == 0:
        return '+'
    if pred == 11:
        return '='
    return str(pred - 1)

train = False
if train:
    """
    Train the model from scratch.
    """

    data = pd.read_csv("ds.csv")
    y = data['0']
    X = data.drop('0', axis=1)


    X = X / 255.0


    y_one_hot = pd.get_dummies(y)
    y_one_hot = y_one_hot.values


    X_train, X_test, y_train, y_test = train_test_split(X, y_one_hot, test_size=0.2, random_state=42)


    model = Sequential([
        Input(shape=(784,)),
        Dense(y_one_hot.shape[1], activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss="categorical_crossentropy",
        metrics=['accuracy']
    )

    hist = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))
    model.evaluate(X_test, y_test)


    model.save("TrainedModelDigitsFinal.keras")

model = load_model("TrainedModelDigitsFinal.keras")

def solve(image):
    """
    Solve Captcha.
    """
    global model
    im_list = [np.asarray(x).reshape(1, 784) for x in img.PreProcessCap(image)]
    expr = ''

    for k, im in enumerate(im_list):
        pred = evaluate_prediction(np.argmax(model.predict(im, verbose=0)))
        print(pred)
        expr += pred if k != (len(im_list) - 1) else '?'

    print("Expression:", expr)
    return eval(expr[:-2])
