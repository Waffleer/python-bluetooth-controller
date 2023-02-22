#Basic code for receiving serial connection

from machine import UART #importing PIN and PWM

#Defining UART channel and Baud Rate
uart= UART(0,9600)

while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        #print(data)

        # Decodes data and splits string into a list
        data = data.decode("ASCII").split(",")
        
        #Spliting array into variables and typecasting to an int
        x = int(data[0])
        y = int(data[1])
        a = int(data[2])
        b = int(data[3])
        rt = int(data[4])
        lt = int(data[5])
        
        print(f" {x} | {y} | {a} | {b} | {rt} | {lt} | ")
      
        
        