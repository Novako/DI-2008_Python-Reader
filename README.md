# DI-2008_Python-Reader
ASCII Python code for DI-2008. Compatible with Linux and Windows

**Prerequisites**:

1) Install Python [code was tested on 3.9]

2) Verify that the following Python packages are installed:
    - pyserial
    - tkinter
    - time

3) Latest firmware for the DI-2008 is recommended https://github.com/dataq-instruments/2008_Firmware_Upgrade. 

4) To better understand the protocol, please refer to https://www.dataq.com/resources/pdfs/misc/di-2008%20protocol.pdf. Note that the 16-bit scan list definition is written from bit 15 to bit 0 and then is converted to decimal when writing the serial code.

5) Plug the device to USB port. If the LED already blinks Yellow, stop, you are already in CDC mode. If not, once the LED turns blinking Green, push the button 5 times, the LED should blink yellow to indicate CDC mode. If you need to exit CDC mode, repeate the same action and a green blinking LED will indicate LibUSB mode.

6) Find out the COM port in use

    - From Windows Device Manager, find out the COM port of the device connected to, and modify the program accordingly<br/>
    ![alt text](https://www.dataq.com/resources/repository/matlab_devicemanager.png)

    - On Linux machines, use the command `dmesg | grep tty` to list connected devices. The device will be described as a "USB ACM device"
    
7) Modify the sample with the correct COM port number

8) The output from this example has two channels: the first is a +/-25 voltage input set on Channel 1, and the second is a Type-T TC input set on Channel 8. The voltage channel will need to be multiplied by 25 to display the correctly scaled measurement. 

9) If you have trouble using Python, you can use any serial terminal program (such as TeraTerm) to connect to DI-2008 and type in the commands manually, as following

   ![alt text](https://www.dataq.com/resources/images/cdc2008.png)
