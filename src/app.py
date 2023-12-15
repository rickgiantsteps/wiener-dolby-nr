# app.py
from flask_cors import CORS
from flask import Flask, request, jsonify, send_file, render_template
import soundfile as sf
import os
import numpy as np
import scipy as sp

app = Flask(__name__)
CORS(app)

AUDIO = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audio')
os.makedirs(AUDIO, exist_ok=True)

UPLOAD_FOLDER = os.path.join(AUDIO, 'uploads')
NOISE_FOLDER = os.path.join(AUDIO, 'noise')
PROCESSED_FOLDER = os.path.join(AUDIO, 'processed')
DENOISED_FOLDER = os.path.join(AUDIO, 'denoised')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(NOISE_FOLDER, exist_ok=True)
os.makedirs(DENOISED_FOLDER, exist_ok=True)

# Set windowing parameters
window_length = 1024
hop = window_length / 4
window = np.hanning(window_length)

# Inizialize output
zeropad_factor = window_length*4 #power of 2 for better performing fft

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
            processed_filename, noise_filename = process_audio(filename)
            return jsonify({'message': 'Upload successful', 'processed_filename': os.path.basename(processed_filename), 'noise_filename': os.path.basename(noise_filename)})
            

    except Exception as e:
        # Log the exception for debugging
        print(f"Exception: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500
        
def process_audio(input_filename):
    # Specify the output filename for the processed audio
    output_filename = os.path.join(PROCESSED_FOLDER, os.path.basename(input_filename))
    output_filename_noise = os.path.join(NOISE_FOLDER, 'noise_'+os.path.basename(input_filename))
    

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
    sf.write(output_filename_noise, noise, samplerate)

    return output_filename, output_filename_noise

if __name__ == '__main__':
    app.run(port=5000)

@app.route('/api/denoise',  methods=['POST'])
def denoise():
    try:
        if 'filename' not in request.form:
            return jsonify({'error': 'No filename provided'}), 400

        filename = os.path.join(PROCESSED_FOLDER, request.form['filename'])
        
        filename_clean = os.path.join(UPLOAD_FOLDER, request.form['filename_clean'])
        
        filename_noise = os.path.join(NOISE_FOLDER, request.form['noise_'+'filename_noise'])

        if not os.path.exists(filename):
            return jsonify({'error': 'File not found'}), 404

        denoised_filename = denoise_audio(filename, filename_clean, filename_noise)

        return jsonify({'message': 'Denoising successful', 'denoised_filename': os.path.basename(denoised_filename)})

    except Exception as ee:
        # Log the exception for debugging
        print(f"Exception: {str(ee)}")
        return jsonify({'error': 'Internal Server Error'}), 500

def pdf_calculator(samplerate, clean_song, noise):
    print("Computing PSD . . . ")
    f, clean_song_PSD = sp.signal.periodogram(clean_song, samplerate, 'hamming', zeropad_factor*2-1)
    fn, noise_PSD = sp.signal.periodogram(noise, samplerate, 'hamming', zeropad_factor*2-1)
    
    return clean_song_PSD, noise_PSD

def denoise_audio(input_filename, input_filename_clean, input_filename_noise):
    # Specify the output filename for the processed audio
    output_filename = os.path.join(DENOISED_FOLDER, os.path.basename(input_filename))

    # Load the audio file
    data, samplerate = sf.read(input_filename)
    data_clean, samplerate_clean = sf.read(input_filename_clean)
    data_noise, samplerate_noise = sf.read(input_filename_noise)

    # Set the length of the output as the shorter of the two inputs
    length = min(len(data_clean),len(data_noise))      
    
    # Set windowing parameters
    window_length = 1024
    hop = window_length / 4
    window = np.hanning(window_length)
    
    # Number of windows that will be generated
    window_number = np.floor((length-window_length)/hop) + 1
    
    # Inizialize output
    zeropad_factor = window_length*4 #power of 2 for better performing fft
    song_emph = np.zeros(length+zeropad_factor)
    out_dolby = np.zeros(length+zeropad_factor)
    
    #PDF calculation
    clean_song_PSD, noise_PSD = pdf_calculator(samplerate, data_clean, data_noise)
    
    print("Applying Wiener DolbyNR . . . ")
    for k in range(0, int(window_number)):

        # Extract frames with windows
        song_frame = window*data_clean[int(k*hop): int(k*hop + window_length)]
        noise_frame = window*data_noise[int(k*hop): int(k*hop + window_length)]

        # FFT
        song_frame_fft = np.fft.fft(song_frame, n=zeropad_factor)
        noise_frame_fft = np.fft.fft(noise_frame, n=zeropad_factor)

        # Emphasis filter
        song_emphasis = song_frame_fft * np.sqrt(noise_PSD/clean_song_PSD)

        noisy_song_emphasis = song_emphasis + noise_frame_fft

        noisy_song_emphasis *= 0.5

        # Deemphasis filter
        noisy_song_deemphasis = noisy_song_emphasis * np.sqrt((2*clean_song_PSD)/noise_PSD)

        out_dolby[int((k*hop)):int((k*hop + (zeropad_factor)))] += np.fft.ifft(noisy_song_deemphasis).real
        
        return sp.io.wavfile.write("denoised_song", samplerate, out_dolby.astype(np.int16))



