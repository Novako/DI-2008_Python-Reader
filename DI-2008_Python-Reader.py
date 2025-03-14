#<<< MODULE IMPORTS >>>#
import serial
import tkinter as tk
import time

#<<< MODIFY ANY VARIABLE DATA HERE >>>#
SER_PORT = 'COM3'                   # Example port on Windows
#SER_PORT = '/dev/ttyACM0'           # Example port on linux

#<<< SET UP >>>#
print("Attempting connection to serial port")
# Establish serial connection
try:
    serConn = serial.Serial(
        port=SER_PORT,
        baudrate=115200
    )
except Exception as error:
    print("Serial connection failed,", error)
    raise SystemExit
else:
    print("Serial connection successful!")

#<<< SERIAL COMMANDS >>>#
serConn.write(b"stop\r\n")          # Stop in case device was left scanning
time.sleep(0.2)
serConn.write(b"eol 2\r\n")         # Set End Of Line (eol) to 1
time.sleep(0.2)
serConn.write(b"encode 1\r\n")      # Set the device to ASCII mode
time.sleep(0.2)
serConn.write(b"slist 0 2304\r\n")  # Set channel 1 to +/-25V
time.sleep(0.2)
serConn.write(b"slist 1 5895\r\n")  # Set channel 8 to Type-T thermocouple
time.sleep(0.2)
serConn.write(b"srate 500\r\n")     # Set sample rate
time.sleep(0.2)
serConn.write(b"dec 1\r\n")         # Set decimation factor
time.sleep(0.2)
serConn.reset_input_buffer()        # Flush all command responses
time.sleep(0.2)
serConn.write(b"start 0\r\n")       # Start scanning
time.sleep(0.5)

#<<< GUI WINDOW >>>#
# Initialize window
window = tk.Tk()
window.title("DI-2008 Reader")
window.geometry("300x50")

# Create label
tk.Label(window, text="Scanning in progress").pack()

# Create program quit button; click this button to stop scanning
tk.Button(window, text="Quit", command=window.destroy).pack()

# Refresh window
window.update()

#<<< CONTINUOUS SCANNING >>>#
while True:
    # Attempt to obtain state of the tk window
    try:
        window.state()
        window.update()
    # Window was closed, proceed with shutdown procedure
    except:
        print("Scanning has stopped")
        serConn.write(b"stop\r")
        time.sleep(0.2)
        serConn.close()
        print("Good-Bye!")
        break
    # State of window was found, proceed with line read
    else:
        line = serConn.readline().decode("utf-8")
        print(line)