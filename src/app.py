# app.py
from flask_cors import CORS
from flask import Flask, request, jsonify, send_file, render_template
import soundfile as sf
import os
import numpy as np

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
PROCESSED_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'processed')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['audio']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            processed_filename = process_audio(filename)
            return jsonify({'message': 'Upload successful', 'processed_filename': os.path.basename(processed_filename)})

    except Exception as e:
        # Log the exception for debugging
        print(f"Exception: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500


def process_audio(input_filename):
    # Specify the output filename for the processed audio
    output_filename = os.path.join(PROCESSED_FOLDER, os.path.basename(input_filename))

    # Load the audio file
    data, samplerate = sf.read(input_filename)

    # Check if the audio data is stereo
    if len(data.shape) == 2:
        # Generate stereo noise with the same number of channels and samples
        noise = np.random.normal(0, 0.005, data.shape)
    else:
        # Generate mono noise for mono audio data
        noise = np.random.normal(0, 0.005, len(data))

    # Add the noise to the audio data
    processed_data = data + noise

    # Write the processed audio to a new file
    sf.write(output_filename, processed_data, samplerate)

    return output_filename

if __name__ == '__main__':
    app.run(port=5000)
