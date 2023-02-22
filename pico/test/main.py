from machine import Pin,PWM,UART #importing PIN and PWM
import time #importing time

#Defining UART channel and Baud Rate
uart= UART(0,9600)

while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        print(data)