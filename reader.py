from readerinit import init_nfc_reader, read_nfc_data

def process_nfc_data(data):
    if data:
        # Add your data processing logic here
        print(f"Processing data: {data}")
    else:
        print("No data to process.")

if __name__ == "__main__":
    ser = init_nfc_reader()
    data = init_nfc_reader(ser)
    process_nfc_data(data)