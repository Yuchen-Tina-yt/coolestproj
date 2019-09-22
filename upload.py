from google.cloud import storage

def upload(file, bucket):
    public_url = upload_file(file, bucket)
    return public_url
    print(public_url)

def upload_file(file, bucket):
    """
    Uploads a file to a given Cloud Storage bucket and returns the public url
    to the new object.
    """
    blob = bucket.blob(file)
    blob.upload_from_string("upload")
    url = blob.public_url
    return url

# upload('commercial_mono.wav')
