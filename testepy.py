import RPi.GPIO as GPIO
import time
import os
import serial

def open_serial_port():
    try:
        ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

ser = open_serial_port()

filename = "/usr/local/bin/testepy-master/posicao.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        flag = "a"
        file.write(flag)
else:
    with open(filename, "r") as file:
        flag = file.read().strip()
        print(f"Conteúdo do arquivo: {flag}")

led1 = 17
led2 = 18
led3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

try:
    while True:
        if flag == "a":
            GPIO.output(led1, GPIO.HIGH)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.LOW)

            with open(filename, "w") as file:
                file.write("a")
                print(f"Arquivo atualizado e Flag A escrito")
            flag = "b"

            if ser:
                try:
                    ser.write(b'a\n')
                    print("Enviado: A")
                except serial.SerialException as e:
                    print(f"Erro ao enviar via serial: {e}")
            time.sleep(4)
            
        elif flag == "b":
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.HIGH)
            GPIO.output(led3, GPIO.LOW)

            with open(filename, "w") as file:
                file.write("b")
                print(f"Arquivo atualizado e Flag B escrito")
            flag = "c"

            if ser:
                try:
                    ser.write(b'b\n')
                    print("Enviado: B")
                except serial.SerialException as e:
                    print(f"Erro ao enviar via serial: {e}")
            time.sleep(4)

        elif flag == "c":
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            GPIO.output(led3, GPIO.HIGH)

            with open(filename, "w") as file:
                file.write("c")
                print(f"Arquivo atualizado e Flag C escrito")
            flag = "a"

            if ser:
                try:
                    ser.write(b'c\n')
                    print("Enviado: C")
                except serial.SerialException as e:
                    print(f"Erro ao enviar via serial: {e}")
            time.sleep(4)

finally:
    GPIO.cleanup()
    if ser:
        ser.close()
    print("Aplicação encerrada")

