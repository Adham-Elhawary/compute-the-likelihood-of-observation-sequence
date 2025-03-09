import librosa
import numpy as np
from scipy.stats import norm
from scipy.special import logsumexp


def compute_likelihood(wav_file):
    y, sr = librosa.load(wav_file, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T
    average_mfcc = np.mean(mfccs, axis=0)
    n_features = average_mfcc.shape[0]
    n_observations = mfccs.shape[0]
    n_states = 6
    variances = np.ones(n_features)
    A = np.zeros((n_states, n_states))

    for i in range(n_states - 1):
        A[i, i] = 0.5
        A[i, i + 1] = 0.5
    A[-1, -1] = 1.0
    pi = np.zeros(n_states)
    pi[0] = 1.0
    log_alpha = np.full((n_observations, n_states), -np.inf)
    log_b = 0.0

    for d in range(n_features):
        log_b += norm.logpdf(mfccs[0, d], loc=average_mfcc[d], scale=np.sqrt(variances[d]))
    log_alpha[0, 0] = np.log(pi[0]) + log_b


    for t in range(1, n_observations):
        log_b = 0.0
        for d in range(n_features):
            log_b += norm.logpdf(mfccs[t, d], loc=average_mfcc[d], scale=np.sqrt(variances[d]))

        for j in range(n_states):
            safe_transitions = np.where(A[:, j] > 0, A[:, j], np.finfo(float).eps)
            log_trans = np.log(safe_transitions)
            log_sum = logsumexp(log_alpha[t - 1] + log_trans)
            log_alpha[t, j] = log_sum + log_b

    log_likelihood = logsumexp(log_alpha[-1])
    return log_likelihood

if __name__ == "__main__":
    likelihood = compute_likelihood(r"C:\Users\Adham\Downloads\download.wav")
    print(f"Log likelihood: {likelihood}")