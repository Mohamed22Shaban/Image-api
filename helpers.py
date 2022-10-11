import os
from flask import current_app, jsonify
from werkzeug.utils import secure_filename

import boto3
from botocore.exceptions import ClientError
def allowed_extention(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower()in current_app.config['ALLOWED_EXTENTIONS'] 




def get_secure_filename_filepath(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'],filename)
    return filename , filepath


# upload to amazon3
def upload_to_s3(file, bucket_name, acl='public-read'):
    s3_client = boto3.client('s3',aws_access_key_id=current_app.config['s3-KEY'],aws_secret_access_key=current_app.config['s3_SECRET'])
    file.filename = secure_filename(file.filename)
    file.filename = os.path.join('uploads/',file.filename)
    try:
        s3_client.upload_fileobj(file, bucket_name, file.filename, ExtraArges={'ACL':acl,'ContentType':file.content_type})
    except ClientError as e:
        return jsonify({'message':'Cannot uoload files to s3 account'}), 400

    return file.filename






