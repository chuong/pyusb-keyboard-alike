from keyboard_alike import reader


class BarCodeReader(reader.Reader):
    """
    This class supports Acan USB bar code scanner configured to work as a keyboard
    http://www.dx.com/p/acan-9800-usb-laser-handheld-barcode-scanner-reader-for-desktop-laptop-2m-cable-34625
    """
    pass


if __name__ == "__main__":
    # Ouput of `dmesg | tail` after plugging the device
    # shows `idVendor=05fe, idProduct=1010`
    reader = BarCodeReader(0x05fe, 0x1010, 72, 8, should_reset=True)
    reader.initialize()
    print(reader.read().strip())
    reader.disconnect()
