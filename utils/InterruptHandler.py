import signal

def sigint_handler(signal, frame):
    """
    InterruptHandler

    if user canceld process it simply shows KeyboardInterrupt
    """
    print ('\nKeyboardInterrupt')
    exit(1)
