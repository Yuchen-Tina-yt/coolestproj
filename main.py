import logging
from transcribe_punct import transcribe_file_with_auto_punctuation

from flask import *


app = Flask(__name__)
app.secret_key = "testing"

ALLOWED_EXT = ['wav','mp3']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No File Found")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash("No selected file")
            return redirect(request.url) #TODO: redirect to NO SELECTED FILE
        if file and allowed_file(file.filename):
            #TODO: ADD TO GOOGLE CLOUD STORAGE
            flash("File uploaded")
            return transcribe_file_with_auto_punctuation('commercial_mono.wav')
    return render_template('index.html')


# @app.route('/transc')
# def transc():
#     return transcribe_file_with_auto_punctuation('commercial_mono.wav')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml. host='127.0.0.1'
    app.run(port=8080, debug=True)
