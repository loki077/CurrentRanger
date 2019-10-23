import time
import serial

ser = serial.Serial(

	port='/dev/ttyACM2',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)

counter = 0

while True:
	x = ser.readline()
	print(x)

	