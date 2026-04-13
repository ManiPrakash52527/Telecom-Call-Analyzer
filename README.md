# Telecom Call Quality Analyzer

## Overview
This project analyzes the quality of telecom voice calls using Digital Signal Processing (DSP) techniques. It processes an audio recording and evaluates key parameters such as Signal-to-Noise Ratio (SNR), silence percentage, and background noise level to determine overall call quality.

---

## Features
- Signal-to-Noise Ratio (SNR) calculation  
- Silence detection using energy threshold  
- Background noise estimation  
- Waveform visualization (time domain)  
- Frequency spectrum analysis (FFT)  
- Spectrogram generation (STFT)  
- Automated call quality scoring  

---

## Technologies Used
- Python  
- NumPy  
- Librosa  
- Matplotlib  
- SciPy  
- Google Colab  

---

## Methodology
1. Upload call recording (.wav or .m4a)  
2. Convert audio into digital signal  
3. Perform frame-based analysis  
4. Calculate signal power and noise power  
5. Compute SNR  
6. Detect silence using energy threshold  
7. Generate graphical outputs  
8. Evaluate call quality score  

---

## Outputs
The system generates the following outputs:

- Waveform of the audio signal  
- Frame energy distribution  
- Frequency spectrum  
- Spectrogram  
- Call quality metrics (SNR, silence %, noise level)  

---

## How to Run
1. Open the project in Google Colab  
2. Install required libraries  
3. Upload your audio file  
4. Run the code  
5. View results and graphs  

---

## Applications
- Telecom network quality monitoring  
- VoIP call analysis  
- Call center performance evaluation  
- Speech signal analysis  
- Network performance optimization  

---

## Future Scope
- Real-time call quality monitoring  
- Machine learning-based quality prediction  
- Integration with telecom systems  
- Noise classification and filtering  

---

## Conclusion
This project demonstrates how DSP techniques can be applied to analyze and evaluate telecom call quality. It provides both numerical metrics and graphical insights, making it useful for understanding and improving communication systems.
