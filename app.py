

from flask import Flask ,jsonify , request ,send_from_directory
from actions import bp as actionsbp
from filters import bp as filtersbp
from andriod import bp as andriodbp
from helpers import get_secure_filename_filepath, allowed_extention

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENTIONS =['png', 'jpg', 'jpeg']

# 1)
app = Flask(__name__)
app.secret_key = 'SECRET_KEY'



# create folder for upload image
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# create Allowed extensions
app.config['ALLOWED_EXTENTIONS'] = ALLOWED_EXTENTIONS

# 3)
app.register_blueprint(actionsbp)
app.register_blueprint(filtersbp)
app.register_blueprint(andriodbp)


@app.route('/')
def index():
    return jsonify({'message':'Welcome to Image API'})

# CRTEAT func for upload images
@app.route('/images', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error':'no Files Was Selected'}), 400
        
        file = request.files['file']

        if file.filename =='':
            return jsonify({'error':'no Files Was Selected'}), 400
        

        if not allowed_extention(file.filename):
            return jsonify({'error':'the extntion is not supported'}), 400
        filename, filepath = get_secure_filename_filepath(file.filename)
        file.save(filepath)
        return jsonify({
            'message': 'File successfully uploaded',
            'filename' :filename
        }) ,201




@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'],name)



if __name__ =='__main__':
    app.run(debug=True)
