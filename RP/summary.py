App 




from picamera import PiCamera
camera=PiCamera()
import time
import RPi.GPIO as gpio
import mqtt.paho.client as mqtt
import mqtt.paho.publish as publish
import json
import Adafruit_DHT as dht
import speech_recognition as sr
from RPLCD.i2c import CharLCD
lcd=CharLCD('PCF8574', 0x27)



# stt


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




# pub.py


# dht_pub.py
# RP 

import RPi.GPIO as gpio
import Adafruit_DHT 
import paho.mqtt.client as mqtt
gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.OUT) #led

def on_publish(c,u,m):
    print("publish")

def on_message(client, userdata, msg): # 값을 읽어들임
    #msg.payload.msg('utf-8')
    get_value=msg.payload.decode('utf-8')
    if(get_value=='on'):
        gpio.output(16,True)
    elif(get_value=='off'):
        gpio.output(16,False)
        

def on_connect(client,b,c,d):
    client.subscribe('dht/CCL') # 토픽 연결
    

client=mqtt.Client()
client.on_publish=on_publish
client.on_message=on_message
client.on_connect=on_connect
client.connect('test.org', 1883, 60)
client.loop_start() # 루프 스타트

try:
    while True:
        # dht 값 publish 하기
        # humi temp순서 기억하기
        humi, temp = Adafruit_DHT.read_retry(22, 23)
        if humi and temp:
            # 둘 다 값이 있을 때
            data={'temp': round(temp,1), 'humi': round(humi,1)}
            client.publish('dht/CCL', data)
except keyboardInterrupt:
    pass
finally:
    gpio.cleanup()



# sub.py

# dht_sub.py
# PC

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def on_message(client, data, msg):
    print('message 처리')
    # dht 메시지를 받고, 다시 publish해야함
    get_data=str(msg.payload.decode('utf-8')) # 문자열 처리 주의
    if get_data!='on' and get_data!='off':
        
        y=eval(get_data)  #딕셔너리가 통채로 넘어옴
        
        if(y['temp']>25):
            # 25도 이상이면
            publish.single('dht/CCL', 'on', hostname='test.org')
        else:
            publish.single('dht/CCL', 'off', hostname='test.org')
        
    

def on_publish(client,data, m):
    print('pub')

def on_connect(client,data,m, rc):
    mqtt.subscribe('dht/CCL')
    
def on_disconnect(client, data,m ):
    print(disconnect)




client=mqtt.Client()
client.on_message=on_message
client.on_publish=on_publish
client.on_disconnect=on_disconnect
client.on_connect=on_connect #subscribe(토픽)
client.connect('test.org', 1883, 60)
client.loop_forever() #루프포에버 영ㅇ원히 구독하겠슴다!!






# settings
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# pin 
button_pin = 12 # 32
pir_pin = 24 # 18
buzzer_pin = 25 # 22
dht_type = 22 
dht_pin = 23 # 16
red_led_pin = 16 # 36
blue_led_pin = 20 # 38
green_led_pin = 21 # 40

# led pwm
pwm_led = GPIO.PWM(16, 500)
pwm_led.start(0)
try:
    while True:
        for i in range(0,101,5):
            pwm_led.ChangeDutyCycle(i) 
            time.sleep(0.02)
        for i in range(100,-1,-5): 
            pwm_led.ChangeDutyCycle(i) 
            time.sleep(0.02)
except KeyboardInterrupt:
    pass
finally:
    pwm_led.stop()
    GPIO.cleanup()


# button
def button_callback(chaneel):
    pass

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback)


# pir
def pir_callback(chaneel):
    pass

GPIO.setup(pir_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pir_pin, GPIO.FALLING, callback=pir_callback)


# buzzer
GPIO.setup(buzzer_pin, GPIO.OUT)
def buzz(): 
    pitch = 1000 
    duration = 0.1 
    period = 1.0 / pitch 
    delay = period / 2 
    cycles = int(duration * pitch)
    for i in range(cycles):
        GPIO.output(buzzer_pin,True)
        time.sleep(delay)
        GPIO.output(buzzer_pin,False)
        time.sleep(delay)

# buzzer pwm
pwm=GPIO.PWM(buzzer_pin, 261) 
pwm.start(90.0) 
time.sleep(3.0) 
pwm.stop()


# lcd
# SDA 3, SCL 5
from RPLCD.i2c import CharLCD
lcd = CharLCD('PCF8574', 0x27) 
lcd.write_string() 
lcd.crlf() 
lcd.clear()
lcd.cursor_pos = (0,0)


# dht
import Adafruit_DHT
humidity, temperature = Adafruit_DHT.read_retry(dht_type, dht_pin) 
if humidity is not None and temperature is not None: 
    humid = str(round(humidity,1)) 
    temp = str(round(temperature,1)) 


# camera
from picamera import PiCamera
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.capture('example.jpg') 
camera.close()


# mqtt - rp
import paho.mqtt.client as mqtt
import time

import json
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "dht/CCL"

def on_publish(client, userdata, mid):
    print ("Message Published...")
def on_connect ( client, userdata , flags, rc ):
    print("Connect with result code" + str (rc))
    client.subscribe("dht/CCL")
def on_message(client, userdata, msg):
    x = str(msg.payload.decode('utf-8'))
    if x == "on": 
        GPIO.output(16, True)
    elif x == "off":
        GPIO.output(16, False)
def on_pre_connect(client, data):
    return

client = mqtt.Client()

client.on_publish = on_publish
client.on_connect = on_connect
client.on_message = on_message
client.on_pre_connect = on_pre_connect

client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
client.loop_start()
try:
    while True:
        data = {'key1':'value1', 'key2' : 'value2'}
        client.publish(MQTT_TOPIC, str(data))
        print('Published. Sleeping ...')
        
except keyboardInterrup:
    GPIO.cleanup()


# mqtt - pc
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
normal_temp = 25.0 
MQTT_Broker = "test.mosquitto.org" 
def on_connect ( client, userdata , flags, rc ):
    print("Connect with result code" + str (rc) )
    client.subscribe("dht/CCL") 
def on_message ( client, userdata , msg ) :
    x = str(msg.payload.decode('utf-8')) 
    print(msg.topic + " " + x)
    if (x!= "on" and x != "off"):
        y = eval(x) 
        if y["temperature"] > normal_temp:
            publish.single("dht/CCL", "on",hostname = 
            MQTT_Broker)
        elif y["temperature"] <= normal_temp:
            publish.single("dht/CCL", "off",hostname = 
            MQTT_Broker)

def on_publish(client, userdata, mid):
    print("message publish..")
def on_disconnect(client, userdata, rc):
    print("Disconnected")
def on_pre_connect(client, data):
    return

client = mqtt.Client ()
client.on_connect = on_connect
client.connect(MQTT_Broker, 1883, 60)
client.on_message = on_message
client.on_publish = on_publish
client.on_pre_connect = on_pre_connect 
client.on_disconnect = on_disconnect
client.loop_forever()


"""
1. rp(pub) data를 publish (while True) ex. DHT
2. pc(sub) data를 subcsribe 
    2-1. on_connet 함수에서 subscribe 함수로 sub
    2-2. on_message 함수에서 pub msg를 받아서 처리
3. pc(pub) data를 publish.single (in on_message) 
    3-1. eval 함수를 사용하기 때문에 if문으로 적절한 유효성 검증 필요
4. rp(sub) data를 subscribe -> 센서 조작 ex. led, lcd
"""


# stt
import speech_recognition as sr
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""/home/pi/git/iot-programming-with-raspi/iot-p-405100-4d785ea5814e.json"""
r = sr.Recognizer()
mic = sr.Microphone()
try:
    while True:
        with mic as source:
            print("Say something!")
            audio = r.listen(source)
        gcSTT = r.recognize_google_cloud(audio, language = 'ko',credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
except KeyboardInterrupt:
    GPIO.cleanup()







"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
 