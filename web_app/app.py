#!/usr/bin/python3
""" Starts a Flask Web Application for a Secondary CHO """
import requests
import json
from models import storage
from models.application import Application
from os import getenv

from flask import Flask, abort, render_template, request, redirect, session, url_for, flash, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import uuid

app = Flask(__name__)
app.secret_key = getenv('CHO_FLASK_SECRET')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

@login_manager.user_loader
def load_user(user_id):
    return storage.find_user_by_id(user_id)

@app.route('/index', strict_slashes=False)
def index():
    """ the index page of the CHO Website """
    return render_template('index.html', cache_id=str(uuid.uuid4()))

@app.route('/about', strict_slashes=False)
def about():
    """ the about page of the CHO Website """
    return render_template('about.html', cache_id=str(uuid.uuid4()))

@app.route('/admission', strict_slashes=False)
def admission():
    """ the admission page of the CHO Website """
    return render_template('admission.html', cache_id=str(uuid.uuid4()))

@app.route('/anthem', strict_slashes=False)
def anthem():
    """ the anthem page of the CHO Website """
    return render_template('anthem.html', cache_id=str(uuid.uuid4()))

@app.route('/curriculum', strict_slashes=False)
def curriculum():
    """ the curriculum page of the CHO Website """
    return render_template('curricullum.html', cache_id=str(uuid.uuid4()))

@app.route('/extra_curriculum', strict_slashes=False)
def extra_curriculum():
    """ the extra_curriculum page of the CHO Website """
    return render_template('extra_curricullum.html', cache_id=str(uuid.uuid4()))

@app.route('/fees', strict_slashes=False)
def fees():
    """ the fees page of the CHO Website """
    return render_template('fees.html', cache_id=str(uuid.uuid4()))

@app.route('/gallery', strict_slashes=False)
def gallery():
    """ the gallery page of the CHO Website """
    return render_template('gallery.html', cache_id=str(uuid.uuid4()))

@app.route('/govboard', strict_slashes=False)
def govboard():
    """ the govboard page of the CHO Website """
    return render_template('govboard.html', cache_id=str(uuid.uuid4()))

@app.route('/principal', strict_slashes=False)
def principal():
    """ the principal page of the CHO Website """
    return render_template('principal.html', cache_id=str(uuid.uuid4()))

@app.route('/religious', strict_slashes=False)
def religious():
    """ the religious page of the CHO Website """
    return render_template('religious.html', cache_id=str(uuid.uuid4()))

@app.route('/portal', strict_slashes=False)
def portal():
    """ the portal page of the CHO Website """
    return render_template('portal.html', cache_id=str(uuid.uuid4()))

@app.route('/application', strict_slashes=False, methods=['GET', 'POST'])
def application():
    """ the page for submitting an application """
    if request.method == 'POST':
        url = getenv('CHO_API_URL') + '/applications'
        data = request.form.to_dict()
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers={'Content-Type': 'application/json'})
        if response.status_code == 201:
            flash('Application submitted successfully', 'alert alert-success')
            return redirect(url_for('application'))
        else:
            flash('Application submission failed', 'alert alert-danger')
            return redirect(url_for('application'))
    return render_template('application.html', cache_id=str(uuid.uuid4()))

@app.route('/signup', methods=['GET', 'POST'], strict_slashes=False)
def signup_page():
    """ The page for creating a user account """
    if request.method == 'POST':
        user_url = getenv('CHO_API_URL') + '/students'
        image_url_template = getenv('CHO_API_URL') + '/students/{}/image'

        data = request.form.to_dict()
        json_data = json.dumps(data)

        # Send POST request to create user
        user_response = requests.post(user_url, data=json_data, headers={'Content-Type': 'application/json'})

        if user_response.status_code == 201:
            user = user_response.json()
            user_id = user.get('id')

            # Retrieve the image
            file = request.files['file']
            files = {
                'file': (file.filename, file.read(), file.content_type)
            }

            # Send POST request to upload image
            image_url = image_url_template.format(user_id)
            image_response = requests.post(image_url, files=files)

            if image_response.status_code == 200:
                flash('Account created successfully', 'alert alert-success')
                return redirect(url_for('login_page'))
            else:
                flash('Account created, but Image upload failed', 'alert alert-danger')
                return redirect(url_for('signup_page'))
        elif user_response.status_code == 409:
            flash('Email already exists', 'alert alert-danger')
            return redirect(url_for('signup_page'))
        else:
            flash('Account creation failed, check the form', 'alert alert-danger')
            return redirect(url_for('signup_page'))
    else:
        return render_template('signup.html', cache_id=str(uuid.uuid4()))

@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login_page():
    """ the page for signing/logging in"""
    if request.method == 'POST':
        url = getenv('CHO_API_URL') + '/login'
        data = request.form.to_dict()
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json,
                                 headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            user_data = response.json()
            user = Student.from_dict(user_data)
            login_user(user)
            flash('Login successful', 'alert alert-success')
            return redirect(url_for('index'))
        else:
            flash('Please check your login credentials', 'alert alert-danger')
            return redirect(url_for('login_page'))
    return render_template('login.html', cache_id=str(uuid.uuid4()))

@login_required
@app.route('/profile', strict_slashes=False, methods=['GET', 'POST', 'DELETE'])
def profile():
    """ the page for user profile"""
    user = storage.find_user_by_id(current_user.id)
    if request.method == 'POST':
        url = getenv('CHO_API_URL') + f'/students/{user.id}'
        data = request.form.to_dict()
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json,
                                headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            flash('Profile updated successfully', 'alert alert-success')
        else:
            flash('Profile update failed', 'alert alert-danger')
        return redirect(url_for('profile'))

    if request.method == 'DELETE':
        url = getenv('CHO_API_URL') + f'/students/{user.id}'
        response = requests.delete(url)
        if response.status_code == 200:
            flash('Profile deleted successfully', 'alert alert-success')
            return redirect(url_for('login_page'))
        else:
            flash('Profile deletion failed', 'alert alert-danger')
            return redirect(url_for('profile'))

    return render_template('profile.html', cache_id=str(uuid.uuid4()), user=user)

@login_required
@app.route('/application/<application_id>', strict_slashes=False, methods=['GET', 'POST', 'DELETE'])
def application_detail(application_id):
    """ the page for viewing and editing a particular application """
    url = getenv('CHO_API_URL') + f'/applications/{application_id}'
    if request.method == 'GET':
        response = requests.get(url)
        if response.status_code == 200:
            application = response.json()
            return render_template('application_detail.html', cache_id=str(uuid.uuid4()), application=application)
        else:
            flash('Application not found', 'alert alert-danger')
            return redirect(url_for('application'))

    if request.method == 'POST':
        data = request.form.to_dict()
        data['user_id'] = current_user.id
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json, headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            flash('Application updated successfully', 'alert alert-success')
        else:
            flash('Application update failed', 'alert alert-danger')
        return redirect(url_for('application_detail', application_id=application_id))

    if request.method == 'DELETE':
        response = requests.delete(url)
        if response.status_code == 200:
            flash('Application deleted successfully', 'alert alert-success')
            return redirect(url_for('application'))
        else:
            flash('Application deletion failed', 'alert alert-danger')
        return redirect(url_for('application_detail', application_id=application_id))

    return render_template('application_detail.html', cache_id=str(uuid.uuid4()))

@login_required
@app.route('/logout', strict_slashes=False)
def logout():
    """ the page for logging out"""
    logout_user()
    flash('Logout successfully', 'alert alert-success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    """ start app """
    port = int(getenv('CHO_API_PORT', 5000))
    host = getenv('CHO_API_HOST', '0.0.0.0')
    app.run(host=host, port=port, debug=True)
