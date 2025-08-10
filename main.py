from microbit import *
import machine
import utime

# Configuración del servo
servo_pin = machine.Pin(0, machine.Pin.OUT)
servo = machine.PWM(servo_pin)
servo.freq(50)

def mover_servo(angulo):
    duty = int((angulo/180)*102 + 26)  # Conversión para SG90
    servo.duty(duty)

# Ejemplo básico: dispensar cada 10 segundos
while True:
    mover_servo(90)  # Abre compuerta
    sleep(2000)
    mover_servo(0)   # Cierra compuerta
    sleep(10000)

