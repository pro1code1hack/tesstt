
from voice_handler import get_recognizer, record_audio, process_audio


def save_data():
    rec = get_recognizer()
    audio = record_audio(rec, timeout=8)
    data = process_audio(rec, audio)
    with open('readme.txt', 'w') as f:
        f.write(data)