from IPython.display import clear_output
from pylab import *
from sklearn import datasets
import matplotlib.pyplot as plt
import json


class Trainer:
    def __init__(self):
        faces = datasets.fetch_olivetti_faces()
        self.results = {}
        self.imgs = faces.images
        self.index = 0

    def increment_face(self):
        self.index = self.index + 1
        return self.index

    def decrement_face(self):
        self.index = self.index - 1
        return self.index

    def record_result(self, glasses=1):
        self.results[str(self.index)] = glasses


def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'z':
        update_glasses(0)
    if event.key == 'm':
        update_glasses(1)
    if event.key == 'y':
        save_close()
    if event.key == 'b':
        previous_picture()


def display_face(face):
    if (trainer.index < 400):
        clear_output()
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect('key_press_event', press)
        plt.imshow(face, cmap='gray')
        ax.set_title('Press a key')
        plt.show()
    else:
        save_close()


def update_glasses(b):
    trainer.record_result(glasses=b)
    trainer.increment_face()
    plt.close()
    display_face(trainer.imgs[trainer.index])


def save_close():
    with open('results.xml', 'w') as f:
        json.dump(trainer.results, f)


def previous_picture():
    trainer.decrement_face()
    plt.close()
    display_face(trainer.imgs[trainer.index])


trainer = Trainer()

while 1:
    display_face(trainer.imgs[trainer.index])
