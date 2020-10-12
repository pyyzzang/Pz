# -*- coding: utf-8 -*- 

import RPi.GPIO as GPIO
import time
import random
import sys
import Adafruit_DHT

# 빨, 주, 노, 초, 파, 남, 보
colors = [0xFF0000, 0xFF0023, 0xFF00FF, 0x0000FF, 0x00FF00, 0x64EB00, 0x4BFB00]
pins = {'pin_R':13, 'pin_G':19, 'pin_B':26}  # 핀 지정

 
GPIO.setmode(GPIO.BCM)       # GPIO BCM 모드 설정                                     
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # 핀 모드를 출력으로 설정
    GPIO.output(pins[i], GPIO.HIGH) # LED를 HIGH로 설정해서 LED 끄기
p_R = GPIO.PWM(pins['pin_R'], 2000)  # 주파수 설정 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 2000)

p_R.start(0)      # 초기 듀티 사이클 = 0 (LED 끄기)
p_G.start(0)
p_B.start(0)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
# LED 색을 설정하는 함수
def getDuty():   # 예)  col = 0x112233
    return random.randrange(0,100)


    

try:
    while True:                         # 무한 반복  
        for col in colors:
            p_R.ChangeDutyCycle(getDuty())     # 듀티 사이클 변경
            p_G.ChangeDutyCycle(getDuty())
            p_B.ChangeDutyCycle(getDuty())

            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 2)
            if humidity is not None and temperature is not None:
                print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))

except KeyboardInterrupt:                # Ctrl+c로 종료
    p_R.stop()
    p_G.stop()
    p_B.stop()

    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)    #LED 끄기
        GPIO.cleanup()