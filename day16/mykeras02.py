import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

EPOCHS=2000 
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
target_data = np.array([[0],[1],[1],[0]], "float32")

model = Sequential()
model.add(Dense(16, input_shape=(2,), activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

print("-----------not train")
print(model.predict(training_data))

history = model.fit(training_data, target_data, 
                    epochs=EPOCHS, verbose=0)

print("----------- train")
print(model.predict(training_data[3:]))
# model.evaluate(training_data, target_data, steps=2)