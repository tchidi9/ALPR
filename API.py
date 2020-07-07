import io
import re
import requests
import picamera
import time
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def getPlateNo():
    texts = extractImageFunc(getImageFunc())
    #print texts (uncomment to print out text extracted from image)

    for text in texts:
        result = extractPlateNum(text)

        if result is None:
	    result = ""

	return result

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


def post(plateNumber, pictureURL, videoURL, longLat): 
    # defining the api-endpoint 
    API_ENDPOINT = "" #enter end point here

    # data to be sent to api 
    data = {
        'plate_number':	plateNumber,
        'picture_url':	pictureURL,
        'video_path':	videoURL,
        'locationInfo':	longLat
    } 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    print(r)
