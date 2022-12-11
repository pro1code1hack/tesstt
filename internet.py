import webbrowser as wb
from voice_handler import get_recognizer, record_audio, process_audio


def google_info():
    url = "http://www.google.com/search?q="
    rec = get_recognizer()
    audio = record_audio(rec, timeout=8)
    query = process_audio(rec, audio)
    wb.open(url + query)


def get_currency():
    url = "https://www.google.com/search?q=курс+доллара+к+гривне"
    wb.open(url)