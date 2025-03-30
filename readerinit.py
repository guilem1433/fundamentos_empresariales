import serial

def init_nfc_reader(port='/dev/ttyUSB0', baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate)
        print(f"NFC Reader initialized on port {port} with baudrate {baudrate}")
        return ser
    except serial.SerialException as e:
        print(f"Error initializing NFC Reader: {e}")
        return None

def read_nfc_data(serial_connection):
    if serial_connection:
        try:
            while True:
                if serial_connection.in_waiting > 0:
                    data = serial_connection.readline().decode('utf-8').strip()
                    print(f"Read data: {data}")
                    return data
        except Exception as e:
            print(f"Error reading NFC data: {e}")
    else:
        print("No serial connection available.")

if __name__ == "__main__":
    ser = init_nfc_reader()
    read_nfc_data(ser)


