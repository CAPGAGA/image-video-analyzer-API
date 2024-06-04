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
    predict_class = np.argmax(result[0])
    predict_label = labels[str(predict_class)]

    return predict_label

