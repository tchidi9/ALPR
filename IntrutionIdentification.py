import io
import re
import requests
import picamera
import time
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def entry(fileName):
    texts = extractImageFunc(fileName)
    #print texts (uncomment to print out text extracted from image)

    for text in texts:
        result = extractPlateNum(text)
	
        if result is not None:
	    return result
	else:
	    return ""

#use google vision API for text extraction from image 
def extractImageFunc(file_name):
    client = vision.ImageAnnotatorClient()

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = [res.description for res in response.text_annotations]

    return texts

# regex expression for plate number
def extractPlateNum(text):
    plate_format = re.compile('[a-zA-Z]{3} [0-9]{2,3}[a-zA-z]{2}')
    results = re.findall(plate_format, text)
    return str(results[0]) if len(results) > 0 else None
