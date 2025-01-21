from serial import Serial
import serial.tools.list_ports as listCom

# THIS MODULE REQUIRES HANDLING IN UI
#   STORING OF OBTAINED VALUES ARE HANDLED IN UI

class CalibModule:
    #Initialize Serial Object
    def __init__(self, com_port='COM5', baud_rate=115200, timeout=2, bool_print=False):
        self.serial_obj = Serial(port=com_port, baudrate=baud_rate, timeout=timeout)
        self.bool_print = bool_print
        self.msg_list = []
        if self.bool_print:
            print("Initialized module")

    def rcvmsg(self):
        msg = self.serial_obj.readline().decode().strip()

        self.msg_list.append(msg)

        if self.bool_print:
            print(msg)
        return msg

    def send_data(self, msg):
        data = msg
        if type(data) == str:
            data = data.encode()
        if self.bool_print:
            print(f"Sent {data}")
        self.serial_obj.write(data)

def detect_serial_auto(bool_print=False, searchKey = "Arduino"):
    ports = listCom.comports()

    detected_list = []
    selected_auto = ''

    for port, desc, hwid in sorted(ports):
        detected_list.append("{}: {} [{}]".format(port, desc, hwid))
        if searchKey in desc:
            selected_auto = f"{port}"
    
    if bool_print:
        print(f"Selected: {selected_auto}")
        print("List of all ports: ")
        for i in range(len(detected_list)):
            print(f"\t{i} - {detected_list[i]}")

    return selected_auto, detected_list
