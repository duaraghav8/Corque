import os
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename
import detect, face_recognizer

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')

file =None

# Route that will process the file upload
@app.route('/upload', methods=['GET','POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        detect.doDetect(file)
        present_student_list = face_recognizer.doFaceRecognition()
        return jsonify (
        	students_present=present_student_list)

	return "something went wrong"
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        # return redirect(url_for('uploaded_file',
        #                         filename=filename))
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
 	#detect.doDetect(file)
 	if file is None:
		return "File is none"
 #    if file is not None:
 #    	# present_student = face_recognizer.doFaceRecognition()
 #    	return "file is not none"
	return "file is not none"
    	
if __name__ == '__main__':
    app.run()
