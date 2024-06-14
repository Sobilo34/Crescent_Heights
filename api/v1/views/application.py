#!/usr/bin/python3
"""  API actions for application """
from werkzeug.utils import secure_filename
from models.user import User
from models.application import Application
from models.images import Image
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask import request
import os


@app_views.route('/applications', methods=['GET'], strict_slashes=False)
@swag_from('documentation/applications/all_applications.yml')
def get_applications():
    """
    Retrieves the list of all applications objects
    """
    all_applications = storage.all(Application).values()
    list_applications = []
    for application in all_applications:
        list_applications.append(application.to_dict())
    return jsonify(list_applications)


@app_views.route('/applications/<application_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/applications/get_application.yml', methods=['GET'])
def get_application(application_id):
    """ Retrieves an application """
    application = storage.get(application, application_id)
    if not application:
        abort(404)

    return jsonify(application.to_dict())


@app_views.route('/applications/<application_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/applications/delete_application.yml', methods=['DELETE'])
def delete_application(application_id):
    """
    Deletes a application Object
    """

    application = storage.get(application, application_id)

    if not application:
        abort(404)

    storage.delete(application)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/applications', methods=['POST'], strict_slashes=False)
@swag_from('documentation/applications/post_application.yml', methods=['POST'])
def post_application():
    """
    Creates a application
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    if 'description' not in request.get_json():
        abort(400, description="Missing description")
    if 'price' not in request.get_json():
        abort(400, description="Missing price")

    data = request.get_json()
    instance = Application(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/applications/<application_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/applications/put_application.yml', methods=['PUT'])
def put_application(application_id):
    """
    Updates a application
    """
    application = storage.get(application, application_id)

    if not application:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(application, key, value)
    storage.save()
    return make_response(jsonify(application.to_dict()), 200)


@app_views.route('/applications/<application_id>/images', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/applications/images/get_images.yml', methods=['GET'])
def get_images(application_id):
    """ Retrieve images associated with a specific application. """
    application = storage.get(application, application_id)
    if not application:
        abort(404)
    list_images = []
    for image in application.images:
        list_images.append(image.to_dict())

    return jsonify(list_images)


@app_views.route('/applications/<application_id>/images', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/applications/image/post_image.yml', methods=['POST'])
def post_image(application_id):
    """
    Upload images for a specific application.
    """
    UPLOAD_FOLDER = "web_app/static/images/upload/application"

    application = storage.get(Application, application_id)
    if not application:
        abort(404)
    if 'file' not in request.files:
        abort(401, description="Not a FILE")

    files = request.files.getlist('file')
    if not files:
        abort(400, description="No file uploaded")
    # get all the files
    image_urls = []
    for file in files:
        if file.filename == '':
            abort(404, description="No selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Create a new Image object
            new_image = Image(url=filename, application_id=application_id)
            new_image.save()
            image_urls.append(filepath)
        else:
            abort(404, description="Invalid file type")
    if image_urls:
        print(image_urls[0])
        application.cover_img = image_urls[0].split('/')[-1]
        storage.save()
    return jsonify(image_urls), 201


# helper function for post_images()
def allowed_file(filename):
    """
    Check if the file is allowed based on the file extension.
    """
    EXT = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXT