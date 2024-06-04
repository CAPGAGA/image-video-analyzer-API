# own
from .load_model import load_model

#  third-party
import json
import numpy as np

labels = json.load(open('model/labels_map.txt'))

async def run_model(data):

    session = load_model('cpu')

    input_name = session.get_inputs()[0].name

    result = session.run(None, {input_name: data})

    probabilities = result[0][0]
    threshold = 0.80

    filtered_classes = [
        {'class': labels[str(i)], 'probability': float(probability)}
        for i, probability in enumerate(probabilities) if probability > threshold
    ]
    print(filtered_classes)
    return filtered_classes

