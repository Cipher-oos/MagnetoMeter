from machine import ADC, Pin      
import time
import datetime
import remap

adc = ADC(Pin(26))
sensor_val=0
PrevGauss=0
cal=0
reading = adc.read_u16
VoltageRef=5
ADC_Voltage = (reading * VoltageRef) / 1024         #converting analog value to digtal value from 0-1023 to 0-5
Voltage = ADC_Voltage
Cal = Voltage           #Calibration voltage

while True :
    ADC_Voltage = (reading * VoltageRef) / 1024.0
    Voltage = ADC_Voltage
    if Voltage >= cal :
        Gauss = ((Voltage - Cal)/0.00033)







def sensorCallback(channel):
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if adc.read_u16(channel):
   
    print(adc.read_u16 Gauss)
  else:
    # Magnet
    print("Sensor LOW " + stamp)



