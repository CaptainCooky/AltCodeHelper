
### `alt_code_tooltip.py`

import PySimpleGUI as sg
import keyboard
import threading

# Define the ALT codes
alt_codes = {
    'Alt+0193': 'Á', 'Alt+0225': 'á',
    'Alt+0192': 'À', 'Alt+0224': 'à',
    'Alt+0194': 'Â', 'Alt+0226': 'â',
    'Alt+0195': 'Ã', 'Alt+0227': 'ã',
    'Alt+0196': 'Ä', 'Alt+0228': 'ä',
    'Alt+0199': 'Ç', 'Alt+0231': 'ç',
    'Alt+0200': 'È', 'Alt+0232': 'è',
    'Alt+0201': 'É', 'Alt+0233': 'é',
    'Alt+0202': 'Ê', 'Alt+0234': 'ê',
    'Alt+0203': 'Ë', 'Alt+0235': 'ë',
    'Alt+0204': 'Ì', 'Alt+0236': 'ì',
    'Alt+0205': 'Í', 'Alt+0237': 'í',
    'Alt+0206': 'Î', 'Alt+0238': 'î',
    'Alt+0207': 'Ï', 'Alt+0239': 'ï',
    'Alt+0210': 'Ò', 'Alt+0242': 'ò',
    'Alt+0211': 'Ó', 'Alt+0243': 'ó',
    'Alt+0212': 'Ô', 'Alt+0244': 'ô',
    'Alt+0213': 'Õ', 'Alt+0245': 'õ',
    'Alt+0214': 'Ö', 'Alt+0246': 'ö',
    'Alt+0216': 'Ø', 'Alt+0248': 'ø',
    'Alt+0217': 'Ù', 'Alt+0249': 'ù',
    'Alt+0218': 'Ú', 'Alt+0250': 'ú',
    'Alt+0219': 'Û', 'Alt+0251': 'û',
    'Alt+0220': 'Ü', 'Alt+0252': 'ü',
    'Alt+0221': 'Ý', 'Alt+0253': 'ý',
    'Alt+0222': 'Þ', 'Alt+0254': 'þ',
}

# Format the ALT codes into a string for the tooltip
tooltip_text = "\n".join([f"{code}: {char}" for code, char in alt_codes.items()])

# Function to show the tooltip
def show_tooltip():
    layout = [[sg.Text(tooltip_text)]]
    window = sg.Window('ALT Codes', layout, keep_on_top=True, finalize=True, element_justification='center', modal=True, grab_anywhere=True)
    window.read(timeout=5000)  # Close the window after 5 seconds

# Function to listen for ALT+0 key press
def listen_for_keypress():
    keyboard.wait('alt+0')
    show_tooltip()
    listen_for_keypress()  # Recursively listen for the key press

# Run the key press listener in a separate thread
thread = threading.Thread(target=listen_for_keypress)
thread.start()
