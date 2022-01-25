from flask import request, jsonify
from flask_restful import Resource, reqparse
import torch
from torch.nn import functional as F
from PIL import Image

from werkzeug.datastructures import FileStorage

from uuid import uuid4 as uuid
import os

from src.model_utils import load_model, image_transformer

(classes, model) = load_model()
transformer = image_transformer()
device = "cpu"
PREDICTION_DIR = os.path.abspath(os.environ['PREDICTION_IMAGES_DIR'])


class DogAPI(Resource):

    def get(self):
        return classes

    def post(self):
        full_path = self.save_picture_to_file(request.files["picture"])
        prediction = self.predict(full_path)
        return {"predictions": prediction}
    
    def save_picture_to_file(self, picture):
        extension = os.path.splitext(picture.filename)[1]
        file_name = str(uuid()) + extension
        full_path = os.path.join(PREDICTION_DIR, file_name)
        picture.save(full_path)
        return full_path

    def predict(self, img):
        validation_batch = torch.stack(
            [transformer(Image.open(img)).to(device)])

        prediction_tensor = model(validation_batch)

        # transform the predictions to a probabilistic value
        prediction_probabilistic = F.softmax(
            prediction_tensor, dim=1).cpu().data.numpy()

        return {
            "sitting": str(prediction_probabilistic[0, 0]),
            "standing": str(prediction_probabilistic[0, 1])
        }
