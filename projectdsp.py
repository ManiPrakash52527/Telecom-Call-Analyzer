# Telecom Call Quality Analyzer with Graphical Visualization

!pip install librosa soundfile

import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
from google.colab import files

print("Upload call audio file (.wav recommended)")
uploaded = files.upload()

filename = list(uploaded.keys())[0]

# Load audio
signal, sr = librosa.load(filename, sr=None)

duration = len(signal) / sr

print("Sampling Rate:", sr)
print("Duration:", duration, "seconds")

# -----------------------------
# SIGNAL POWER
# -----------------------------

signal_power = np.mean(signal**2)

# -----------------------------
# FRAME ENERGY CALCULATION
# -----------------------------

frame_length = int(0.02 * sr)
hop_length = int(0.01 * sr)

energy = []

for i in range(0, len(signal) - frame_length, hop_length):
    frame = signal[i:i+frame_length]
    energy.append(np.sum(frame**2))

energy = np.array(energy)

# Noise threshold
threshold = np.percentile(energy, 20)

noise_frames = energy[energy < threshold]
noise_power = np.mean(noise_frames)

# -----------------------------
# SNR
# -----------------------------

snr = 10 * np.log10(signal_power / noise_power)

# -----------------------------
# SILENCE DETECTION
# -----------------------------

silence_threshold = 0.01

silent_samples = np.sum(np.abs(signal) < silence_threshold)

silence_percentage = (silent_samples / len(signal)) * 100

# -----------------------------
# BACKGROUND NOISE LEVEL
# -----------------------------

background_noise_level = np.sqrt(noise_power)

# -----------------------------
# CALL QUALITY SCORE
# -----------------------------

quality_score = 0

if snr > 20:
    quality_score += 40
elif snr > 10:
    quality_score += 25
else:
    quality_score += 10

if silence_percentage < 20:
    quality_score += 30
elif silence_percentage < 40:
    quality_score += 20
else:
    quality_score += 10

if background_noise_level < 0.02:
    quality_score += 30
elif background_noise_level < 0.05:
    quality_score += 20
else:
    quality_score += 10

if quality_score > 80:
    quality = "Excellent"
elif quality_score > 60:
    quality = "Good"
elif quality_score > 40:
    quality = "Moderate"
else:
    quality = "Poor"

print("\nSNR:", snr, "dB")
print("Silence Percentage:", silence_percentage, "%")
print("Noise Level:", background_noise_level)
print("Call Quality Score:", quality_score, "/100")
print("Classification:", quality)

# ------------------------------------------------
# GRAPH 1 : Waveform
# ------------------------------------------------
plt.figure(figsize=(12,4))
librosa.display.waveshow(signal, sr=sr)
plt.title("Call Signal Waveform")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
# ------------------------------------------------
# GRAPH 2 : Frame Energy
# ------------------------------------------------
plt.figure(figsize=(12,4))
plt.plot(energy)
plt.axhline(threshold, linestyle='--')
plt.title("Frame Energy Distribution")
plt.xlabel("Frame Index")
plt.ylabel("Energy")
plt.show()
# ------------------------------------------------
# GRAPH 3 : Frequency Spectrum
# ------------------------------------------------
spectrum = np.fft.fft(signal)
freq = np.fft.fftfreq(len(signal), 1/sr)
plt.figure(figsize=(12,4))
plt.plot(freq[:len(freq)//2], np.abs(spectrum[:len(freq)//2]))
plt.title("Frequency Spectrum of Call Signal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

# ------------------------------------------------
# GRAPH 4 : Spectrogram
# ------------------------------------------------
plt.figure(figsize=(12,5))

S = librosa.stft(signal)
S_db = librosa.amplitude_to_db(abs(S))

librosa.display.specshow(S_db,
                         sr=sr,
                         x_axis='time',
                         y_axis='hz')
plt.colorbar()
plt.title("Spectrogram of Call Signal")
plt.show()
# ------------------------------------------------
# GRAPH 5 : Quality Score Chart
# ------------------------------------------------

metrics = ["SNR", "Silence", "Noise"]
values = [snr, silence_percentage, background_noise_level]

plt.figure(figsize=(6,4))
plt.bar(metrics, values)
plt.title("Call Quality Metrics")
plt.show()
