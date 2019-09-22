from google.cloud import storage
#client = storage.Client()
#bucket_name = 'fakeadults201'
# Creates the new bucket
#bucket = client.create_bucket(bucket_name)
def upload(file,bucket):
    public_url = upload_file(file,bucket)
    return public_url
    print(public_url)

def upload_file(file,bucket):
    """
    Uploads a file to a given Cloud Storage bucket and returns the public url
    to the new object.
    """

    # The name for the new bucket
    blob = bucket.blob(file)
    blob.upload_from_string("upload")
    url = blob.public_url
    return url
    #blob.upload_from_string(
        #file_stream,
        #content_type=content_type)

#upload('commercial_mono.wav')
