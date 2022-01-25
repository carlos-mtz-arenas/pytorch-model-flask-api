import torch
from torchvision import models, transforms
import torch.nn as nn

from src.model_meta.model_configuration import model_classes


def load_model():
    device = "cpu"

    model = models.resnet50(pretrained=False).to(device)

    model.fc = nn.Sequential(
        nn.Linear(2048, 128),
        nn.ReLU(inplace=True),
        nn.Linear(128, 2)).to(device)

    model.load_state_dict(torch.load('./src/model_meta/dog-trainer.h5'))

    return (model_classes, model)


def image_transformer():
    normalizer = transforms.Normalize(
        [0.5, 0.5, 0.5],
        [0.5, 0.5, 0.5]
    )

    transformer = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalizer
    ])

    return transformer
