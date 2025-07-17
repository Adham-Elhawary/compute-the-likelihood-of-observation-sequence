# 🗣️ Project Title: Speech Command Log-Likelihood Estimator

## 📌 Description
A Python-based tool that calculates the **log-likelihood of spoken commands** in audio files using a basic **Hidden Markov Model (HMM)** with **MFCC features**. Ideal for speech recognition, signal modeling, or HMM demonstrations.

---

## 🎯 Purpose / Motivation
- [ ] Audio classification or keyword spotting
- [ ] Educational demo of HMMs in Python
- [ ] Research in speech recognition or audio modeling
- [ ] Other: *(specify)*

---

## 🧩 Key Features
- [x] MFCC feature extraction using `librosa`
- [x] Manual implementation of a left-to-right HMM
- [x] Gaussian emission probabilities
- [x] Log-domain forward algorithm for numerical stability
- [x] Outputs sequence log-likelihood

---

## 📁 Project Structure
project/
│
├── hmm_audio_likelihood.py # Main script
├── sample_audio.wav # (Optional) test audio file
├── requirements.txt # Dependencies
└── README.md # This file

---

## ⚙️ Installation

### ✅ Dependencies
Install Python libraries:

```bash
pip install librosa numpy scipy

---

## ⚒️ Configuration

| Parameter   | Default | Description                         |
|-------------|---------|-------------------------------------|
| `n_states`  | 6       | Number of HMM states                |
| `n_mfcc`    | 13      | Number of MFCC features             |
| `variances` | 1.0     | Gaussian variance per feature       |

---

## 📚 References

- [Librosa Documentation](https://librosa.org/doc/latest/)
- [Hidden Markov Models (Wikipedia)](https://en.wikipedia.org/wiki/Hidden_Markov_model)
- [MFCC Explained](https://haythamfayek.com/2016/04/21/speech-processing-for-machine-learning.html)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/YourFeature

