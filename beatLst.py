from aubio import source, onset
# https://aubio.org/doc/latest/onset_2test-onset_8c-example.html
# https://github.com/aubio/aubio/blob/master/python/demos/demo_onset.py
def onsettimes_list(file_path):
    window_size = 1024 # FFT size
    hop_size = window_size // 4

    sample_rate = 0
    s = source(file_path, sample_rate, hop_size)
    sample_rate = s.samplerate
    Onset = onset('default', window_size, hop_size)

    OnsetsList = [] # 
    total_frames = 0
    while True: # read frames
        samples, framesRead = s()
        if Onset(samples):
            onset_time = Onset.get_last_s()
            OnsetsList.append(onset_time*1000)
        total_frames += framesRead
        if framesRead < hop_size:   break
    return OnsetsList
















