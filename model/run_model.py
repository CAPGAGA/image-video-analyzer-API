from .load_model import load_model

def run_model(data):

    session = load_model('cpu')

    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    result = session.run([output_name], {input_name: data})

    return result

