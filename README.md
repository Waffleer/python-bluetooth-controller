# python bluetooth controller
 
This is a script to send data packets over a bluetooth connection via a COM port.

This uses an xbox controller to get inputs and puts them into a string which is sent over a serial connection to reviving raspberry pi pico with a bluetooth connection

# how to install

Install latest version of python 3
Install packages serialpy & inputs
    - pip install serialpy
    - pip install inputs

Download the two main.py files, they are different so dont mix them up

Connect to raspberry pi via bluetooth

Go to settings
In "Bluetooth & Devices" go to "More Bluetooth settings"

Click on "COM Ports"

See what COM port is being used for outgoing traffic to your pico 
    You need to be connected via bluetooth for this to work

    go to computer/main.py and change to the correct COM port, default is 5


Add pico/main.py to your raspberry pi pico
    I normally use Thonny IDE for working with my pico
        https://thonny.org/


Run main.py on your pico

Run computer/main.py on your computer and you should see a serial output in thonny from your pico

You can connect a controller and have it read your inputs, this code works with my wired xbox controller but i dont know beyond that

Good luck and have fun, feel free to reach out if you have any questions