import json
import pyaudio
from vosk import Model, KaldiRecognizer
import pyfirmata
import sys

model = Model("vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model,16000)
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

board = pyfirmata.Arduino("COM3")


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        
        if rec.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]

for text in listen():
    if text == "Включить":
        board.digital[9].write(1) #Даємо сигнал 9 порту 
    elif text == "Выключить":
        board.digital[9].write(0) #Виключаємо
    elif text == "Выйти":
        sys.exit()