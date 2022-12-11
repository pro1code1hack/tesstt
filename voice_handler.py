import speech_recognition as sr


def get_recognizer():
    recognizer = sr.Recognizer()
    return recognizer


def record_audio(recognizer: sr.Recognizer, timeout=None):
    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(f"Recording for {4 if timeout is None else timeout} seconds")
        recorded_audio = recognizer.listen(source, timeout=timeout or 4)
        print("Done recording")
        return recorded_audio


def process_audio(recognizer: sr.Recognizer, recorded_audio: sr.AudioData):
    try:
        text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        )
        return text.lower()

    except Exception as ex:
        print(ex)
