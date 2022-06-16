from flask import Flask, render_template, request, session, jsonify
import os
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
from image_predictor import predict_image

try:
    os.makedirs('staticFiles/upload')
except OSError as e:
    print('exists')

class_label = ['cable_crossover', 'lat_pull_down', 'pec_deck', 'smith_machine', 'treadmill']

# Backend operation
templateFiles = 'templateFiles'
staticFiles = 'staticFiles'

# Defining upload folder path
UPLOAD_FOLDER = 'staticFiles/uploads'

# Define allowed files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name for template path
# The default folder name for static files should be "static" else need to mention custom folder for static path
app = Flask(__name__, template_folder= templateFiles, static_folder= staticFiles)

# Configure upload folder for Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
 
@app.route('/')
def index():
    return render_template('index_upload_and_show_data.html')
 
@app.route('/',  methods=("POST", "GET"))
def uploadFile():
    if request.method == 'POST':
        # Upload file
        uploaded_img = request.files.get('file')
        if uploaded_img is None or uploaded_img.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(uploaded_img.filename):
            return jsonify({'error': 'format not supported'})

        try:
          file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp.jpg')
          uploaded_img.save(file_path)

          #predict
          image = Image.open(uploaded_img.stream)
          prediction =  predict_image(image)

          
          return render_template('index_upload_and_show_data_page2.html', user_image = file_path, prediction = str(class_label[prediction]))
          
        except Exception as e:
            return jsonify({'error': 'error during prediction', 'reason': e}) 
        
if __name__=='__main__':
  app.run()