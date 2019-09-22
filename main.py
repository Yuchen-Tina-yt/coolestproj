import logging
from transcribe_punct import transcribe_file_with_auto_punctuation
from upload import upload, upload_file
from flask import *
from google.cloud import storage

app = Flask(__name__)
app.secret_key = "testing"

ALLOWED_EXT = ['wav','mp3']

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT
def conversion(filename):
    form os import path
    from pydub impirt AudioSegment
    if(filename)
    src = filename
    dst = "test.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format = "wav")

@app.route('/', methods=['GET', 'POST'])
def index():
    client = storage.Client()
    bucket_name = 'fakeadults'
    #bucket = client.create_bucket(bucket_name)
    bucket = client.get_bucket(bucket_name)

    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No File Found")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            blob = bucket.blob(file.filename)
            blob.upload_from_file(file)
            flash("File uploaded")
            return transcribe_file_with_auto_punctuation(file)
            # return transcribe_file_with_auto_punctuation(url)
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
