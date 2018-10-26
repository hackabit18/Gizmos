
import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

file_name = os.path.join(
os.path.dirname(__file__),
'C:/Users/Abbas Shah/Desktop/osama.png')

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotations

if __name__=="__main__":

    print('Labels:')
    for label in labels:
         print(label.description)