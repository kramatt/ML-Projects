# Machine Learning Mastery
# Your First Deep Learning Project in Python with Keras Step-By-Step
# Article: https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Load and split the dataset
dataset = loadtxt('/Users/Matt/Documents/School/Data Science/Machine Learning Mastery/Datasets/pima-indians-diabetes.csv', delimiter=',')
X = dataset[:,0:8]
y = dataset[:,8]

# Define keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the keras model on the dataset
model.fit(X, y, epochs=150, batch_size=10, verbose=0)

# Evaluate the keras model
_, accuracy = model.evaluate(X, y, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

# Make rounded probability predictions with the model
#predictions = model.predict(X)
#rounded = [round(x[0]) for x in predictions]

# Make class predictions with the model
predictions = model.predict_classes(X)

for i in range(20):
    print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))
