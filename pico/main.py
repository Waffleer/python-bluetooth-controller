#Basic code for receiving serial connection

from machine import UART, Pin, PWM #importing PIN and PWM

#Defining UART channel and Baud Rate
uart= UART(0,9600)



#OUT1  and OUT2
#Motor Controller 1
mc1_in1=Pin(6,Pin.OUT)  #IN1`
mc1_in2=Pin(7,Pin.OUT)  #IN2
mc1_in3=Pin(4,Pin.OUT)  #IN3
mc1_in4=Pin(3,Pin.OUT)  #IN4
mc1_EN_A=PWM(Pin(8))
mc1_EN_B=PWM(Pin(2))
# Defining frequency for enable pins
mc1_EN_A.freq(1500)
mc1_EN_B.freq(1500)
# Setting maximum duty cycle for maximum speed (0 to 65025)
mc1_EN_A.duty_u16(65025)
mc1_EN_B.duty_u16(65025)




def right_forward():
    print("Right Forward")
    mc1_in1.low()
    mc1_in2.high()
    
    
def right_backward():
    print("Right Backwards")
    mc1_in1.high()
    mc1_in2.low()
    
    
def left_forward():
    print("Left Forward")
    mc1_in3.low()
    mc1_in4.high()
    
    
def left_backward():
    print("Left Backwards")
    mc1_in3.high()
    mc1_in4.low()
    
    
def ry_stop():
    mc1_in1.low()
    mc1_in2.low()
    print("ry_stop")

def ly_stop():
    mc1_in3.low()
    mc1_in4.low()
    print("ly_stop")

    

def abs(num: int):
    if num < 0:
        num = num * -1
    return num

def drivetrain(ly: int, ry: int):
    
    # Shifts the number up 25 so help with the motor will spin
    ry_speed = int(abs(ry) * .75)
    if ry_speed > 10:
        ry_speed+=25
    else:
        ry_speed = 0
        
    ly_speed = int(abs(ly) * .75)
    if ly_speed > 10:
        ly_speed+=25
    else:
        ly_speed = 0
    
        
    
    
    print(f"{ly} | {ry}")
    ly_speed = float(abs(ly_speed))/100 * 65025
    ry_speed = float(abs(ry_speed))/100 * 65025
    
    
    mc1_EN_A.duty_u16(int(ly_speed)) #Setting Duty Cycle
    mc1_EN_B.duty_u16(int(ry_speed)) #Setting Duty Cycle
    
    print(f"{ly_speed} | {ry_speed}")
    
    if ry > 0:
        right_forward()
    elif ry < 0:
        right_backward()
    else:
        ry_stop()
    
    if ly > 0:
        left_forward()
    elif ly < 0:
        left_backward()
    else:
        ly_stop()
        
        
    
    


while True:
    if uart.any(): #Checking if data available
        data=uart.read() #Getting data
        #print(data)

        # Decodes data and splits string into a list
        data = data.decode("ASCII").split(",")
        
        #Spliting array into variables and typecasting to an int
        try:
            ly = int(data[0])
            ry = int(data[1])
            a = int(data[2])
            b = int(data[3])
            rt = int(data[4])
            lt = int(data[5])
        except ValueError:
            continue
        
        
        #Gets rid of controller drift
        if ly < 10 and ly > -10 :
            ly = 10
        if ry < 10 and ry > -10 :
            ry = 10
        
        #print(f" {x} | {y} | {a} | {b} | {rt} | {lt} | ")
        drivetrain(ly, ry)
      
        
        

