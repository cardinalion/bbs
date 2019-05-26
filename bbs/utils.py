from flask import current_app


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['BBS_ALLOWED_IMAGE_EXTENSIONS']