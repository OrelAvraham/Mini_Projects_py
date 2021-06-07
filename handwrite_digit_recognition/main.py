import tensorflow as tf
import matplotlib.pyplot as plt
import random
import keyboard
import numpy as np
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation=tf.nn.relu),
    tf.keras.layers.Dense(32, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)

print(f'loss: {val_loss}, acc: {val_acc}')

name = 'in-32-32-out.model'
model.save(f'models_files/{name}')
'''
model = tf.keras.models.load_model('digit_classifier.model')
'''

predictions = model.predict([x_test])

size = 20
start = random.randrange(len(x_test) - size)
for i in range(start, start + size):
    print(np.argmax(predictions[i]))
    plt.imshow(x_test[i])
    plt.show()
    # while not keyboard.is_pressed('enter'):
    #     pass

if __name__ == '__main__':
    pass
