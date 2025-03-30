import sys
import os
from readerinit import init_nfc_reader, read_nfc_data

if __name__ == "__main__":
    ser = init_nfc_reader()
    read_nfc_data(ser)