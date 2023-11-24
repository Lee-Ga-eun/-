
import RPi.GPIO as gpio
import time
import speech_recognition as sr

r=sr.Recognizer()
mic=sr.Microphone()

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT) # led

try:
    while True:
        with mic as source:
            print('say something')
        
        answer=r.recognize_google_cloud(r.listen(source), language='ko', credentials_json='json파일위치')
        
        if '불 켜' in answer:
            gpio.output(16,True)
except sr.UnknownValueError:
    print()
except sr.RequestError:
    print()
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()