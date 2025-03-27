import numpy as np
import keras
import img
import pandas as pd
from sklearn.model_selection import train_test_split

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
    Create an exteremely oversensitized model to predict the digits in the captcha.
    """
    #----------------------
    # + 0 1 2 3 4 5 6 7 8 9 = 
    data = pd.read_csv("ds.csv")
    y,X = data['0'],data.drop('0', axis=1)
    y = pd.get_dummies(y).astype(int).values
    y = np.argmax(y, axis=1)
    X = X/255 # Make Grayscale ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    

    #----------------------
    # MODEL STRUCTURE
    """
        Input  --> HL1 --> (ReLu) --> HL2 --> (ReLu) --> Output --> (Default Softmax) --> Ans
    """

    model = keras.models.Sequential()
    model.add(keras.layers.Input(shape=(784,)))
    #model.add(keras.layers.Dense(64, activation='relu'))
    
    model.add(keras.layers.Dense(12, activation='linear'))
    
    #-------------------------

    # BUILD MODEL
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

    # TRAIN MODEL
    hist = model.fit(X_train, y_train, epochs=200, validation_data=(X_test, y_test))
    model.evaluate(X_test, y_test)
    # SAVE TRAINED MODEL
    model.save("TrainedModelDigitsFinal.keras")

model = keras.saving.load_model("TrainedModelDigitsFinal.keras")

def solve(image):
    """
    Solve Capatcha.
    """
    
    global model
    im_list = [np.asarray(x).reshape(1,784) for x in img.PreProcessCap(image)]
    expr = ''
    for k,im in enumerate(im_list): 
        pred = evaluate_prediction(np.argmax(model.predict(im)))
        print(pred)
        expr += pred if k != (len(im_list) - 1) else '?'
    
    print(expr)
    return eval(expr[:-2])

