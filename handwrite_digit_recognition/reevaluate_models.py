from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import mnist
import os


(x_1, y_1), (x_2, y_2) = mnist.load_data()

x = x_1 + x_2
y = y_1 + y_2

for name in os.listdir('./models_files'):
    model = load_model(f'./models_files/{name}')
    val_loss, val_acc = model.evaluate(x, y)
    print(f'{name}\nloss: {val_loss}, acc: {val_acc}\n')

if __name__ == '__main__':
    pass