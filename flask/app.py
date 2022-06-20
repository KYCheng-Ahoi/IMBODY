""" Flask API for annotating medical images """
import sys
import json
import numpy as np
import cv2

from io import BytesIO
from flask import Flask, jsonify, request
from pydicom.dataset import Dataset

from utils.dicom_helper import dictify
from utils.png_helper import annotate_png

class PytorchParams:
    model_path = 'archieve/training/model.pt'
    ckpt_path = 'archieve/training/cp-final.ckpt'
    with open('archieve/training/class_names.json') as BOB:
        class_names = json.load(BOB)

p = PytorchParams()
print(f"{len(p.class_names)} classes are detected")

try:
    # instantiate the network
    import torch
    model = torch.jit.load(p.model_path)
    checkpoint = torch.load(p.ckpt_path)
    model.load_state_dict(checkpoint['model_state_dict'])
except:
    print("Error loading model. Check if file exists.")
    sys.exit(0)

app = Flask(__name__)

@app.route('/')
def main():
    """ Main page of the API """
    return "This is the main page" 

@app.route('/png-predict/json', methods=['POST'])
def predict_json():
    """Reponse DL prediction for PNG images (Post as JSON input)"""
    data = request.json
    return jsonify({
        's3_key': data['s3_key'], 
        'annotation': annotate_png(data['inputs'], model, p)
    })

# https://stackoverflow.com/questions/50779424/postman-python-and-passing-images-and-metadata-to-a-web-service
@app.route('/png-predict/form-data', methods=['POST'])
def predict_form_data():
    """Reponse DL prediction for PNG images (Post as HTML Form Data)"""
    try: 
        npimg = np.fromfile(request.files['inputs'], np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)
        return jsonify({
            's3_key': request.form['s3_key'], 
            'annotation': annotate_png(img, model, p)
        }), 200
    except Exception as e:
        print(e)
    return {'s3_key': request.form['s3_key'], 'annotation':''}

@app.route('/dicom/json', methods=['POST'])
def dicom_json():
    """Extract DICOM header for DICOM images (Post as JSON input)"""
    data = request.json
    ds = Dataset.from_json(data["inputs"])
    annotation =  str(dictify(ds))
    print(annotation)
    return {
        's3_key': data['s3_key'], 
        'annotation': annotation
        }, 200


@app.route('/dicom/form-data', methods=['POST'])
def dicom_form_data():
    """Extract DICOM header for DICOM images (Post as HTML Form Data)"""
    try:
        s = BytesIO(request.files['inputs'].read())
        import pydicom
        annotation = str(dictify(pydicom.dcmread(s, force=True)))
        print(annotation)
        return {
            's3_key': request.form['s3_key'], 
            'annotation': annotation
        }, 200
    except Exception as e:
        print(e)
    return {'s3_key': request.form['s3_key'], 'annotation':''}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
