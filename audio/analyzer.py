import librosa
import numpy as np

def analyze_audio(file_path):
    y, sr = librosa.load(file_path, sr=44100)
    
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)    
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    return {
        "tempo": tempo,
        "beat_times": beat_times
    }

