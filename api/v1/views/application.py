from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask import request
import os
from werkzeug.utils import secure_filename

#!/usr/bin/python3
"""  API actions for application """

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
@swag_from('documentation/applications/get_application.yml')
def get_application(application_id):
    """ Retrieves an application """
    application = storage.get(Application, application_id)
    if not application:
        abort(404)

    return jsonify(application.to_dict())


@app_views.route('/applications/<application_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/applications/delete_application.yml')
def delete_application(application_id):
    """
    Deletes an application Object
    """

    application = storage.get(Application, application_id)

    if not application:
        abort(404)

    storage.delete(application)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/applications', methods=['POST'], strict_slashes=False)
@swag_from('documentation/applications/post_application.yml')
def post_application():
    """
    Creates an application
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'first_name' not in request.get_json():
        abort(400, description="Missing first_name")
    if 'last_name' not in request.get_json():
        abort(400, description="Missing last_name")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'phone' not in request.get_json():
        abort(400, description="Missing phone")
    if 'address' not in request.get_json():
        abort(400, description="Missing address")
    if 'date_of_birth' not in request.get_json():
        abort(400, description="Missing date_of_birth")
    if 'grade_applying_for' not in request.get_json():
        abort(400, description="Missing grade_applying_for")
    if 'parent_name' not in request.get_json():
        abort(400, description="Missing parent_name")
    if 'parent_contact' not in request.get_json():
        abort(400, description="Missing parent_contact")

    data = request.get_json()
    instance = Application(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/applications/<application_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/applications/put_application.yml')
def put_application(application_id):
    """
    Updates an application
    """
    application = storage.get(Application, application_id)

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


@app_views.route('/applications/<application_id>/documents', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/applications/documents/get_documents.yml')
def get_documents(application_id):
    """ Retrieve documents associated with a specific application. """
    application = storage.get(Application, application_id)
    if not application:
        abort(404)
    list_documents = []
    for document in application.documents:
        list_documents.append(document.to_dict())

    return jsonify(list_documents)


@app_views.route('/applications/<application_id>/documents', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/applications/documents/post_document.yml')
def post_document(application_id):
    """
    Upload documents for a specific application.
    """
    UPLOAD_FOLDER = "web_app/static/documents/upload/application"

    application = storage.get(Application, application_id)
    if not application:
        abort(404)
    if 'file' not in request.files:
        abort(401, description="Not a FILE")

    files = request.files.getlist('file')
    if not files:
        abort(400, description="No file uploaded")
    # get all the files
    file_paths = []
    for file in files:
        if file.filename == '':
            abort(404, description="No selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            # Create a new Document object
            new_document = Document(name=filename, file_path=filepath, application_id=application_id)
            new_document.save()
            file_paths.append(filepath)
        else:
            abort(404, description="Invalid file type")
    if file_paths:
        print(file_paths[0])
        # Update the application with the first document path
        application.document_path = file_paths[0]
        storage.save()
    return jsonify(file_paths), 201


# helper function for post_document()
def allowed_file(filename):
    """
    Check if the file is allowed based on the file extension.
    """
    EXT = {'pdf', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXT
