from flask import Blueprint, render_template, request
from app.model import ImageModel, MLPModel
from app.utils import getData, printText, printPredictionResults

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/predict', methods=['POST'])
def predict():
    textData, textString, image = getData()

    Image_Model = ImageModel('saved_models/image_model_scripted.pt')
    MLP_Model = MLPModel('saved_models/mlp_model_scripted.pt')

    img_pred = Image_Model.predict(image)
    mlp_pred = MLP_Model.predict_mlp(textData)
    text_info = printText(textString)
    prediction_results = printPredictionResults(img_pred, mlp_pred)
    return render_template('result.html', text_info=text_info, prediction_results=prediction_results)
