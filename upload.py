from google.cloud import storage
def upload(file):
    public_url = upload_file(file)
    return public_url
    print(public_url)

def upload_file(file):
    """
    Uploads a file to a given Cloud Storage bucket and returns the public url
    to the new object.
    """
    client = storage.Client()
    # The name for the new bucket
    bucket_name = 'my-new-bucket'
    # Creates the new bucket
    bucket = client.create_bucket(bucket_name)
    blob = bucket.blob(file)
    #blob.upload_from_string(
        #file_stream,
        #content_type=content_type)

    #url = blob.public_url

upload('commercial_mono.wav')
