import onnxruntime as ort

MODEL_PATH = "model/efficientnet-lite4-11.onnx"

def load_model(device:str):

    if device == 'cuda':
        providers = ['CUDAExecutionProvider']
    elif device == 'cpu':
        providers = ['CPUExecutionProvider']
    session = ort.InferenceSession(MODEL_PATH, providers=providers)
    return session

