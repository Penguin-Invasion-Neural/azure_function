from keras.models import Sequential

def predict(input):
    model = Sequential()
    model.load_weights('model.h5')
    prediction = model.predict(input)

    return prediction