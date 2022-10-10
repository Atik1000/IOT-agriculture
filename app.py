# def mp3_to_wav():
#     import os
#     from pydub import AudioSegment
#     import glob

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all mp3 files
#     mp3_files = glob.glob(cwd + "/*.mp3")

#     # Loop through all mp3 files
#     for mp3_file in mp3_files:
#         # Convert mp3 to wav
#         sound = AudioSegment.from_mp3(mp3_file)
#         wav_file = os.path.splitext(mp3_file)[0] + ".wav"
#         print("Converting %s to %s" % (mp3_file, wav_file))
#         sound.export(wav_file, format="wav")

#     # Remove all mp3 files
#     # for mp3_file in mp3_files:
#     #     os.remove(mp3_file)

# if __name__ == "__main__":
#     mp3_to_wav()


# # play the wav file
# def play_wav():
#     import os
#     import simpleaudio as sa

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all wav files
#     wav_files = glob.glob(cwd + "/*.wav")

#     # Loop through all wav files
#     for wav_file in wav_files:
#         # Play wav file
#         wave_obj = sa.WaveObject.from_wave_file(wav_file)
#         play_obj = wave_obj.play()
#         play_obj.wait_done()


# def noise_reduction():
#     import os
#     from pydub import AudioSegment
#     import glob

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all wav files
#     wav_files = glob.glob(cwd + "/*.wav")

#     # Loop through all wav files
#     for wav_file in wav_files:
#         # Apply noise reduction
#         sound = AudioSegment.from_file(wav_file)
#         noise_reduced_file = os.path.splitext(wav_file)[0] + "_NR.wav"
#         print("Applying noise reduction to %s to %s" % (wav_file, noise_reduced_file))
#         noise_reduced_sound = sound.low_pass_filter(1500).high_pass_filter(50)
#         noise_reduced_sound.export(noise_reduced_file, format="wav")



# def waveplot():
#     import os
#     from pydub import AudioSegment
#     import glob
#     import matplotlib.pyplot as plt

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all wav files
#     wav_files = glob.glob(cwd + "/*.wav")

#     # Loop through all wav files
#     for wav_file in wav_files:
#         # Apply noise reduction
#         sound = AudioSegment.from_file(wav_file)
#         noise_reduced_file = os.path.splitext(wav_file)[0] + "_NR.wav"
#         print("Applying noise reduction to %s to %s" % (wav_file, noise_reduced_file))
#         noise_reduced_sound = sound.low_pass_filter(1500).high_pass_filter(50)
#         noise_reduced_sound.export(noise_reduced_file, format="wav")

#         # Get the audio data
#         audio_data = noise_reduced_sound.get_array_of_samples()

#         # Plot the audio data
#         plt.plot(audio_data)
#         plt.show()
    

# def audio_sample_rate():
#     import os
#     from pydub import AudioSegment
#     import glob
#     import matplotlib.pyplot as plt

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all wav files
#     wav_files = glob.glob(cwd + "/*.wav")

#     # Loop through all wav files
#     for wav_file in wav_files:
#         # Apply noise reduction
#         sound = AudioSegment.from_file(wav_file)
#         noise_reduced_file = os.path.splitext(wav_file)[0] + "_NR.wav"
#         print("Applying noise reduction to %s to %s" % (wav_file, noise_reduced_file))
#         noise_reduced_sound = sound.low_pass_filter(1500).high_pass_filter(50)
#         noise_reduced_sound.export(noise_reduced_file, format="wav")

#         # Get the audio data
#         audio_data = noise_reduced_sound.get_array_of_samples()

#         # Plot the audio data
#         plt.plot(audio_data)
#         plt.show()

#         # Get the sample rate
#         sample_rate = noise_reduced_sound.frame_rate
#         print("Sample rate: %s" % sample_rate)



# def audio_voice_signature_detection():
#     import os
#     from pydub import AudioSegment
#     import glob
#     import matplotlib.pyplot as plt
#     import numpy as np
#     from scipy.io import wavfile
#     from scipy import signal
#     from scipy.fftpack import fft

#     # Get the current working directory
#     cwd = os.getcwd()

#     # Get all wav files
#     wav_files = glob.glob(cwd + "/*.wav")

#     # Loop through all wav files
#     for wav_file in wav_files:
#         # Apply noise reduction
#         sound = AudioSegment.from_file(wav_file)
#         noise_reduced_file = os.path.splitext(wav_file)[0] + "_NR.wav"
#         print("Applying noise reduction to %s to %s" % (wav_file, noise_reduced_file))
#         noise_reduced_sound = sound.low_pass_filter(1500).high_pass_filter(50)
#         noise_reduced_sound.export(noise_reduced_file, format="wav")

#         # Get the audio data
#         audio_data = noise_reduced_sound.get_array_of_samples()

#         # Plot the audio data
#         plt.plot(audio_data)
#         plt.show()

#         # Get the sample rate
#         sample_rate = noise_reduced_sound.frame_rate
#         print("Sample rate: %s" % sample_rate)

#         # Get the FFT
#         fft_out = fft(audio_data)

#         # Get the frequencies
#         frequencies = np.abs(fft_out)

#         # Get the maximum frequency
#         max_freq = frequencies.argmax()

#         # Get the voice signature
#         voice_signature = max_freq * sample_rate / len(audio_data)
#         print("Voice signature: %s" % voice_signature)

#         # Plot the frequencies
#         plt.plot(frequencies)
#         plt.show()

#         # Get the FFT frequencies
#         fft_freq = np.fft.fftfreq(len(frequencies), 1 / sample_rate)

#         # Plot the FFT frequencies
#         plt.plot(fft_freq, frequencies)
#         plt.show()

#         # Get the FFT frequencies
#         fft_freq = np.fft.fftfreq(len(frequencies), 1 / sample_rate)

#         # Plot the FFT frequencies
#         plt.plot(fft_freq, frequencies)
#         plt.show()

#         # Get the FFT frequencies
#         fft_freq = np.fft.fftfreq(len(frequencies), 1 / sample_rate)

#         # Plot the FFT frequencies
#         plt.plot(fft_freq, frequencies)
#         plt.show()

x axis =Time 
y axis =value

# proposed architectures

