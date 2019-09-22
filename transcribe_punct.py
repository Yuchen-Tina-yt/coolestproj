
#!/usr/bin/env python

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample that demonstrates auto punctuation
and recognition metadata.
Example usage:
    python transcribe_auto_punctuation.py resources/commercial_mono.wav
"""
import wave
import argparse
# import io
# import cloudstorage as gcs


def stereo_to_mono(audio_file_name):
    sound = pydub.AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound.export(audio_file_name, format="wav")

def mp3_to_wav(audio_file_name):
    if audio_file_name.split('.')[1] == 'mp3':
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")

def frame_rate_channel(audio_file_name):
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate,channels

def transcribe_file_with_auto_punctuation(path, frame_rate):
    """Transcribe the given audio file with auto punctuation enabled."""
    # [START speech_transcribe_auto_punctuation]
    from google.cloud import speech
    client = speech.SpeechClient()

    # with gcs.open(path, 'rb') as file:
    # content = file.read()

    audio = speech.types.RecognitionAudio(uri=path)
    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code='en-US',
        # Enable automatic punctuation
        enable_automatic_punctuation=True)
    try:
        response = client.long_running_recognize(config, audio)
    except:
        response = client.recognize(config, audio)
    ret = []

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        # print('-' * 20)

        # print('First alternative of result {}'.format(i))
        ret.append(alternative.transcript)

    return '<br/>'.join(ret)
    # [END speech_transcribe_auto_punctuation]

# Imports the Google Cloud client library

# def upload_file(file_stram, filename, content_type)
#     from google.cloud import storage
#     # Instantiates a client
#     storage_client = storage.Client()
#
#     # The name for the new bucket
#     bucket_name = 'my-new-bucket'
#     # Creates the new bucket
#     bucket = storage_client.create_bucket(bucket_name)
#     blob = bucket.blob(filename)
#
#     blob.upload_from_string(
#         file_stream)
#
#     url = blob.public_url
#     if isinstance(url, six.binary_type):
#         url = url.decode('utf-8')
#
#     return url

#print('Bucket {} created.'.format(bucket.name))
