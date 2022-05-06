from PiicoDev_QMC6310 import PiicoDev_QMC6310     #Importing QMC6310 LIBs
from PiicoDev_Unified import sleep_ms

magSensor = PiicoDev_QMC6310(range=3000) # initialise the magnetometer    , 3000 Micro Tesla is the limit of QMC6310
magSensor.calibrate()   #calibrate QMC6310 IF NOT CALIBRATED BEFORE

threshold = 120 # microTesla or 'uT'.

while True:

    strength = magSensor.readMagnitude()   # Reads the magnetic-field strength in microTesla (uT)
    myString = str(strength) + ' uT'       # create a string with the field-strength and the unit
    print(myString)                        # Print the field strength
    
    if strength > threshold:               # Check if the magnetic field is strong
        print('Strong Magnet!')

    sleep_ms(1000)
