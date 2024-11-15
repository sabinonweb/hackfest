import os

def is_virtualenv():
    return 'VIRTUAL_ENV' in os.environ

def virtualenv():
    if is_virtualenv():
        print("Running inside a virtual environment.")
    else:
        print("Not running inside a virtual environment.")